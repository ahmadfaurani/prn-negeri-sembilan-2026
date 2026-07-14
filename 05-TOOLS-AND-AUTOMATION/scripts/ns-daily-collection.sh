#!/bin/bash
# Negeri Sembilan PRN 2026 - Daily News Collection Script
# Workspace: /home/p62operator/.openclaw/workspace-ns/
# Classification: TLP:AMBER

set -e

WORKSPACE="/home/p62operator/.openclaw/workspace-ns"
RAW_DIR="${WORKSPACE}/04-DATA-AND-SOURCES/raw-scrapes"
DATE_STAMP=$(date +%Y%m%d)
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

echo "=== Negeri Sembilan PRN 2026 - Daily Collection ==="
echo "Date: ${DATE_STAMP}"
echo "Timestamp: ${TIMESTAMP}"
echo ""

# Create date-stamped directory
mkdir -p "${RAW_DIR}/${DATE_STAMP}"

# Negeri Sembilan News Sources (13 priority sources)
declare -a SOURCES=(
    "https://www.sinarharian.com.my/negeri-sembilan"
    "https://www.bharian.com.my/sembilan"
    "https://www.utusan.com.my/negeri/2026/07/negeri-sembilan/"
    "https://www.nst.com.my/news/nation"
    "https://www.thestar.com.my/news/nation"
    "https://www.malaysiakini.com/news/my"
    "https://www.freemalaysiatoday.com/category/nation/"
    "https://bernamahub.com/category/nasional/"
    "https://www.astroawani.com/berita-nasional"
    "https://www.ohbulan.com/tag/negeri-sembilan/"
    "https://www.mstar.com.my/lokal/sembilan"
    "https://www.metro.com.my/berita/nasional"
    "https://www.kosmo.com.my/berita/nasional/"
)

# Firecrawl API endpoint (v2)
FIRECRAWL_API="http://localhost:3002/v2/scrape"

SUCCESS_COUNT=0
TIMEOUT_COUNT=0
ERROR_COUNT=0

echo "Collecting from ${#SOURCES[@]} sources..."
echo ""

for SOURCE in "${SOURCES[@]}"; do
    SOURCE_NAME=$(echo "$SOURCE" | sed 's|https://www.||; s|https://||; s|/.*||; s|\.||g')
    OUTPUT_FILE="${RAW_DIR}/${DATE_STAMP}/${SOURCE_NAME}_${TIMESTAMP}.md"
    
    echo "→ ${SOURCE_NAME}..."
    
    # Use Firecrawl v2 API
    RESPONSE=$(curl -s -X POST "${FIRECRAWL_API}" \
        -H "Content-Type: application/json" \
        -d "{
            \"url\": \"${SOURCE}\",
            \"onlyMainContent\": true,
            \"formats\": [\"markdown\"],
            \"timeout\": 30000
        }" 2>&1) || {
        echo "  ✗ CURL failed"
        TIMEOUT_COUNT=$((TIMEOUT_COUNT+1))
        continue
    }
    
    # Check if response contains markdown content (v2 API structure)
    if echo "$RESPONSE" | jq -e '.data.markdown' >/dev/null 2>&1; then
        echo "$RESPONSE" | jq -r '.data.markdown' > "${OUTPUT_FILE}" 2>/dev/null || {
            echo "  ✗ Failed to extract markdown"
            ERROR_COUNT=$((ERROR_COUNT+1))
            continue
        }
        
        WORD_COUNT=$(wc -w < "${OUTPUT_FILE}")
        if [ "$WORD_COUNT" -gt 50 ]; then
            echo "  ✓ Success (${WORD_COUNT} words)"
            SUCCESS_COUNT=$((SUCCESS_COUNT+1))
        else
            echo "  ✗ Content too thin (${WORD_COUNT} words)"
            ERROR_COUNT=$((ERROR_COUNT+1))
            rm -f "${OUTPUT_FILE}"
        fi
    else
        echo "  ✗ No markdown in response"
        ERROR_COUNT=$((ERROR_COUNT+1))
    fi
done

echo ""
echo "=== Collection Summary ==="
echo "Successful: ${SUCCESS_COUNT}/${#SOURCES[@]}"
echo "Timeouts: ${TIMEOUT_COUNT}"
echo "Errors: ${ERROR_COUNT}"
echo ""

# Write collection metadata
cat > "${RAW_DIR}/${DATE_STAMP}/collection_metadata.json" << EOF
{
    "date": "${DATE_STAMP}",
    "timestamp": "${TIMESTAMP}",
    "workspace": "${WORKSPACE}",
    "sources_attempted": ${#SOURCES[@]},
    "successful": ${SUCCESS_COUNT},
    "timeouts": ${TIMEOUT_COUNT},
    "errors": ${ERROR_COUNT},
    "success_rate": "$(echo "scale=1; ${SUCCESS_COUNT}*100/${#SOURCES[@]}" | bc)%"
}
EOF

echo "Metadata written to: ${RAW_DIR}/${DATE_STAMP}/collection_metadata.json"
echo ""

# Exit with appropriate code
if [ ${SUCCESS_COUNT} -ge 5 ]; then
    echo "✓ Collection completed successfully"
    exit 0
else
    echo "⚠ Collection degraded (${SUCCESS_COUNT}/${#SOURCES[@]})"
    exit 1
fi
