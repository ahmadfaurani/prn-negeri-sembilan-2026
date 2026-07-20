#!/usr/bin/env python3
"""
Scan workspace directories for markdown files with embedded timestamps.
Compare 'Generated:' timestamps, 'Brief ID:' timestamps, and filename timestamps
against actual file creation time (stat birth time).
Report mismatches > 10 minutes.
"""

import os
import re
import json
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path

# MYT = UTC+8
MYT = timezone(timedelta(hours=8))
UTC = timezone.utc

# Directories to scan
BASE = "/home/p62operator/.openclaw"
WORKSPACE_DIRS = [
    os.path.join(BASE, "workspace-ns"),
    os.path.join(BASE, "workspace-hoi"),
    os.path.join(BASE, "workspace-weststar-rti"),
]

# Keywords for subdirectories to include
SUBDIR_KEYWORDS = ['intelligence', 'brief', 'daily', 'production']

# Directories to skip
SKIP_DIRS = {'.git', 'node_modules', '__pycache__'}
SKIP_PATTERNS = ['backup', '.bak']

# Threshold in minutes
THRESHOLD_MINUTES = 10


def should_skip(path_str):
    """Check if a path should be skipped."""
    parts = Path(path_str).parts
    for part in parts:
        if part in SKIP_DIRS:
            return True
        for pat in SKIP_PATTERNS:
            if pat in part.lower():
                return True
    return False


def is_relevant_directory(filepath):
    """Check if the file is in a relevant directory (workspace dir + subdir keywords)."""
    filepath = os.path.abspath(filepath)
    # Must be under one of the workspace dirs
    for ws in WORKSPACE_DIRS:
        ws = os.path.abspath(ws)
        if filepath.startswith(ws + '/'):
            # Check if any path component contains a keyword
            rel = filepath[len(ws)+1:]
            parts = rel.split('/')
            for part in parts[:-1]:  # exclude filename
                for kw in SUBDIR_KEYWORDS:
                    if kw in part.lower():
                        return True
            # Also include files directly in the workspace root or first-level subdirs
            # that match the keywords even partially in the filename
            # Actually, let's be inclusive - scan everything in the workspace dirs
            return True
    return False


def get_birth_time(filepath):
    """Get file birth time using stat --format='%W' (epoch seconds)."""
    try:
        # Use %W for birth time in seconds since epoch
        result = subprocess.run(
            ['stat', '--format=%W', filepath],
            capture_output=True, text=True, timeout=5
        )
        raw = result.stdout.strip()
        if raw == '-' or not raw or raw == '0':
            # Birth time not available, fall back to modification time %Y (epoch)
            result = subprocess.run(
                ['stat', '--format=%Y', filepath],
                capture_output=True, text=True, timeout=5
            )
            raw = result.stdout.strip()
            epoch = float(raw)
            return datetime.fromtimestamp(epoch, tz=UTC), 'mtime (birth unavailable)'
        
        epoch = float(raw)
        return datetime.fromtimestamp(epoch, tz=UTC), 'birth'
    except Exception as e:
        return None, f'error: {e}'


def parse_timestamp_str(ts_str, default_tz=MYT):
    """Parse a timestamp string that may be in various formats."""
    ts_str = ts_str.strip()
    
    # Try various formats
    formats = [
        # "2026-07-20 20:30 MYT" or "2026-07-20 20:30 UTC"
        # We handle timezone separately
        ("%Y-%m-%d %H:%M", None),
        ("%Y-%m-%d %H:%M:%S", None),
        ("%Y-%m-%dT%H:%M", None),
        ("%Y-%m-%dT%H:%M:%S", None),
        ("%Y-%m-%dT%H%M", None),
        ("%Y-%m-%dT%H%M%S", None),
    ]
    
    # Extract timezone from the string
    tz = default_tz
    tz_matched = False
    
    # Check for timezone indicators
    if 'MYT' in ts_str:
        tz = MYT
        tz_matched = True
        ts_str_clean = ts_str.replace('MYT', '').strip()
    elif 'UTC' in ts_str:
        tz = UTC
        tz_matched = True
        ts_str_clean = ts_str.replace('UTC', '').strip()
    elif '+08' in ts_str:
        tz = MYT
        tz_matched = True
        ts_str_clean = ts_str.replace('+08', '').strip()
    elif '+0800' in ts_str:
        tz = MYT
        tz_matched = True
        ts_str_clean = ts_str.replace('+0800', '').strip()
    elif 'Z' in ts_str and ts_str.rstrip().endswith('Z'):
        tz = UTC
        tz_matched = True
        ts_str_clean = ts_str.rstrip()[:-1].strip()
    else:
        ts_str_clean = ts_str
    
    # Remove trailing parentheses content like "(09:12 MYT)" 
    ts_str_clean = re.sub(r'\(.*?\)', '', ts_str_clean).strip()
    # Remove trailing annotations like "(6-hourly)" or "(11:33 MYT)"
    ts_str_clean = re.sub(r'\s*\(.*?\)\s*$', '', ts_str_clean).strip()
    
    for fmt, _ in formats:
        try:
            dt = datetime.strptime(ts_str_clean, fmt)
            dt = dt.replace(tzinfo=tz)
            return dt
        except ValueError:
            continue
    
    # Try ISO format with timezone
    try:
        # Handle formats like 2026-07-20T11:23:44+08:00
        dt = datetime.fromisoformat(ts_str)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=tz)
        return dt
    except ValueError:
        pass
    
    return None


