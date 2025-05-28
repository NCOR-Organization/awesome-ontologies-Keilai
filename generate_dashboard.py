import os
from datetime import datetime

DUMP_DIR = "dump"
DASHBOARD_PATH = "dashboard.html"

# File extensions to include
ontology_extensions = [".owl", ".ttl", ".rdf", ".jsonld"]

# Scan /dump directory
ontology_files = [
    f for f in os.listdir(DUMP_DIR)
    if any(f.endswith(ext) for ext in ontology_extensions)
]

# HTML header
html = [
    "<!DOCTYPE html>",
    "<html>",
    "<head>",
    "<meta charset='utf-8'/>",
    "<title>Ontology Dashboard</title>",
    "<link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css' rel='stylesheet'>",
    "</head>",
    "<body class='p-4'>",
    "<div class='container'>",
    "<h1>🧠 Ontology Dashboard</h1>",
    f"<p>Showing {len(ontology_files)} ontology file(s) in <code>/dump</code></p>",
    "<table class='table table-striped table-hover'>",
    "<thead><tr><th>Filename</th><th>Format</th><th>Size</th><th>Last Modified</th></tr></thead>",
    "<tbody>"
]

# Populate table rows
for filename in sorted(ontology_files):
    filepath = os.path.join(DUMP_DIR, filename)
    size_kb = os.path.getsize(filepath) / 1024
    mtime = os.path.getmtime(filepath)
    modified = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M")
    ext = os.path.splitext(filename)[-1].lower().replace(".", "").upper()
    html.append(
        f"<tr><td><a href='{DUMP_DIR}/{filename}'>{filename}</a></td>"
        f"<td>{ext}</td>"
        f"<td>{size_kb:.1f} KB</td>"
        f"<td>{modified}</td></tr>"
    )

# HTML footer
html += [
    "</tbody>",
    "</table>",
    "<p><small>Last updated: " + datetime.now().strftime("%Y-%m-%d %H:%M") + "</small></p>",
    "</div></body></html>"
]

# Write to dashboard.html
with open(DASHBOARD_PATH, "w") as f:
    f.write("\n".join(html))

print(f"✅ Dashboard written to {DASHBOARD_PATH}")
