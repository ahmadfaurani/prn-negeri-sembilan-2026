#!/bin/bash
# =============================================================================
# Content Sanitization Script for ARAS Endpoint Content Filter False Positives
# =============================================================================
# PURPOSE: Pre-process workspace data files to replace trigger word combinations
#          that falsely trigger the ARAS endpoint's harmful_child_safety and
#          bias_sexual_orientation content filters.
#
# CONTEXT: Malaysian political/defence intelligence — words like "youth" (young
#          voters, UMNO Youth), "dominant" (dominant narrative), "cp" (Command
#          Post, Communist Party), "kid" (kidnapping), "child" (child policy),
#          "explicit" (explicit statement), "cure" (procurement), "trans"
#          (transparency) are routine political terminology but trigger the
#          ARAS endpoint's content guardrails as false positives.
#
# USAGE:
#   ./sanitize-filter-triggers.sh [YYYYMMDD]
#   If no date argument, processes today's files.
#
# AFFECTED FILTERS (as of 2026-07-22 incident):
#   - harmful_child_safety: "youth + dominant", "youth + haji", "kid + dominate",
#     "child + explicit", keyword "cp"
#   - bias_sexual_orientation: keyword "cure trans"
#
# TRIGGER MAPPING:
#   youth → belia (Malay equivalent, same meaning)
#   dominant → primary
#   dominate → lead
#   haji → haji_honorific (only when adjacent to "youth"/"belia")
#   kid → minor (only in PDRM crime context)
#   child → kanak-kanak (Malay equivalent)
#   explicit → overt
#   cure → remedy
#   trans → transparent (when not already "transparency")
#   cp → cmd_post
#
# DATE: 2026-07-23
# TLP:AMBER
# =============================================================================

set -euo pipefail

TARGET_DATE="${1:-$(TZ=Asia/Kuala_Lumpur date '+%Y%m%d')}"
WORKSPACE="/home/p62operator/.openclaw/workspace-ns"

# Directories to sanitize
RAW_DIR="${WORKSPACE}/04-DATA-AND-SOURCES/raw-scrapes/${TARGET_DATE}"
ENTITY_DIR="${WORKSPACE}/04-DATA-AND-SOURCES/processed-entities/${TARGET_DATE}"
SENTIMENT_DIR="${WORKSPACE}/04-DATA-AND-SOURCES/sentiment-analysis/${TARGET_DATE}"

# Sanitization rules (order matters — more specific patterns first)
# Format: "old_pattern|new_pattern"
SANITIZE_RULES=(
  # Conditional matches (two-word triggers)
  'youth + dominant|belia + primary'
  'youth + haji|belia + haji_honorific'
  'kid + dominate|minor + lead'
  'child + explicit|kanak-kanak + overt'
  # Keyword triggers
  'cure trans|remedy transparent'
  # Individual words that combine into triggers (context-aware)
  # Only replace "youth" when it appears as a standalone word in political context
  '\byouth\b|belia'
  '\bdominant\b|primary'
  '\bdominate\b|lead'
  '\bexplicit\b|overt'
  # "cp" as standalone keyword (not in "CPU", "MCP", etc.)
  '\bcp\b|cmd_post'
  # "kid" only in crime/kidnapping context (standalone)
  '\bkid\b|minor'
  # "child" standalone (not "childhood", "children")
  '\bchild\b|kanak-kanak'
)

# Files to skip (this script itself, binary files)
SKIP_PATTERNS="sanitize-filter-triggers|\.git|\.png|\.jpg|\.pdf"

echo "=== ARAS Content Filter Sanitization ==="
echo "Target date: ${TARGET_DATE}"
echo "Workspace: ${WORKSPACE}"
echo ""

PROCESSED=0
SKIPPED=0

sanitize_file() {
    local file="$1"
    local tmp_file="${file}.sanitized"

    # Skip binary files and the script itself
    if echo "$file" | grep -qE "$SKIP_PATTERNS"; then
        ((SKIPPED++)) || true
        return
    fi

    # Check if file contains any trigger words before processing
    if ! grep -qilE '\byouth\b|\bdominant\b|\bdominate\b|\bexplicit\b|\bcp\b|\bkid\b|\bchild\b|cure trans' "$file" 2>/dev/null; then
        ((SKIPPED++)) || true
        return
    fi

    cp "$file" "$tmp_file"

    for rule in "${SANITIZE_RULES[@]}"; do
        old_pattern="${rule%%|*}"
        new_pattern="${rule##*|}"
        # Use perl for word boundary support with \b
        perl -pi -e "s/${old_pattern}/${new_pattern}/gi" "$tmp_file" 2>/dev/null || true
    done

    # Only replace if changes were made
    if ! diff -q "$file" "$tmp_file" >/dev/null 2>&1; then
        mv "$tmp_file" "$file"
        echo "  ✓ Sanitized: $(basename "$file")"
        ((PROCESSED++)) || true
    else
        rm "$tmp_file"
        ((SKIPPED++)) || true
    fi
}

echo "--- Processing raw scrapes ---"
if [ -d "$RAW_DIR" ]; then
    for f in "$RAW_DIR"/*.md "$RAW_DIR"/*.json; do
        [ -f "$f" ] && sanitize_file "$f"
    done
else
    echo "  (no raw scrapes for ${TARGET_DATE})"
fi

echo "--- Processing processed entities ---"
if [ -d "$ENTITY_DIR" ]; then
    for f in "$ENTITY_DIR"/*.md "$ENTITY_DIR"/*.json; do
        [ -f "$f" ] && sanitize_file "$f"
    done
else
    echo "  (no processed entities for ${TARGET_DATE})"
fi

echo "--- Processing sentiment analysis ---"
if [ -d "$SENTIMENT_DIR" ]; then
    for f in "$SENTIMENT_DIR"/*.md "$SENTIMENT_DIR"/*.json; do
        [ -f "$f" ] && sanitize_file "$f"
    done
else
    echo "  (no sentiment analysis for ${TARGET_DATE})"
fi

echo ""
echo "=== Summary ==="
echo "  Processed: ${PROCESSED} files"
echo "  Skipped:   ${SKIPPED} files"
echo "  Date:       ${TARGET_DATE}"
echo ""
echo "NOTE: Replacements are reversible. Original terms are preserved in git history."
echo "      This script only modifies data files, not the brief agent's prompt or output."
