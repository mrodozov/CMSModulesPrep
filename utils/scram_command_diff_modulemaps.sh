#!/bin/bash -x

#rm -rf $CMSSW_BASE/cppmodulescache/*

for i in `cat $1`
do

export mm_file=`echo CMS_${i} | sed "s/\///g"`
echo 'Package ' $i

#put the if not modulemap_files/$mm_file.txt then continue here

mkdir -p modulescache/$i

git-cms-addpkg $i
cp modulemap_files/$mm_file.txt  /build/cmsbld/mrodozov/CMSSW_10_2_X_2018-06-12-2300/src/module.modulemap

USER_CXXFLAGS="-Wno-module-import-in-extern-c -fmodules-cache-path=/build/cmsbld/mrodozov/CMSSW_10_2_X_2018-06-12-2300/modulescache/$i -fmodules -Xclang -fmodules-local-submodule-visibility -fcxx-modules -Wno-register -Rmodule-build -ivfsoverlay "/tmp/$(whoami)/outputdir/vfs_folder"" scram b -v -k -j 1 COMPILER=llvm > /build/cmsbld/mrodozov/CMSSW_10_2_X_2018-06-12-2300/modulescache/$i/${mm_file}.log  2>&1

rm -rf src
scram b clean

done

