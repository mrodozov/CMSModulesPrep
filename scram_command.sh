#!/bin/bash -x

#rm -rf $CMSSW_BASE/cppmodulescache/*

USER_CXXFLAGS="-Wno-module-import-in-extern-c -fmodules-cache-path=/tmp/${USER}/cppmodulescache -fmodules -Xclang -fmodules-local-submodule-visibility -fcxx-modules -Wno-register -Rmodule-build -ivfsoverlay "/tmp/${USER}/outputdir/vfs_folder"" scram b -v -j $1 COMPILER=llvm 2>&1
