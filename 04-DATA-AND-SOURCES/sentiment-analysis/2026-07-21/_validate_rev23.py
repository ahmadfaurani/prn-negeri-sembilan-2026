import json, os
base = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/sentiment-analysis/2026-07-21"
jf = os.path.join(base, "sentiment-20260721-0022.json")
sf = os.path.join(base, "summary.md")
with open(jf) as f:
    d = json.load(f)
print("JSON OK. report_id:", d["metadata"]["report_id"])
print("revision:", d["metadata"]["revision"], "prev:", d["metadata"]["previous_revision"])
print("total_entity_count:", d["metadata"]["total_entity_count"], "critical:", d["metadata"]["critical_count"], "priority:", d["metadata"]["priority_count"], "none:", d["metadata"]["none_count"])
print("new_entities:", len(d["new_entities"]), "updated_entities:", len(d["updated_entities"]))
# verify required fields per mission format on each entity
req = {"entity","pir_tag","sentiment","score","trend","alert","source_count"}
missing = []
for grp in ("new_entities","updated_entities"):
    for e in d[grp]:
        m = req - set(e.keys())
        if m: missing.append((grp, e.get("entity"), m))
print("missing required fields:", missing if missing else "NONE")
# score range check
bad = [(e.get("entity"), e["score"]) for grp in ("new_entities","updated_entities") for e in d[grp] if not (-1.0 <= e["score"] <= 1.0)]
print("out-of-range scores:", bad if bad else "NONE")
print("summary.md exists:", os.path.exists(sf), "size:", os.path.getsize(sf))
print("json size:", os.path.getsize(jf))
