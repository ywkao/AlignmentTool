#!/usr/bin/env python2
import subprocess

#path = "/afs/cern.ch/user/y/ykao/work/esAlignment/CMSSW_12_4_3/src/AlignmentTool/ESAlignTool/test/condor/result"
path = "/eos/cms/store/user/ykao/esAlignment/CMSSW_12_4_3/result_withJulyDB_20221014"

def exe(command):
    print command
    subprocess.call(command, shell=True)

def make_hit_map():
    idx = 7
    command = "root -l -b -q 'DrawHits.C(\"%s/AlignmentFile_iter%d.root\", \"HitMap_iter%d\")'" % ( path, idx, idx)

    idx = 8
    subidx = 82
    rootfile = "/eos/cms/store/user/ykao/esAlignment/CMSSW_12_4_3/result_20221014_playground/AlignmentFile_iter8_output35.root"
    rootfile = "/eos/cms/store/user/ykao/esAlignment/CMSSW_12_4_3/result_20221014_playground/AlignmentFile_iter8_output82.root"
    command = "root -l -b -q 'DrawHits.C(\"%s\", \"HitMap_iter%d_output%d\")'" % ( rootfile, idx, subidx)

    exe(command)

def make_comparison_plot():
    command = "root -l -b -q 'DrawResidual_comparison.C(\"%s\")'" % path
    exe(command)

def make_individual_plots():
    iters = [1, 11]
    for i in iters:
        command = "root -l -b -q 'DrawResidual.C(%2d,  \"%s/AlignmentFile_iter%d.root\")'" % (i, path, i)
        exe(command)

        continue

        command = "root -l -b -q 'DrawHits.C(\"%s/AlignmentFile_iter%d.root\", \"HitMap_iter%d\")'" % ( path, i, i)
        exe(command)

if __name__ == "__main__":
    #make_comparison_plot()
    make_hit_map()
