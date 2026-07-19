#!/bin/bash
# Negeri Sembilan PRN 2026 - NOMINATION DAY SURGE Collection (PIR-aware)
# Workspace: /home/p62operator/.openclaw/workspace-ns/
# Classification: TLP:AMBER
# Covers 10 director-approved sources + PIR-06/09/07 tagging

WORKSPACE="/home/p62operator/.openclaw/workspace-ns"
RAW_DIR="${WORKSPACE}/04-DATA-AND-SOURCES/raw-scrapes"
DATE_STAMP=$(date +%Y%m%d)
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
OUT_DIR="${RAW_DIR}/${DATE_STAMP}"
mkdir -p "${OUT_DIR}"

FIRECRAWL_API="http://localhost:3002/v2/scrape"
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"

# 10 director-approved sources (name|url)
declare -a SOURCES=(
    "malaysiakinicom|https://www.malaysiakini.com/news/my"
    "thmalaysianinsightcom|https://www.themalaysianinsight.com/"
    "nstcommy|https://www.nst.com.my/news/nation"
    "thestarcommy|https://www.thestar.com.my/news/nation"
    "utusancommy|https://www.utusan.com.my/nasional/"
    "bhariancommy|https://www.bharian.com.my/sembilan"
    "kosmocommy|https://www.kosmo.com.my/berita/nasional/"
    "astroawanicom|https://www.astroawani.com/berita-nasional"
    "mstarcommy|https://www.mstar.com.my/lokal/sembilan"
    "ohbulancom|https://www.ohbulan.com/tag/negeri-sembilan/"
)

# PIR keyword regexes (case-insensitive)
PIR06='(pecat|termination|remove|keluar|withdraw|tarik diri|majlis tertinggi|asas kukuh|bersatu.*pn|pn.*bersatu|muhyiddin|samsuri|hadi|kiandee|hamzah)'
PIR09='(pecat|disiplin|lompat|pengkhianat|defector|hopper|kredibiliti|eligibility|bankrup|kes mahkamah|calon bebas|independent)'
PIR07='(kerusi tumpuan|battleground|pertembungan|marquee|pinggir|manifesto|kempen|operasi|calon|tempat mengundi|n\.14|n\.15|n\.28|n\.13|n\.32|n\.04|n\.33|n\.10|ampangan)'

SUCCESS_COUNT=0
ERROR_COUNT=0
declare -a META_ENTRIES=()

