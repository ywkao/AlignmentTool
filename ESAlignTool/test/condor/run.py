#!/usr/bin/env python2
import os
import subprocess
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-e', help = "execute the script", action = 'store_true')
parser.add_argument('-i', help = "enable iterations", action = 'store_true')
parser.add_argument('-r', help = "run the interation code", action = 'store_true')
parser.add_argument('-m', help = "make residual plots", action = 'store_true')
parser.add_argument("-o", help = "set output directory", type=str, default = "result")
args = parser.parse_args()

iteration = 9
directory = args.o
path = "/afs/cern.ch/user/y/ykao/work/esAlignment/CMSSW_8_0_8/src/AlignmentTool/ESAlignTool"

#----------------------------------------------------------------------------------------------------

def exe(command):
    if args.e:
        subprocess.call(command, shell=True)
    else:
        print ">>>", command

def run(iteration):
    ## run iteration
    output_file = "%s/AlignmentFile_iter%d.root" % (directory, iteration)
    input_files = "%s/AlignmentFile_iter%d_output0*.root" % (directory, iteration)
    command = "hadd -f %s %s" % (output_file, input_files)
    exe(command)

    # retrieve new values
    os.chdir( path+"/myAna" )
    command = "root -l -q 'getESMInfo.C(%d, \"%s\")'" % (iteration, path + "/test/condor/" + output_file)
    exe(command)
    
    # update result
    os.chdir( path+"/test" )
    command = "cat ../myAna/test_py.txt | tail -n 25 | tee -a inputMatrixElements_cfi.py"
    exe(command)

#----------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    subprocess.call("mkdir -p %s/out" % directory, shell=True)
    subprocess.call("mkdir -p %s/err" % directory, shell=True)
    subprocess.call("mkdir -p %s/log" % directory, shell=True)

    # Later, I want to auto creating exe.sub
    subprocess.call("time condor_submit ./submit/exe.sub", shell=True)

    # I want to auto monitor condor jobs
    print ">>> check..."
    
    run(iteration)

    print ">>> finished!"
