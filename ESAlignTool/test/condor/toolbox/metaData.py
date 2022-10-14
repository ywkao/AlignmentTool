#!/usr/bin/env python2

content = '''+JobFlavour = "workday"

periodic_release =  (NumJobStarts < 4) && ((CurrentTime - EnteredCurrentStatus) > 60) 

getenv     = True 
myPath     = {PATH}/test
executable = $(myPath)/condor/script.sh
input      = $(myPath)/AlignIter_cfg.py

should_transfer_files = YES
transfer_input_files  = $(myPath)/inputFiles_cfi.py, $(myPath)/inputMatrixElements_cfi.py, $(myPath)/Cert_Collisions2022_355100_357900_Golden.json
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
    AlignIter_cfg.py $(iteration) batch11 AlignmentFile_iter$(iteration)_output11.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch12 AlignmentFile_iter$(iteration)_output12.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch13 AlignmentFile_iter$(iteration)_output13.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch14 AlignmentFile_iter$(iteration)_output14.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch15 AlignmentFile_iter$(iteration)_output15.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch16 AlignmentFile_iter$(iteration)_output16.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch17 AlignmentFile_iter$(iteration)_output17.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch18 AlignmentFile_iter$(iteration)_output18.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch19 AlignmentFile_iter$(iteration)_output19.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch20 AlignmentFile_iter$(iteration)_output20.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch21 AlignmentFile_iter$(iteration)_output21.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch22 AlignmentFile_iter$(iteration)_output22.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch23 AlignmentFile_iter$(iteration)_output23.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch24 AlignmentFile_iter$(iteration)_output24.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch25 AlignmentFile_iter$(iteration)_output25.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch26 AlignmentFile_iter$(iteration)_output26.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch27 AlignmentFile_iter$(iteration)_output27.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch28 AlignmentFile_iter$(iteration)_output28.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch29 AlignmentFile_iter$(iteration)_output29.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch30 AlignmentFile_iter$(iteration)_output30.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch31 AlignmentFile_iter$(iteration)_output31.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch32 AlignmentFile_iter$(iteration)_output32.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch33 AlignmentFile_iter$(iteration)_output33.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch34 AlignmentFile_iter$(iteration)_output34.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch35 AlignmentFile_iter$(iteration)_output35.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch36 AlignmentFile_iter$(iteration)_output36.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch37 AlignmentFile_iter$(iteration)_output37.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch38 AlignmentFile_iter$(iteration)_output38.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch39 AlignmentFile_iter$(iteration)_output39.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch40 AlignmentFile_iter$(iteration)_output40.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch41 AlignmentFile_iter$(iteration)_output41.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch42 AlignmentFile_iter$(iteration)_output42.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch43 AlignmentFile_iter$(iteration)_output43.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch44 AlignmentFile_iter$(iteration)_output44.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch45 AlignmentFile_iter$(iteration)_output45.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch46 AlignmentFile_iter$(iteration)_output46.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch47 AlignmentFile_iter$(iteration)_output47.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch48 AlignmentFile_iter$(iteration)_output48.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch49 AlignmentFile_iter$(iteration)_output49.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch50 AlignmentFile_iter$(iteration)_output50.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch51 AlignmentFile_iter$(iteration)_output51.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch52 AlignmentFile_iter$(iteration)_output52.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch53 AlignmentFile_iter$(iteration)_output53.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch54 AlignmentFile_iter$(iteration)_output54.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch55 AlignmentFile_iter$(iteration)_output55.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch56 AlignmentFile_iter$(iteration)_output56.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch57 AlignmentFile_iter$(iteration)_output57.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch58 AlignmentFile_iter$(iteration)_output58.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch59 AlignmentFile_iter$(iteration)_output59.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch60 AlignmentFile_iter$(iteration)_output60.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch61 AlignmentFile_iter$(iteration)_output61.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch62 AlignmentFile_iter$(iteration)_output62.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch63 AlignmentFile_iter$(iteration)_output63.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch64 AlignmentFile_iter$(iteration)_output64.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch65 AlignmentFile_iter$(iteration)_output65.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch66 AlignmentFile_iter$(iteration)_output66.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch67 AlignmentFile_iter$(iteration)_output67.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch68 AlignmentFile_iter$(iteration)_output68.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch69 AlignmentFile_iter$(iteration)_output69.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch70 AlignmentFile_iter$(iteration)_output70.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch71 AlignmentFile_iter$(iteration)_output71.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch72 AlignmentFile_iter$(iteration)_output72.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch73 AlignmentFile_iter$(iteration)_output73.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch74 AlignmentFile_iter$(iteration)_output74.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch75 AlignmentFile_iter$(iteration)_output75.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch76 AlignmentFile_iter$(iteration)_output76.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch77 AlignmentFile_iter$(iteration)_output77.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch78 AlignmentFile_iter$(iteration)_output78.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch79 AlignmentFile_iter$(iteration)_output79.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch80 AlignmentFile_iter$(iteration)_output80.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch81 AlignmentFile_iter$(iteration)_output81.root $(myPath)/condor/{DIR}
    AlignIter_cfg.py $(iteration) batch82 AlignmentFile_iter$(iteration)_output82.root $(myPath)/condor/{DIR}
)
'''
