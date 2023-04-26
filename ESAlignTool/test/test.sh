#!/bin/bash

tag="130XGT"
time cmsRun AlignIter_cfg.py print IterN=1 myInputTag=default OutFilename=pureTest_AlignmentFile_iter1_output01_${tag}.root InputRefitter=False TrackLabel=ecalAlCaESAlignTrackReducer 2>&1 | tee log_${tag}.txt

#--------------------------------------------------
# run with json file
#--------------------------------------------------
#time cmsRun validate_cfg.py print IterN=1 myInputTag=default OutFilename=pureTest_AlignmentFile_iter1_output01_${tag}.root JSONFilename=./Cert_Collisions2022_355100_357900_Golden.json InputRefitter=False TrackLabel=ecalAlCaESAlignTrackReducer 2>&1 | tee log_${tag}.txt

#--------------------------------------------------
# validation
#--------------------------------------------------
#time cmsRun validate_cfg.py print IterN=1 myInputTag=default OutFilename=pureTest_AlignmentFile_iter1_output01.root InputRefitter=False TrackLabel=ecalAlCaESAlignTrackReducer 2>&1 | tee log.txt

#--------------------------------------------------
# quick test
#--------------------------------------------------
#time cmsRun validate_cfg.py print MaxEvents=1 IterN=1 myInputTag=default OutFilename=pureTest_AlignmentFile_iter1_output01_${tag}.root InputRefitter=False TrackLabel=ecalAlCaESAlignTrackReducer 2>&1 | tee log_${tag}.txt

#--------------------------------------------------
# quick test with more details stored
#--------------------------------------------------
#time cmsRun validate_cfg.py print MaxEvents=1 IterN=1 myInputTag=default OutFilename=pureTest_AlignmentFile_iter1_output01_${tag}.root InputRefitter=False TrackLabel=ecalAlCaESAlignTrackReducer StoreDetail=True 2>&1 | tee log_${tag}.txt
