#!/bin/bash -x

git clone https://github.com/Teemperor/ClangAutoModules.git
cp CMSModulesPrep/* .
#wget https://teemperor.de/pub/module.log
cp module.modulemap src/module.modulemap
