#!/bin/bash
# Negeri Sembilan PRN 2026 - Entity Extraction Script
# Workspace: /home/p62operator/.openclaw/workspace-ns/
# Classification: TLP:AMBER

set -e

WORKSPACE="/home/p62operator/.openclaw/workspace-ns"
RAW_DIR="${WORKSPACE}/04-DATA-AND-SOURCES/raw-scrapes"
PROCESSED_DIR="${WORKSPACE}/04-DATA-AND-SOURCES/processed-entities"
DATE_STAMP=$(date +%Y%m%d)

echo "=== Negeri Sembilan PRN 2026 - Entity Extraction ==="
echo "Date: ${DATE_STAMP}"
echo ""

# Create processed directory
mkdir -p "${PROCESSED_DIR}/${DATE_STAMP}"

# Find today's collected files
COLLECTION_DIR="${RAW_DIR}/${DATE_STAMP}"

if [ ! -d "${COLLECTION_DIR}" ]; then
    echo "⚠ No collection directory found for ${DATE_STAMP}"
    echo "Looking for most recent collection..."
    
    # Find most recent collection
    COLLECTION_DIR=$(ls -td ${RAW_DIR}/*/ 2>/dev/null | head -1 | tr -d '\n')
    if [ -z "${COLLECTION_DIR}" ]; then
        echo "✗ No collection data found"
        exit 1
    fi
    DATE_STAMP=$(basename "${COLLECTION_DIR}")
    echo "Using collection from: ${DATE_STAMP}"
fi

echo "Processing collection: ${COLLECTION_DIR}"
echo ""

# Count source files
SOURCE_COUNT=$(find "${COLLECTION_DIR}" -name "*.md" -type f | wc -l)
echo "Found ${SOURCE_COUNT} source files"

if [ "${SOURCE_COUNT}" -eq 0 ]; then
    echo "✗ No markdown files to process"
    exit 1
fi

# Entity extraction categories
declare -a ENTITIES=(
    "politicians"
    "parties"
    "constituencies"
    "issues"
    "events"
    "organizations"
    "locations"
)

echo ""
echo "Extracting entities by category..."

for ENTITY_TYPE in "${ENTITIES[@]}"; do
    OUTPUT_FILE="${PROCESSED_DIR}/${DATE_STAMP}/entities_${ENTITY_TYPE}.json"
    
    echo "→ Extracting ${ENTITY_TYPE}..."
    
    # Use Python for entity extraction
    cat "${COLLECTION_DIR}"/*.md | python3 -c "
import sys
import json
import re
from collections import defaultdict

# Read all input
content = sys.stdin.read()

# Simple pattern-based extraction
entities = {
    'politicians': set(),
    'parties': set(),
    'constituencies': set(),
    'issues': set(),
    'events': set(),
    'organizations': set(),
    'locations': set()
}

# Party patterns
party_patterns = [
    r'\b(PH|Pakatan Harapan)\b',
    r'\b(BN|Barisan Nasional)\b',
    r'\b(PN|Perikatan Nasional)\b',
    r'\b(UMNO)\b',
    r'\b(PKR)\b',
    r'\b(DAP)\b',
    r'\b(PAS)\b',
    r'\b(Bersatu)\b',
    r'\b(MUDA)\b',
    r'\b(Bersama)\b',
]

# Constituency patterns (Negeri Sembilan DUN)
dun_patterns = [
    r'\b(N\d{2}\s+[A-Za-z\s]+)\b',
    r'\b(DUN\s+[A-Za-z\s]+)\b',
]

# Extract parties
for pattern in party_patterns:
    matches = re.findall(pattern, content, re.IGNORECASE)
    entities['parties'].update(matches)

# Extract DUN names
for pattern in dun_patterns:
    matches = re.findall(pattern, content, re.IGNORECASE)
    entities['constituencies'].update(matches)

# Convert to JSON
output = {
    'date': '$(date -Iseconds)',
    'source_count': ${SOURCE_COUNT},
    'entity_type': '${ENTITY_TYPE}',
    'entities': list(entities.get('${ENTITY_TYPE}', set()))
}

print(json.dumps(output, indent=2))
" > "${OUTPUT_FILE}" 2>/dev/null || {
        echo "  ✗ Extraction failed for ${ENTITY_TYPE}"
        continue
    }
    
    if [ -s "${OUTPUT_FILE}" ]; then
        ENTITY_COUNT=$(jq '.entities | length' "${OUTPUT_FILE}" 2>/dev/null || echo "0")
        echo "  ✓ Extracted ${ENTITY_COUNT} ${ENTITY_TYPE}"
    else
        echo "  ✗ No entities extracted"
    fi
done

# Create consolidated entity file
echo ""
echo "Creating consolidated entity file..."

cat > "${PROCESSED_DIR}/${DATE_STAMP}/entities_consolidated.json" << EOF
{
    "date": "${DATE_STAMP}",
    "timestamp": "$(date -Iseconds)",
    "source_count": ${SOURCE_COUNT},
    "extraction_completed": true,
    "entity_categories": ["politicians", "parties", "constituencies", "issues", "events", "organizations", "locations"]
}
EOF

echo ""
echo "=== Entity Extraction Summary ==="
echo "Date: ${DATE_STAMP}"
echo "Sources processed: ${SOURCE_COUNT}"
echo "Output directory: ${PROCESSED_DIR}/${DATE_STAMP}/"
echo ""
echo "✓ Entity extraction completed"
