#!/usr/bin/env python2

content = '''+JobFlavour = "espresso"

periodic_release =  (NumJobStarts < 4) && ((CurrentTime - EnteredCurrentStatus) > 60) 

getenv     = True 
myPath     = /afs/cern.ch/user/y/ykao/work/esAlignment/CMSSW_8_0_8/src/AlignmentTool/ESAlignTool/test
executable = $(myPath)/condor/script.sh
input      = $(myPath)/AlignIter_cfg.py

should_transfer_files = YES
transfer_input_files  = $(myPath)/inputFiles_cfi.py, $(myPath)/inputMatrixElements_cfi.py
transfer_output_files = ""

output     = $(myPath)/condor/{DIR}/out/hello.$(ClusterID).$(ProcID).out
error      = $(myPath)/condor/{DIR}/err/hello.$(ClusterID).$(ProcID).err
log        = $(myPath)/condor/{DIR}/log/hello.$(ClusterID).$(ProcID).log

iteration = {ITERN}
queue arguments from (
    #AlignIter_cfg.py $(iteration) default AlignmentFile_iter$(iteration).root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch01 AlignmentFile_iter$(iteration)_output01.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch02 AlignmentFile_iter$(iteration)_output02.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch03 AlignmentFile_iter$(iteration)_output03.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch04 AlignmentFile_iter$(iteration)_output04.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch05 AlignmentFile_iter$(iteration)_output05.root $(myPath)/condor/{DIR}
)
'''