def extract_generated_timestamp(content):
    """Extract the 'Generated:' timestamp from file content."""
    # Look for **Generated:** 2026-07-20 20:30 MYT
    # Also handle **Generated:** 2026-07-20 04:00 UTC
    # Also handle **Run:** 2026-07-14 07:10 UTC (for monitoring briefs)
    
    patterns = [
        r'\*\*Generated:\*\*\s*(.+?)(?:\n|$)',
        r'\*\*Run:\*\*\s*(.+?)(?:\n|\||$)',
        r'\*\*Collection Cycle:\*\*\s*(.+?)(?:\n|\(|$)',
        r'## Monitor Cycle:\s*(.+?)(?:\n|$)',
        r'\*\*Monitor Cycle:\*\*\s*(.+?)(?:\n|$)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, content[:3000], re.MULTILINE)
        if match:
            raw_ts = match.group(1).strip()
            # Clean up: remove trailing pipe-separated fields
            if '|' in raw_ts:
                raw_ts = raw_ts.split('|')[0].strip()
            # Remove trailing "  " (markdown line break)
            raw_ts = raw_ts.rstrip(' ').rstrip('  ')
            
            dt = parse_timestamp_str(raw_ts)
            if dt:
                return dt, raw_ts
    
    return None, None


def extract_brief_id_timestamp(content):
    """Extract timestamp from 'Brief ID:' field."""
    # Look for **Brief ID:** PRN-NS-NOMINATION-20260720-2030
    match = re.search(r'\*\*Brief ID:\*\*\s*(\S+)', content[:3000])
    if match:
        brief_id = match.group(1).strip()
        # Extract YYYYMMDD-HHMM pattern
        ts_match = re.search(r'(\d{4})(\d{2})(\d{2})-(\d{2})(\d{2})', brief_id)
        if ts_match:
            year, month, day, hour, minute = ts_match.groups()
            try:
                dt = datetime(int(year), int(month), int(day), int(hour), int(minute), tzinfo=MYT)
                return dt, brief_id
            except ValueError:
                pass
    return None, None


def extract_filename_timestamp(filepath):
    """Extract timestamp from filename (YYYYMMDD-HHMM pattern)."""
    filename = os.path.basename(filepath)
    
    # Pattern 1: YYYYMMDD-HHMM (e.g., PRN-NS-NOMINATION-20260720-2030.md)
    match = re.search(r'(\d{4})(\d{2})(\d{2})-(\d{2})(\d{2})', filename)
    if match:
        year, month, day, hour, minute = match.groups()
        try:
            dt = datetime(int(year), int(month), int(day), int(hour), int(minute), tzinfo=MYT)
            return dt, f"{year}{month}{day}-{hour}{minute}"
        except ValueError:
            pass
    
    # Pattern 2: YYYY-MM-DD-HHMM (e.g., policing-intel-2026-07-20-0629.md)
    match = re.search(r'(\d{4})-(\d{2})-(\d{2})-(\d{2})(\d{2})', filename)
    if match:
        year, month, day, hour, minute = match.groups()
        try:
            dt = datetime(int(year), int(month), int(day), int(hour), int(minute), tzinfo=MYT)
            return dt, f"{year}-{month}-{day}-{hour}{minute}"
        except ValueError:
            pass
    
    # Pattern 3: YYYY-MM-DDTHHMMSS+08 (e.g., 2026-07-20T112344+08-daily-report.md)
    match = re.search(r'(\d{4})-(\d{2})-(\d{2})T(\d{2})(\d{2})(\d{2})\+08', filename)
    if match:
        year, month, day, hour, minute, second = match.groups()
        try:
            dt = datetime(int(year), int(month), int(day), int(hour), int(minute), int(second), tzinfo=MYT)
            return dt, f"{year}-{month}-{day}T{hour}{minute}{second}+08"
        except ValueError:
            pass
    
    # Pattern 4: YYYY-MM-DDTHHMMSSZ (e.g., 2026-07-20T033300Z-daily-report.md)
    match = re.search(r'(\d{4})-(\d{2})-(\d{2})T(\d{2})(\d{2})(\d{2})Z', filename)
    if match:
        year, month, day, hour, minute, second = match.groups()
        try:
            dt = datetime(int(year), int(month), int(day), int(hour), int(minute), int(second), tzinfo=UTC)
            return dt, f"{year}-{month}-{day}T{hour}{minute}{second}Z"
        except ValueError:
            pass
    
    # Pattern 5: YYYY-MM-DDTHHMM+08 (shorter form)
    match = re.search(r'(\d{4})-(\d{2})-(\d{2})T(\d{2})(\d{2})\+08', filename)
    if match:
        year, month, day, hour, minute = match.groups()
        try:
            dt = datetime(int(year), int(month), int(day), int(hour), int(minute), tzinfo=MYT)
            return dt, f"{year}-{month}-{day}T{hour}{minute}+08"
        except ValueError:
            pass
    
    # Pattern 6: monitoring-brief-YYYYMMDD-HHMM.md
    match = re.search(r'(\d{4})(\d{2})(\d{2})-(\d{2})(\d{2})', filename)
    if match:
        year, month, day, hour, minute = match.groups()
        try:
            dt = datetime(int(year), int(month), int(day), int(hour), int(minute), tzinfo=MYT)
            return dt, f"{year}{month}{day}-{hour}{minute}"
        except ValueError:
            pass
    
    return None, None


def find_md_files():
    """Find all relevant .md files in the workspace directories."""
    md_files = []
    
    for ws_dir in WORKSPACE_DIRS:
        if not os.path.exists(ws_dir):
            continue
        for root, dirs, files in os.walk(ws_dir):
            # Skip unwanted directories
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not any(p in d.lower() for p in SKIP_PATTERNS)]
            
            for f in files:
                if f.endswith('.md'):
                    filepath = os.path.join(root, f)
                    if not should_skip(filepath):
                        md_files.append(filepath)
    
    return sorted(md_files)


