#!/usr/bin/env python2

txt = "Run2022B_lumi.txt"

integral = 0.
with open(txt, 'r') as fin:
    for line in fin.readlines():
        if "/22" in line:
            lumi = float( line.strip().split()[12] )
            integral += lumi
            print lumi

print "--------------------"
print integral
