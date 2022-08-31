#!/usr/bin/env python2
import subprocess

path = "/afs/cern.ch/user/y/ykao/work/esAlignment/CMSSW_12_3_0_pre5/src/AlignmentTool/ESAlignTool/test/condor/result"

def exe(command):
    print command
    subprocess.call(command, shell=True)


def make_plots():
    command = "root -l -b -q DrawResidual_comparison.C"
    exe(command)
    
    iters = [1, 11]
    for i in iters:
        command = "root -l -b -q 'DrawResidual.C(%2d,  \"%s/AlignmentFile_iter%d.root\")'" % (i, path, i)
        exe(command)

        continue

        command = "root -l -b -q 'DrawHits.C(\"%s/AlignmentFile_iter%d.root\", \"HitMap_iter%d\")'" % ( path, i, i)
        exe(command)

if __name__ == "__main__":
    make_plots()
