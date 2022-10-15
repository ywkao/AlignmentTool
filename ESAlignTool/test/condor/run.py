#!/usr/bin/env python2
import os, glob, time
import subprocess
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-e', help = "execute the script", action = 'store_true')
parser.add_argument("-o", help = "set output directory", type=str, default = "result")
args = parser.parse_args()

directory = args.o
path = os.getcwd().split("/test/condor")[0]

NumberExpectedOutputFiles = 82 

#----------------------------------------------------------------------------------------------------

def init():
    subprocess.call("mkdir -p %s/out" % directory, shell=True)
    subprocess.call("mkdir -p %s/err" % directory, shell=True)
    subprocess.call("mkdir -p %s/log" % directory, shell=True)
    subprocess.call("mkdir -p %s/tmp" % directory, shell=True)

def exe(command):
    if args.e:
        subprocess.call(command, shell=True)
    else:
        print ">>>", command
        #print command

def rename_directory(sub_dir, iteration):
    original = path + "/test/condor/" + directory + "/" + sub_dir
    modified = path + "/test/condor/" + directory + "/" + sub_dir + "_iteration_%d" % (iteration)
    command = "mv %s %s" % (original, modified)
    exe(command)

def job_monitor():
    print "\n--------------------------------------- start job monitoring ---------------------------------------"
    time.sleep(1800) # 30 min
    duration = 1800.

    # monitor condor jobs
    wait_time = 120.
    running = True
    while running:
        counter = 0
        subprocess.call("condor_q > tmp.txt", shell=True)

        # check how many jobs are running
        fin = open("tmp.txt", 'r')
        for line in fin.readlines():
            if 'ykao' in line and 'ID' in line:
                counter += 1
                ndone = line.split()[5]
                nrun  = line.split()[6]
                nidle = line.split()[7]
        fin.close()

        if counter == 0:
            print "All jobs are finished!"
            break
        else:
            print "Remaining jobs (DONE/RUN/IDLE):", ndone, nrun, nidle, ", time = %.1f min, wait for %.0f seconds..." % (duration/60., wait_time)
            duration += wait_time 
            time.sleep(wait_time)

    # monitor output files
    wait_time = 60.
    transferring = True
    while transferring:
        outputfiles = glob.glob(input_files)
        if len(outputfiles)==NumberExpectedOutputFiles:
            print "All output files transferred!", outputfiles
            break
        else:
            print "Output files coming back.", ", time = %.1f min, wait for %.0f senconds..." % (duration/60., wait_time)
            duration += wait_time 
            time.sleep(wait_time)

    print "-------------------------------------- end of job monitoring ---------------------------------------\n"

def run(iteration):
    # recreate a sub file
    import toolbox.metaData as m
    with open("./submit/exe.sub", 'w') as fsub:
        fsub.write(m.content.format(PATH=path, ITERN=iteration, DIR=directory))

    print "\n---------------------------------------- ./submit/exe.sub ------------------------------------------"
    with open("./submit/exe.sub", 'r') as fin:
        for line in fin.readlines():
            print line.strip()
    print "----------------------------------------------------------------------------------------------------\n"

    # submit jobs
    command = "time condor_submit ./submit/exe.sub"
    exe(command)

    # monitor jobs
    if args.e:
        job_monitor()

    # hadd
    rootfile = path + "/test/condor/" + output_file
    command = "hadd -f %s %s" % (rootfile, input_files)
    exe(command)

    tmp = path + "/test/condor/" + directory + "/tmp"
    command = "mv %s %s" % (input_files, tmp)
    exe(command)

    # prevent >1,000 files in single directories
    rename_directory("tmp", iteration)
    rename_directory("log", iteration)
    rename_directory("err", iteration)
    rename_directory("out", iteration)
    init()

    # retrieve new values
    os.chdir( path+"/myAna" )
    command = "root -l -q 'getESMInfo.C(%d, \"%s\")'" % (iteration, rootfile)
    exe(command)
    
    # update result
    os.chdir( path+"/test" )
    command = "cat ../myAna/test_py.txt | tail -n 25 | tee -a inputMatrixElements_cfi.py"
    exe(command)

    # make residual plots
    os.chdir( path+"/macro")
    command = "root -l -b -q 'DrawResidual.C(%d, \"%s\")'" % (iteration, rootfile)
    exe(command)

    # reset
    os.chdir( path+"/test/condor" )


def print_command(iteration):
    rootfile = path + "/test/condor/" + output_file
    command = "root -l -b -q 'DrawResidual.C(%d, \"%s\")'" % (iteration, rootfile)
    print command

#----------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    init()

    scope = range(3,12)
    scope = range(2,12)
    scope = range(1,2)
    scope = range(2,8)

    #for iteration in scope:
    #    output_file = "%s/AlignmentFile_iter%d.root" % (directory, iteration)
    #    print_command(iteration)
    #exit()

    for iteration in scope:
        print "\n================================================== intration:", iteration, "=================================================="
        output_file = "%s/AlignmentFile_iter%d.root" % (directory, iteration)
        input_files = "%s/AlignmentFile_iter%d_output*.root" % (directory, iteration)
        run(iteration)

    print ">>> finished!"
