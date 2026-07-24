#!/bin/bash
# Workstream: PRN Negeri Sembilan 2026 Git Sync
# Repo: prn-negeri-sembilan-2026 (HCR-095)
# Runs after: Campaign Period pipeline — Collection (06:00/18:00 MYT), Campaign Trail (09:00/15:00/23:00 MYT), Entity (08:00 MYT), Sentiment (10:00 MYT), Brief (12:00/21:00 MYT)
# Updated: 2026-07-24 — Unified workspace integration: added Campaign Trail Tracker (10d9c6242b4e) to config export. 6 NS cronjobs total.

set -e
WORKDIR="/home/p62operator/.openclaw/workspace-ns"
cd "$WORKDIR"

# STEP 1: Export cronjob configurations from Hermes internal state
python3 -c "
import json
try:
    with open('/home/p62operator/.hermes/cron/jobs.json') as f:
        data = json.load(f)
    jobs = data['jobs']
    ns_ids = ['bf8a4c1fb881', '3c9e6756876a', '02e588724145', 'b8f69d6f990d', '2df980e8e094', '10d9c6242b4e']
    ns_jobs = [j for j in jobs if j.get('id') in ns_ids]
    export = {
        'workstream': 'PRN Negeri Sembilan 2026 (HCR-095)',
        'exported_at': __import__('datetime').datetime.utcnow().isoformat() + 'Z',
        'repo': 'ahmadfaurani/prn-negeri-sembilan-2026',
        'workspace': '/home/p62operator/.openclaw/workspace-ns',
        'total_cronjobs': len(ns_jobs),
        'cronjobs': []
    }
    for j in ns_jobs:
        m = j.get('model')
        model_name = m.get('model') if isinstance(m, dict) else None
        provider = m.get('provider') if isinstance(m, dict) else None
        sched = j.get('schedule', {})
        sched_display = sched.get('display', '?') if isinstance(sched, dict) else str(sched)
        export['cronjobs'].append({
            'id': j['id'],
            'name': j['name'],
            'schedule': sched_display,
            'deliver': j.get('deliver', '?'),
            'model': model_name or 'inherit (default)',
            'provider': provider or j.get('provider', 'inherit'),
            'enabled_toolsets': j.get('enabled_toolsets', 'all'),
            'workdir': j.get('workdir', 'default'),
            'enabled': j.get('enabled', True),
            'prompt': j.get('prompt', '')
        })
    with open('/home/p62operator/.openclaw/workspace-ns/05-TOOLS-AND-AUTOMATION/cronjob-configs.json', 'w') as f:
        json.dump(export, f, indent=2, ensure_ascii=False)
    print(f'Exported {len(ns_jobs)} cronjob configs')
except Exception as e:
    print(f'Config export skipped: {e}')
"

# STEP 2: Git sync
TIMESTAMP=$(date -u +%Y-%m-%dT%H:%M:%SZ)
CHANGES=$(git status --porcelain | wc -l)

if [ "$CHANGES" -gt 0 ]; then
    git add -A
    git reset 04-DATA-AND-SOURCES/scratch/ 2>/dev/null
    git commit -m "auto: prn-negeri-sembilan git-sync $TIMESTAMP"
    git push origin main 2>&1 && echo "✅ Pushed $CHANGES files to prn-negeri-sembilan-2026 (HCR-095)" || echo "⚠️ Committed locally, push deferred (auth pending)"
else
    echo "No changes to sync — prn-negeri-sembilan-2026 (HCR-095)"
fi
