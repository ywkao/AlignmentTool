#!/usr/bin/env python2

content = '''+JobFlavour = "workday"

periodic_release =  (NumJobStarts < 4) && ((CurrentTime - EnteredCurrentStatus) > 60) 

getenv     = True 
myPath     = {PATH}/test
executable = $(myPath)/condor/script.sh
input      = $(myPath)/AlignIter_cfg.py

should_transfer_files = YES
transfer_input_files  = $(myPath)/inputFiles_cfi.py, $(myPath)/inputMatrixElements_cfi.py, $(myPath)/Cert_Collisions2022_355100_357900_Golden.json, $(myPath)/ESAlignments_Run3_2022B_iter11.db
transfer_output_files = ""

output     = $(myPath)/condor/{DIR}/out/hello.$(ClusterID).$(ProcID).out
error      = $(myPath)/condor/{DIR}/err/hello.$(ClusterID).$(ProcID).err
log        = $(myPath)/condor/{DIR}/log/hello.$(ClusterID).$(ProcID).log

iteration = {ITERN}
queue arguments from (
    AlignIter_cfg.py $(iteration) batch01 AlignmentFile_iter$(iteration)_output01.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch02 AlignmentFile_iter$(iteration)_output02.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch03 AlignmentFile_iter$(iteration)_output03.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch04 AlignmentFile_iter$(iteration)_output04.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch05 AlignmentFile_iter$(iteration)_output05.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch06 AlignmentFile_iter$(iteration)_output06.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch07 AlignmentFile_iter$(iteration)_output07.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch08 AlignmentFile_iter$(iteration)_output08.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch09 AlignmentFile_iter$(iteration)_output09.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch10 AlignmentFile_iter$(iteration)_output10.root $(myPath)/condor/{DIR}
)
'''
