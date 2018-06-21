#!/bin/bash -x

export here=`pwd`

if [[ ! -d $here/outputdir ]]; then
mkdir -p $here/outputdir
fi

if [[ ! -e $here/outputdir/log.log ]]; then
touch $here/outputdir/log.log
fi

./ClangAutoModules/ClangModules.py \
	--modulemap-dir ${CMSSW_BASE}/ClangAutoModules/files \
	--output-dir $here/outputdir \
	--vfs-output $here/outputdir/vfs_folder \
	--log $here/outputdir/log.log \
	-I "/usr/include:/cvmfs/cms-ib.cern.ch/nweek-02528/slc7_amd64_gcc630/external/boost/1.63.0-omkpbe2/include" --invocation "clang -std=c++11"
