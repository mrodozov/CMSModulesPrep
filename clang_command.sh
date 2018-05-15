#!/bin/bash -x

if [[ ! -d /tmp/${USER}/outputdir ]]; then
mkdir /tmp/${USER}/outputdir
fi

#if [[ ! -e /tmp/${USER}/outputdir/log.log ]]; then
#rm /tmp/${USER}outputdir/log.log
#fi

./ClangAutoModules/ClangModules.py --modulemap-dir ${CMSSW_BASE}/ClangAutoModules/files --output-dir /tmp/${USER}/outputdir --vfs-output /tmp/${USER}/outputdir/vfs_folder  --log /tmp/rodozov/outputdir/log.log -I "/usr/include:/cvmfs/cms-ib.cern.ch/nweek-02523/slc7_amd64_gcc630/external/boost/1.63.0-omkpbe2/include:/cvmfs/cms-ib.cern.ch/nweek-02523/slc7_amd64_gcc630/external/tinyxml/2.5.3-omkpbe2/include/" --invocation "clang -std=c++11"
