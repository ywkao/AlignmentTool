#!/usr/bin/env python2
import glob

# you can design to select golden runs, https://twiki.cern.ch/twiki/bin/viewauth/CMS/CertificationOfCollisions22
keys_golden_runs = []

# load list of files
contents = []
for txt in glob.glob("new*txt"):
    fin = open(txt, 'r')
    lines = fin.readlines()
    contents += lines
    fin.close()

# sort and output a list
output = "list_sorted_runs.txt"
with open(output, 'w') as fout:
    contents.sort()
    for line in contents:
        line.strip()
        fout.write(line)