def main():
    md_files = find_md_files()
    print(f"Found {len(md_files)} markdown files to scan")
    
    results = []
    files_with_generated = 0
    files_with_brief_id = 0
    files_with_filename_ts = 0
    
    for filepath in md_files:
        try:
            with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read(5000)  # Read first 5000 chars
        except Exception as e:
            continue
        
        # Get actual file creation time
        birth_dt, time_source = get_birth_time(filepath)
        if birth_dt is None:
            continue
        
        # Convert to MYT
        actual_myt = birth_dt.astimezone(MYT)
        
        # Extract 'Generated:' timestamp
        gen_dt, gen_raw = extract_generated_timestamp(content)
        
        # Extract 'Brief ID:' timestamp
        brief_dt, brief_raw = extract_brief_id_timestamp(content)
        
        # Extract filename timestamp
        fn_dt, fn_raw = extract_filename_timestamp(filepath)
        
        if gen_dt:
            files_with_generated += 1
        if brief_dt:
            files_with_brief_id += 1
        if fn_dt:
            files_with_filename_ts += 1
        
        # Compare 'Generated:' timestamp with actual creation time
        if gen_dt:
            gen_myt = gen_dt.astimezone(MYT)
            diff_seconds = abs((gen_myt - actual_myt).total_seconds())
            diff_minutes = diff_seconds / 60.0
            
            if diff_minutes > THRESHOLD_MINUTES:
                results.append({
                    "file": filepath,
                    "check_type": "Generated vs actual",
                    "embedded_timestamp": gen_myt.strftime("%Y-%m-%d %H:%M %Z"),
                    "embedded_raw": gen_raw,
                    "actual_creation_time_myt": actual_myt.strftime("%Y-%m-%d %H:%M:%S MYT"),
                    "time_source": time_source,
                    "difference_minutes": round(diff_minutes, 1)
                })
        
        # Compare 'Brief ID:' timestamp with actual creation time
        if brief_dt:
            brief_myt = brief_dt.astimezone(MYT)
            diff_seconds = abs((brief_myt - actual_myt).total_seconds())
            diff_minutes = diff_seconds / 60.0
            
            if diff_minutes > THRESHOLD_MINUTES:
                results.append({
                    "file": filepath,
                    "check_type": "Brief ID vs actual",
                    "embedded_timestamp": brief_myt.strftime("%Y-%m-%d %H:%M %Z"),
                    "embedded_raw": brief_raw,
                    "actual_creation_time_myt": actual_myt.strftime("%Y-%m-%d %H:%M:%S MYT"),
                    "time_source": time_source,
                    "difference_minutes": round(diff_minutes, 1)
                })
        
        # Compare filename timestamp with actual creation time
        # Try both MYT and UTC interpretations for filename timestamps
        if fn_dt:
            # Interpretation 1: filename timestamp is in MYT
            fn_as_myt = fn_dt  # already MYT
            diff_myt = abs((fn_as_myt - actual_myt).total_seconds()) / 60.0
            
            # Interpretation 2: filename timestamp was actually in UTC
            fn_as_utc = fn_dt.replace(tzinfo=UTC)
            fn_as_utc_in_myt = fn_as_utc.astimezone(MYT)
            diff_utc = abs((fn_as_utc_in_myt - actual_myt).total_seconds()) / 60.0
            
            # Use the smaller difference (best interpretation)
            if diff_myt <= diff_utc:
                diff_minutes = diff_myt
                fn_final = fn_as_myt
                tz_note = "MYT"
            else:
                diff_minutes = diff_utc
                fn_final = fn_as_utc_in_myt
                tz_note = "UTC (filename timestamp was actually UTC, not MYT)"
            
            if diff_minutes > THRESHOLD_MINUTES:
                results.append({
                    "file": filepath,
                    "check_type": "Filename vs actual",
                    "embedded_timestamp": fn_final.strftime("%Y-%m-%d %H:%M %Z"),
                    "embedded_raw": f"{fn_raw} (interpreted as {tz_note})",
                    "actual_creation_time_myt": actual_myt.strftime("%Y-%m-%d %H:%M:%S MYT"),
                    "time_source": time_source,
                    "difference_minutes": round(diff_minutes, 1)
                })
        
        # Also check Brief ID vs Generated consistency
        if gen_dt and brief_dt:
            gen_myt = gen_dt.astimezone(MYT)
            brief_myt = brief_dt.astimezone(MYT)
            diff_seconds = abs((gen_myt - brief_myt).total_seconds())
            diff_minutes = diff_seconds / 60.0
            
            if diff_minutes > THRESHOLD_MINUTES:
                results.append({
                    "file": filepath,
                    "check_type": "Generated vs Brief ID",
                    "embedded_timestamp": gen_myt.strftime("%Y-%m-%d %H:%M %Z"),
                    "embedded_raw": f"Generated: {gen_raw} | Brief ID: {brief_raw}",
                    "actual_creation_time_myt": brief_myt.strftime("%Y-%m-%d %H:%M:%S MYT"),
                    "time_source": "Brief ID timestamp (for comparison)",
                    "difference_minutes": round(diff_minutes, 1)
                })
        
        # Also check Generated vs Filename consistency
        if gen_dt and fn_dt:
            gen_myt = gen_dt.astimezone(MYT)
            fn_myt = fn_dt.astimezone(MYT)
            diff_seconds = abs((gen_myt - fn_myt).total_seconds())
            diff_minutes = diff_seconds / 60.0
            
            if diff_minutes > THRESHOLD_MINUTES:
                results.append({
                    "file": filepath,
                    "check_type": "Generated vs Filename",
                    "embedded_timestamp": gen_myt.strftime("%Y-%m-%d %H:%M %Z"),
                    "embedded_raw": f"Generated: {gen_raw} | Filename: {fn_raw}",
                    "actual_creation_time_myt": fn_myt.strftime("%Y-%m-%d %H:%M:%S MYT"),
                    "time_source": "Filename timestamp (for comparison)",
                    "difference_minutes": round(diff_minutes, 1)
                })
    
    # Summary
    print(f"\nSummary:")
    print(f"  Total .md files scanned: {len(md_files)}")
    print(f"  Files with 'Generated:'/'Run:'/'Collection Cycle:' timestamp: {files_with_generated}")
    print(f"  Files with 'Brief ID:' timestamp: {files_with_brief_id}")
    print(f"  Files with filename timestamp: {files_with_filename_ts}")
    print(f"  Mismatches found (> {THRESHOLD_MINUTES} min): {len(results)}")
    
    # Output JSON
    output = {
        "summary": {
            "total_md_files_scanned": len(md_files),
            "files_with_generated_timestamp": files_with_generated,
            "files_with_brief_id_timestamp": files_with_brief_id,
            "files_with_filename_timestamp": files_with_filename_ts,
            "threshold_minutes": THRESHOLD_MINUTES,
            "mismatches_found": len(results)
        },
        "mismatches": results
    }
    
    output_path = os.path.join(BASE, "workspace-ns", "timestamp_mismatch_report.json")
    with open(output_path, 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"\nReport written to: {output_path}")
    
    # Also print the JSON for immediate viewing
    print("\n" + "="*80)
    print("JSON OUTPUT:")
    print("="*80)
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
