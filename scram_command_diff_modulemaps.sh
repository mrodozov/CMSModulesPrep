#!/bin/bash -x

#rm -rf $CMSSW_BASE/cppmodulescache/*

export here=`pwd`

for i in `cat $1`
do

export mm_file=`echo CMS_${i} | sed "s/\//_/g"`
echo 'Package ' $i

#put the if not modulemap_files/$mm_file.txt then continue here

if [[ ! -e modulemap_files/$mm_file ]]; then
continue
fi

mkdir -p modulescache/$i

git-cms-addpkg $i
cp modulemap_files/$mm_file.txt  $here/src/module.modulemap

USER_CXXFLAGS="-Wno-module-import-in-extern-c -fmodules-cache-path=$here/modulescache/$i -fmodules -Xclang -fmodules-local-submodule-visibility -fcxx-modules -Wno-register -Rmodule-build -ivfsoverlay "$here/outputdir/vfs_folder"" scram b -v -k -j 1 COMPILER=llvm > $here/modulescache/$i/${mm_file}.log  2>&1

rm -rf src
scram b clean

done

