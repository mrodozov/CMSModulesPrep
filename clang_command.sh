#!/bin/bash -x

if [[ ! -d /tmp/$(whoami)/outputdir ]]; then
mkdir /tmp/$(whoami)/outputdir
fi

#if [[ -e /tmp/$(whoami)/outputdir/log.log ]]; then
#rm /tmp/$(whoami)outputdir/log.log
#fi

./ClangAutoModules/ClangModules.py --modulemap-dir ${CMSSW_BASE}/ClangAutoModules/files --output-dir /tmp/$(whoami)/outputdir --vfs-output /tmp/$(whoami)/outputdir/vfs_folder  --log /tmp/$(whoami)/outputdir/log.log -I "/usr/include:/build/cmsbld/all/inst/slc7_amd64_gcc630/external/boost/1.63.0-omkpbe2/include" --invocation "clang -std=c++11"
