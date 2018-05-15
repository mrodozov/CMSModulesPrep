#!/bin/bash -x

git clone https://github.com/Teemperor/ClangAutoModules.git
git clone https://github.com/mrodozov/CMSModulesPrep.git
cp CMSModulesPrep/* .
wget https://teemperor.de/pub/module.log
mv module.log src/module.modulemap
