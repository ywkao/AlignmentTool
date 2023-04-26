#!/usr/bin/env python2
import json

output = "inputFiles.json"
mytxt = "list_sorted_runs.txt"

# load
fin = open(mytxt, 'r')
content = fin.readlines()
fin.close()

# store
FileNames = {}
for i, line in enumerate(content):
    key = "batch0%d" % (i+1) if i<9 else "batch%d" % (i+1)
    FileNames[key] = [line.strip()]

# write
with open(output, 'w') as f:
    json.dump(FileNames, f, sort_keys=True, indent=4)
    f.write("\n")

