#!/bin/bash
#----------------------------------------------------------------------------------------------------
# set up env
#----------------------------------------------------------------------------------------------------
export XRD_NETWORKSTACK=IPv4
export X509_USER_PROXY=/afs/cern.ch/user/y/ykao/x509up_u75423
env SHELL=/bin/sh gdb cmsRun # https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideTroubleShootingMore
WD=$PWD

my_working_directory=$5
cd $my_working_directory
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval $(scram runtime -sh)
export PYTHONHOME=`scram tool info python | grep PYTHON_BASE | sed 's/PYTHON_BASE=//'`
cd $WD

echo ""
echo "-------------------------------------------- env check ---------------------------------------------"
echo ">>> pwd"; pwd
echo ">>> ls -lhrt ."; ls -lhrt .
echo ">>> ls $X509_USER_PROXY"; ls $X509_USER_PROXY
echo ">>> echo $PYTHONHOME"; echo $PYTHONHOME
echo ">>> which root"; which root  # check root
echo "----------------------------------------------------------------------------------------------------"
echo ""

#----------------------------------------------------------------------------------------------------
# main code
#----------------------------------------------------------------------------------------------------
echo $@; exe=$1; itern=$2; inputTag=$3; outputFile=$4; echo ""
time cmsRun ${exe} print IterN=${itern} myInputTag=${inputTag} OutFilename=${outputFile} InputRefitter=False TrackLabel=ecalAlCaESAlignTrackReducer JSONFilename=Cert_Collisions2022_355100_357900_Golden.json

#----------------------------------------------------------------------------------------------------
# transfer back
#----------------------------------------------------------------------------------------------------
errors=""
for file in $(find -name '*.root'); do
    echo ">>> cp -pv ${file} ${my_working_directory}"; cp -pv ${file} ${my_working_directory};
    if [[ $? != 0 ]]; then errors="$errors $file($?)"; fi
done

for file in $(find -name 'log*'); do
    echo ">>> cp -pv ${file} ${my_working_directory}"; cp -pv ${file} ${my_working_directory};
done

if [[ -n "$errors" ]]; then
   echo "Errors while staging files"
   echo "$errors"
   exit -2
fi
