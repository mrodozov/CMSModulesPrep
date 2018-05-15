#Get the image and mount minimal number of folders:

docker run -it --rm -v /build:/build -v /tmp:/tmp cmssw/slc7-builder:latest bash

#get into the build dir and make a dir with 777 permissions

mkdir install;
chmod 777 install;
cd install;

#get the bootstrap and run it

wget cmsrep.cern.ch/cmssw/bootstrap.sh ;
sh ./bootstrap.sh -a slc7_amd64_gcc630 setup ;
./common/cmspkg -a slc7_amd64_gcc630 install -y cms+cmssw+CMSSW_10_2_0_pre3 ;

#after it's finished as it takes some time, source the environment:

source cmsset_default.sh ;

#now get a CMSSW release,this one is recent one:

scram p CMSSW_10_2_0_pre3 ;

#setup cmsenv

cd CMSSW_10_2_0_pre3 ;

cmsenv

#the release is set up, get the ClangModules repo and the workaround scripts

git clone https://github.com/mrodozov/CMSModulesPrep.git

cp CMSModulesPrep/setup.sh .

./setup.sh

#this will get ClangModules repo, cmssw module map and it would put it in the src dir

#move the module.module map from src as git-cms-addpkg would complain otherwise that src is not empty

#add it later when packages are added

mv src/module.modulemap .

#prepare vfs and mapping files running clang_commands.sh

./clang_command.sh

#change the vfs_folder file in /tmp/cmsbuild/outputdir/vfs_folder to override the root include with empty.modulemap
#the file is adjusted for the given env and paths, edit if needed 

cp vfs_folder /tmp/cmsbuild/outputdir/vfs_folder

#add a pkg, default would be FWCore. Put the module map back in src

git-cms-addpkg FWCore

cp module.modulemap src/

#run scram. currently it runs with -k option

./scram_command.sh 8

