#!/usr/bin/env python
import glob
import subprocess

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--das" , help = "Run DAS query to list root files", action="store_true")
parser.add_argument("-s", "--sort", help = "Sort root files in the txt files", action="store_true")
parser.add_argument("-l", "--lumi", help = "Run DAS query to list luminosity", action="store_true")
args = parser.parse_args()

def exe(command):
    subprocess.call(command, shell=True)

def search_files():
    print ">>> start searching files through DAS..."

    # 2023 CMS DAS: https://cmsweb.cern.ch/das/request?view=list&limit=50&instance=prod%2Fglobal&input=dataset%3D%2FEGamma*%2FRun2023*EcalESAlign*%2FALCARECO
    datasets = [
        #"/EGamma0/Run2023A-EcalESAlign-PromptReco-v2/ALCARECO",
        #"/EGamma0/Run2023B-EcalESAlign-PromptReco-v1/ALCARECO",
        "/EGamma1/Run2023A-EcalESAlign-PromptReco-v2/ALCARECO",
        "/EGamma1/Run2023B-EcalESAlign-PromptReco-v1/ALCARECO",
    ]

    for i, dataset in enumerate(datasets):
        txtFile = 'new_files_0%d.txt' % i
        command = 'dasgoclient --query="file dataset=%s" > %s' % (dataset, txtFile)
        exe(command)
        print ">>> %s is created" % txtFile

def sort_root_files():
    print ">>> start sorting files..."
    
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
    print ">>> %s is created" % output

def check_lumi():
    print ">>> start checking lumi through DAS..."

    txtFile = "lumi_2023.txt"
    exe('echo "# init lumi" > %s' % txtFile)

    fin = open("list_sorted_runs.txt", 'r')
    rootfiles = fin.readlines()

    for f in rootfiles:
        command = 'dasgoclient --query="lumi file=%s" >> %s' % (f, txtFile)
        exe(command)
    print ">>> %s is created" % txtFile

#--------------------------------------------------

if __name__ == "__main__":
    if args.das:
        search_files()

    if args.sort:
        sort_root_files()

    if args.lumi:
        check_lumi()

    print ">>> finished!"
