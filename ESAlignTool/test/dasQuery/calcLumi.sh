#!/bin/bash
# reference-01: https://github.com/piedraj/instructions/blob/master/BRILCALC.md
# reference-02: http://opendata.cern.ch/docs/cms-guide-luminosity-calculation

#export PATH=$HOME/.local/bin:/afs/cern.ch/cms/lumi/brilconda-1.1.7/bin:$PATH

brilcalc --version

#brilcalc lumi -u /pb -c web --begin 355374 --end 355455 -i Cert_Collisions2022_355100_357900_Golden.json > Run2022B_lumi.txt
#brilcalc lumi -u /pb -c web --begin 355374 --end 355679 -i Cert_Collisions2022_355100_357900_Golden.json > Run2022B_lumi.txt
brilcalc lumi -u /pb -c web --begin 355374 --end 355456 -i Cert_Collisions2022_355100_357900_Golden.json > Run2022B_lumi.txt

./reportLumi.py
