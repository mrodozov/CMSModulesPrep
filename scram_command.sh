#!/bin/bash -x

#rm -rf $CMSSW_BASE/cppmodulescache/*

USER_CXXFLAGS="-Wno-module-import-in-extern-c -fmodules-cache-path=/tmp/rodozov/cppmodulescache -fmodules -Xclang -fmodules-local-submodule-visibility -fcxx-modules -Wno-register -Rmodule-build -ivfsoverlay "/tmp/rodozov/outputdir/vfs_folder"" scram b -v -j $1 COMPILER=llvm 2>&1
