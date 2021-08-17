#!/usr/bin/env python
import os
import subprocess

start_iteration = False
start_iteration = True

def run(iteration):
    # run iteration
    command = "cmsRun AlignIter_cfg.py IterN=%d OutFilename=AlignmentFile_iter%d.root InputRefitter=False TrackLabel=ecalAlCaESAlignTrackReducer" % (iteration, iteration)
    subprocess.call(command, shell=True)
    
    # retrieve new values
    os.chdir("../myAna")
    command = "root -l -q 'getESMInfo.C(%d)'" % iteration
    subprocess.call(command, shell=True)
    
    # update result
    os.chdir("../test")
    command = "cat ../myAna/test_py.txt | tail -n 25 | tee -a inputMatrixElements_cfi.py"
    subprocess.call(command, shell=True)

def make_plots():
    os.chdir("../macro")
    command = "root -l -q 'DrawResidual.C'"
    subprocess.call(command, shell=True)
    
    command = "cp *png /eos/user/y/ykao/www/ESAlignment"
    subprocess.call(command, shell=True)

if __name__ == "__main__":
    if start_iteration:
        for iteration in range(11,12):
            print ">>> start iteration: %d" % iteration
            run(iteration)

    make_plots()

# /eos/cms/store/group/dpg_ecal/alca_ecalcalib/ESAlignment/ESALCALRECO_CMSSW_8_0_7_patch3_v2/HLTPhysics/crab_HLTPhysics_Run2016B-v1/160513_115757/0000
