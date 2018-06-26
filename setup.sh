#!/bin/bash -x

git clone https://github.com/Teemperor/ClangAutoModules.git
cp -r CMSModulesPrep/* .
if [[ ! -d modulemap_files ]]
then
   mkdir modulemap_files
fi
cp get_module_map.py src/
cd src/
python get_module_map.py > `pwd`/modulemap
cd ..
