#!/usr/bin/env python
import subprocess
import glob
from termcolor import colored
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-e", "--exe" , help = "Execute submission if adding --exe", action = "store_true")
parser.add_argument("-m", "--monitor" , help = "Minitor submitted jobs if adding --monitor", action = "store_true")
parser.add_argument("--employed" , nargs = '+', help = "Input ids of bigbird machines, ex. ./check_htcondor.py --monitor --employed 08 11 12")
args = parser.parse_args()


employed_machines = {'green':[]}
log = "log_submission.txt"
log_machine_status = "tmp_log_machine_status.txt"

def check(machine_id):
    global log, employed_machines
    employed_machines['green'].append(machine_id)
    subprocess.call("mybigbird %s 2>&1 >> %s " % (machine_id, log), shell = True)

def check_bigbird_machine():
    global log
    with open(log, 'w') as f:
        f.write(">>> start checking... \n")

    if args.employed != None:
        for num in args.employed:
            check(str(num))

def check_machine_status():
    global employed_machines

    subprocess.call("condor_status -schedd > %s" % log_machine_status, shell = True)
    d = {}
    with open(log_machine_status, 'r') as f:
        for line in f.readlines():
            if 'bigbird' in line:
                machine = line.strip().split()[0]
                num_running = int(line.strip().split()[2])
                num_idle = int(line.strip().split()[3])
                pack = "%s:( %d / %d )" % (machine, num_running, num_idle)
                if num_idle > 0:
                    #print "%s: %.2f ( %d / %d )" % (machine, ratio, num_running, num_idle)
                    ratio = float(num_running) / float(num_idle)
                    d[pack] = ratio

    d_sorted = sorted(d.items(), key=lambda x: x[1], reverse=True)
    if len(employed_machines) == 0:
        for ele in d_sorted:
            print "%s: %.2f %s" % (ele[0].split(':')[0], ele[1], ele[0].split(':')[1])
    else:
        for ele in d_sorted:
            machine  = ele[0].split(':')[0]
            moreInfo = ele[0].split(':')[1]
            message = "%s: %.2f %s" % (machine, ele[1], moreInfo)

            # bigbird15.cern.ch
            machineId = machine[7:9]

            # determine text color
            color = 'white'
            for specified_color in employed_machines.keys():
                high_light_ids = employed_machines[specified_color]

                for mId in high_light_ids:
                    if machineId == mId:
                        color = specified_color

            print colored(message, color)
    
    raw_input("Press Enter to continue...")

def submit(machine_id, command):
    global log
    subprocess.call("mybigbird %s && %s && condor_q 2>&1 >> %s" % (machine_id, command, log), shell = True)

def exe_submission():
    global log
    with open(log, 'w') as f:
        f.write(">>> start submission... \n")

    #submit("23", "condor_submit dir_sig_2017/runJobs3.sub")
    #submit("23", "condor_submit dir_sig_2018/runJobs7.sub")
    #submit("23", "condor_submit dir_smh_2016/runJobs2.sub")

if __name__ == "__main__":
    if args.monitor:
        check_bigbird_machine() # update employed_machines
        check_machine_status()
        if args.employed != None:
            subprocess.call("vim %s" % log, shell = True)

    if args.exe:
        exe_submission()

    print ">>> finished!"
