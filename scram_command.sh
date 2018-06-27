#!/bin/bash -x

#rm -rf $CMSSW_BASE/cppmodulescache/*

export here=`pwd`

USER_CXXFLAGS="-Wno-module-import-in-extern-c -fmodules-cache-path=$here/cppmodulescache -fmodules -Xclang -fmodules-local-submodule-visibility -fcxx-modules -Wno-register -Rmodule-build -ivfsoverlay "$here/outputdir/vfs_folder"" scram b -v -k -j $1 COMPILER=llvm 2>&1