for ENTRY in "${SOURCES[@]}"; do
    NAME="${ENTRY%%|*}"
    URL="${ENTRY##*|}"
    OUTFILE="${OUT_DIR}/${NAME}_${TIMESTAMP}.md"
    echo "→ ${NAME} (${URL})"

    RESPONSE=$(curl -s --max-time 45 -X POST "${FIRECRAWL_API}" \
        -H "Content-Type: application/json" \
        -d "{\"url\":\"${URL}\",\"formats\":[\"markdown\"],\"onlyMainContent\":true,\"timeout\":40000}" 2>&1)

    MARKDOWN=$(echo "$RESPONSE" | jq -r '.data.markdown // empty' 2>/dev/null)

    if [ -z "$MARKDOWN" ]; then
        echo "  ✗ No markdown (Firecrawl fail); trying direct curl fallback"
        MARKDOWN=$(curl -sL --max-time 30 -A "${UA}" "${URL}" 2>/dev/null | \
            python3 -c "import sys,html,re; t=sys.stdin.read(); t=re.sub(r'<script.*?</script>','',t,flags=re.S); t=re.sub(r'<style.*?</style>','',t,flags=re.S); t=re.sub(r'<[^>]+>',' ',t); t=html.unescape(t); print(re.sub(r'\n\s*\n+','\n',t))" 2>/dev/null)
    fi

    WORD_COUNT=$(echo "$MARKDOWN" | wc -w)
    if [ "$WORD_COUNT" -lt 50 ]; then
        echo "  ✗ Content too thin (${WORD_COUNT} words)"
        ERROR_COUNT=$((ERROR_COUNT+1))
        META_ENTRIES+=("{\"source\":\"${NAME}\",\"url\":\"${URL}\",\"status\":\"error\",\"word_count\":${WORD_COUNT},\"priority_tags\":[]}")
        continue
    fi

    # PIR tagging - find headline-ish lines and tag
    PRIORITY_TAGGED=$(echo "$MARKDOWN" | awk -v RS='' '
        BEGIN { IGNORECASE=1 }
        {
            line=$0
            tag=""
            if (line ~ /pecat|termination|remove|keluar|withdraw|tarik diri|majlis tertinggi|asas kukuh|bersatu.*pn|pn.*bersatu|muhyiddin|samsuri|kiandee|hamzah/) tag=tag "PIR-06 "
            if (line ~ /pecat|disiplin|lompat|pengkhianat|defector|hopper|kredibiliti|eligibility|bankrup|kes mahkamah|calon bebas|independent/) tag=tag "PIR-09 "
            if (line ~ /kerusi tumpuan|battleground|pertembungan|marquee|pinggir|manifesto|kempen|operasi|calon|ampangan|n\.14|n\.15|n\.28|n\.13|n\.32|n\.04|n\.33|n\.10/) tag=tag "PIR-07 "
            if (tag != "") print "[PRIORITY " tag "] " line
            else print line
        }')

    echo "$PRIORITY_TAGGED" > "${OUTFILE}"

    # Count priority tags
    P06=$(grep -ciE "$PIR06" "${OUTFILE}" 2>/dev/null || echo 0)
    P09=$(grep -ciE "$PIR09" "${OUTFILE}" 2>/dev/null || echo 0)
    P07=$(grep -ciE "$PIR07" "${OUTFILE}" 2>/dev/null || echo 0)
    TAGS=""
    [ "$P06" -gt 0 ] && TAGS="${TAGS}PIR-06(${P06}) "
    [ "$P09" -gt 0 ] && TAGS="${TAGS}PIR-09(${P09}) "
    [ "$P07" -gt 0 ] && TAGS="${TAGS}PIR-07(${P07}) "
    TAGS="${TAGS% }"
    [ -z "$TAGS" ] && TAGS="none"

    echo "  ✓ ${WORD_COUNT} words | tags: ${TAGS}"
    SUCCESS_COUNT=$((SUCCESS_COUNT+1))
    META_ENTRIES+=("{\"source\":\"${NAME}\",\"url\":\"${URL}\",\"status\":\"ok\",\"word_count\":${WORD_COUNT},\"priority_tags\":\"${TAGS}\",\"file\":\"$(basename ${OUTFILE})\"}")
done

# Write metadata
META_FILE="${OUT_DIR}/collection_metadata.json"
python3 - <<PYEOF
import json, datetime
entries = [
$(printf '%s\n' "${META_ENTRIES[@]}" | sed 's/$/,/')
]
doc = {
    "date": "${DATE_STAMP}",
    "timestamp": "${TIMESTAMP}",
    "cycle": "nomination-day-surge",
    "workspace": "${WORKSPACE}",
    "sources_attempted": ${#SOURCES[@]},
    "successful": ${SUCCESS_COUNT},
    "errors": ${ERROR_COUNT},
    "success_rate": f"{${SUCCESS_COUNT}*100//${#SOURCES[@]}}%",
    "pir_priorities": {
        "PIR-06": "PN-Removal-of-Bersatu Watch (HIGHEST)",
        "PIR-09": "Candidate Credibility (SECOND)",
        "PIR-07": "Battleground Assessment (THIRD)"
    },
    "critical_pir06_alert": "pending-analysis",
    "sources": entries
}
with open("${META_FILE}","w") as f:
    json.dump(doc, f, indent=2, ensure_ascii=False)
print("Metadata written:", "${META_FILE}")
PYEOF

echo ""
echo "=== Surge Collection Summary ==="
echo "Successful: ${SUCCESS_COUNT}/${#SOURCES[@]}"
echo "Errors: ${ERROR_COUNT}"
echo "Timestamp: ${TIMESTAMP}"
