from pytablewriter import MarkdownTableWriter
import json

writer = MarkdownTableWriter()
writer.table_name = "Intent Cross-Validation Results (5 folds)"

with open('results/intent_report.json', 'r') as f:
    data = json.loads(f.read())
writer.headers = ["class"] + list(data['micro avg'].keys())

classes = list(data.keys())
classes.sort(key = lambda x: data[x]['support'], reverse=True)

writer.value_matrix = [
    [c] + [data[c][k] for k in data[c].keys()]
    for c in classes
]

writer.dump('results.md')
