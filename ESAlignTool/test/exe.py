#!/usr/bin/env python
import os
import subprocess
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-e', help = "execute the script", action = 'store_true')
parser.add_argument('-m', help = "make residual plots", action = 'store_true')
parser.add_argument('-r', help = "run the interation code", action = 'store_true')
args = parser.parse_args()

start_iteration = True
start_iteration = False

def exe(command):
    if args.e:
        subprocess.call(command, shell=True)
    else:
        print ">>>", command

def run(iteration):
    # run iteration
    command = "cmsRun AlignIter_cfg.py IterN=%d OutFilename=AlignmentFile_iter%d.root InputRefitter=False TrackLabel=ecalAlCaESAlignTrackReducer" % (iteration, iteration)
    exe(command)
    
    # retrieve new values
    os.chdir("../myAna")
    command = "root -l -q 'getESMInfo.C(%d)'" % iteration
    exe(command)
    
    # update result
    os.chdir("../test")
    command = "cat ../myAna/test_py.txt | tail -n 25 | tee -a inputMatrixElements_cfi.py"
    exe(command)

def make_plots():
    os.chdir("../macro")
    command = "root -l -b -q 'DrawResidual.C'"
    subprocess.call(command, shell=True)
    
    #command = "cp *png /eos/user/y/ykao/www/ESAlignment"
    #subprocess.call(command, shell=True)

if __name__ == "__main__":
    if args.r:
        if start_iteration:
            for iteration in range(2,12):
                print ">>> start iteration: %d" % iteration
                run(iteration)
        else:
            iteration = 1
            iteration = 0
            print ">>> start iteration: %d" % iteration
            run(iteration)

    if args.m:
        make_plots()

    print ">>> finished!"
# /eos/cms/store/group/dpg_ecal/alca_ecalcalib/ESAlignment/ESALCALRECO_CMSSW_8_0_7_patch3_v2/HLTPhysics/crab_HLTPhysics_Run2016B-v1/160513_115757/0000
