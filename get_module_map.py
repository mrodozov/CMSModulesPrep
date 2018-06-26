#!/usr/bin/env python

import os
import sys

ignored_headers = [
  # CMS things
  "DataFormats/Common/interface/AssociativeIterator.h",
  "DataFormats/Math/interface/AVXVec.h", # Can't be used alone, needs Vec4 definition.
  "GeneratorInterface/Core/interface/RNDMEngineAccess.h", # Obsolete header DONE
  "GeneratorInterface/Pythia8Interface/interface/RandomP8.h", # Obsolete header
  "Geometry/Records/interface/GeometricDetExtraRcd.h", # Obsolete header
  "DataFormats/RecoCandidate/interface/RecoPFClusterRefCandidate.h", # Obsolete header DONE
  "DataFormats/RecoCandidate/interface/RecoPFClusterRefCandidateFwd.h", #Obsolete header DONE
  "SimDataFormats/TrackingAnalysis/interface/TrackingDataPrint.h", # Really old code that doesn't compile anymore.
  "CondFormats/Calibration/interface/EfficiencyPayloads.h", # Obsolete header
  "RecoHI/HiMuonAlgos/interface/HICSimpleNavigationSchool.h", #Obsolete header
  "RecoHI/HiMuonAlgos/interface/HICMuonPropagator.h", #Obsolete header
  "RecoHI/HiMuonAlgos/interface/HITrackVertexMaker.h", #Obsolete header
  "RecoHI/HiMuonAlgos/interface/HICMeasurementEstimator.h", #Obsolete header
  "RecoHI/HiMuonAlgos/interface/HICSeedMeasurementEstimator.h", #Obsolete header
  "RecoHI/HiMuonAlgos/interface/FmpConst.h", #Obsolete header
  "RecoHI/HiMuonAlgos/interface/HICTrajectoryBuilder.h", #Obsolete header
  "RecoHI/HiMuonAlgos/interface/HICMuonUpdator.h", #Obsolete header
  "RecoHI/HiMuonAlgos/interface/HICTrajectoryCorrector.h", #Obsolete header
  "RecoHI/HiMuonAlgos/interface/DiMuonSeedGeneratorHIC.h", #Obsolete header
  "RecoHI/HiMuonAlgos/interface/FastMuPropagator.h", #Obsolete header
  "RecoHI/HiMuonAlgos/interface/HICConst.h", #Obsolete header
  "RecoHI/HiMuonAlgos/interface/HICTkOuterStartingLayerFinder.h", #Obsolete header
  "RecoHI/HiMuonAlgos/interface/DiMuonTrajectorySeed.h", #Obsolete header
  "RecoHI/HiMuonAlgos/interface/HICFTSfromL1orL2.h", #Obsolete header
  "CommonTools/Utils/src/CandForTest.h", # Doesn't have header guards....
  "Geometry/TrackerGeometryBuilder/interface/GeomDetLess.h", #Obsolete header
  "Geometry/TrackerGeometryBuilder/interface/GluedGeomDet.h", #Obsolete header
  "CondFormats/GeometryObjects/interface/GeometryFile.h", #Obsolete header
  "TrackingTools/MeasurementDet/interface/GeometricSearchDetMeasurements.h", #Obsolete header
  "TrackingTools/TrajectoryFiltering/interface/BaseCkfTrajectoryFilter.h", #Obsolete header
  "FastSimulation/Utilities/interface/RandomEngine.h", #Obsolete header
  "RecoMuon/MuonIsolation/interface/MuIsoExtractor.h", #Obsolete header
  "RecoMuon/MuonIsolation/interface/MuIsoExtractorFactory.h", #Obsolete header
  "RecoPixelVertexing/PixelTriplets/interface/CombinedHitTripletGenerator.h", #Obsolete header
  "CondFormats/DTObjects/interface/DTCompactMapAbstractHandler.h", #Obsolete header
  "CondFormats/DTObjects/interface/DTConfigAbstractHandler.h", #Obsolete header

  "L1TriggerConfig/GMTConfigProducers/interface/GTRecordGroup.h", #Does funny template stuff

  "L1Trigger/RegionalCaloTrigger/interface/L1GctRegion.h", # Is doing funny C++ things

  "CondTools/SiPixel/interface/PixelPopConDCSSourceHandler.h", #References nonexistent file

  "CommonTools/ParticleFlow/interface/TopProjectors.h", # Is doing strange template things.

  "CondCore/DTPlugins/interface/DTConfigPluginHandler.h", #Obsolete header

  "PhysicsTools/UtilAlgos/interface/AdHocNTupler.h", #includes nonexistent file

  "CondCore/DTPlugins/interface/DTCompactMapPluginHandler.h", #Obsolete header

  "CommonTools/CandAlgos/interface/CandDecaySelector.h", # Specializes StoreManagerTrait in CommonTools/CandAlgos/interface/CandDecaySelector.h:47
#In module 'CMS_CommonToolsUtilAlgos' imported from /home/teemperor/cms/cmssw/CommonTools/CandAlgos/interface/CandCombiner.h:23:
#/home/teemperor/cms/cmssw/CommonTools/UtilAlgos/interface/ObjectSelector.h:35:46: error: missing '#include "CommonTools/CandAlgos/interface/CandDecaySelector.h"'; #definition of
#      'StoreManagerTrait<reco::CandidateCollection, EdmFilter>' must be imported from module 'CMS_CommonToolsCandAlgos.CandDecaySelector.h' before it is required
#         typename StoreManager = typename ::helper::StoreManagerTrait<OutputCollection, edm::EDFilter>::type,
#                                                    ^
#/home/teemperor/cms/cmssw/CommonTools/CandAlgos/interface/ObjectShallowCloneSelector.h:15:43: note: in instantiation of default argument for 'ObjectSelector<type-#parameter-0-0,
#      edm::OwnVector<reco::Candidate, edm::ClonePolicy<reco::Candidate> >, type-parameter-0-1, helper::NullPostProcessor<edm::OwnVector<reco::Candidate, #edm::ClonePolicy<reco::Candidate> >,
#      edm::EDFilter> >' required here
#class ObjectShallowCloneSelector : public ObjectSelector<Selector, reco::CandidateCollection, SizeSelector> {
#                                          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#/home/teemperor/cms/cmssw/CommonTools/CandAlgos/interface/CandDecaySelector.h:47:10: note: previous definition is here
#  struct StoreManagerTrait<reco::CandidateCollection, EdmFilter> {
#         ^


  "RecoLocalCalo/EcalRecAlgos/interface/EcalSeverityLevelService.h", # References EcalSeverityLevel which doesn't seem to exist

  "DataFormats/GeometrySurface/interface/SimpleConeBounds.h", #Calls tmp.inside(p) but that usually takes also a LocalError parameter
  "RecoVertex/KinematicFitPrimitives/interface/KinematicVertexDistance.h", #Includes nonexistent file
  "PhysicsTools/UtilAlgos/interface/StoreManagerTrait.h", #Redefines ObjectSelectorBase, CommonTools/UtilAlgos/interface/StoreManagerTrait.h
  "PhysicsTools/UtilAlgos/interface/BasicFilter.h", #Uses the "vitrual" keyword, that has yet 'to be understood'..., DONE
  "PhysicsTools/UtilAlgos/interface/AdHocNTupler.h", #Includes nonexistent file
  "PhysicsTools/HepMCCandAlgos/interface/MCTruthCompositeMatcher.h", # Includes nonexistend file
  "L1Trigger/CSCTrackFinder/interface/CSCTFSPCoreLogic.h", #Includes missing generated code
  "L1Trigger/CSCTrackFinder/interface/CSCTFSectorProcessor.h", #Includes header above
  "RecoVertex/MultiVertexFit/interface/LinPtFinderFromAdaptiveFitter.h", #Includes nonexistent file
  "CommonTools/RecoAlgos/interface/PixelMatchGsfElectronSelector.h", # Obsolete file
  "CommonTools/UtilAlgos/interface/ObjectCounter.h", #Includes nonexistent file
  "PhysicsTools/CandUtils/interface/CandMatcher.h", #Not even valid core anymore, has std;:vector instead of::... DONE
  "CommonTools/RecoAlgos/interface/PixelMatchGsfElectronSelector.h", #Includes nonexistent file
  "TrackingTools/GsfTools/interface/RCMultiGaussianState.h", #Obsolete code
  "CommonTools/RecoAlgos/interface/PhotonSelector.h", #Does funny things with unique_ptr copying around..
  "PhysicsTools/IsolationUtils/interface/TauConeIsolationAlgo.h", #Includes nonexistent header
  "CommonTools/CandAlgos/interface/NamedCandCombiner.h", #Includes nonexistent header
  "CommonTools/CandUtils/interface/NamedCandCombiner.h", # Constructor doesn't work
  "TrackingTools/GsfTools/interface/KeepingNonZeroWeightsMerger.h", #Includes nonexistent file
  "Mixing/Base/interface/PoissonPUGenerator.h", # calls non-static member function  without object CLHEP::RandPoissonQ
  "RecoVertex/KinematicFitPrimitives/interface/KinematicVertexAssociator.h", #includes nonexistent header

  "CommonTools/Utils/src/CutBinaryOperatorSetter.h", #includes below header
  "CommonTools/Utils/src/CutBinaryOperator.h", #includes nonexistend CutBase.h

  "TrackingTools/TrackFitters/interface/DebugHelpers.h", # textual header

  "MagneticField/VolumeGeometry/interface/PlanarVolumeBoundary.h", # Includes nonexisent file: MagneticField/MagVolumeGeometry/interface/BoundaryPlane.h

  "DataFormats/SiPixelDigi/interface/PixelDigifwd.h", # Forward delcares a nested class?

  "DataFormats/FEDRawData/interface/DaqData.h", # Completely broken

  "CaloOnlineTools/HcalOnlineDb/interface/LMap.h", #Includes boost/boost::shared_ptr ...

  "RecoEcal/EgammaClusterProducers/interface/PiZeroDiscriminatorProducer.h", # Redefines a symbol
  "DQM/SiStripCommissioningDbClients/interface/SamplingHistosUsingDb.h", #Does inheritance wrong

  "SimTracker/TrackHistory/interface/TrackClassifierByProxy.h", #Uses nonexistent TrackClassifier constructor

  "TrackingTools/GsfTracking/src/DebugHelpers.h", #Broken code?

  "DataFormats/GeometryCommonDetAlgo/interface/DeepCopyPointer.h", # Cycle DataFormats/GeometryCommonDetAlgo - DataFormats/GeometrySurface
  "DataFormats/GeometryCommonDetAlgo/interface/ErrorMatrixTag.h", # Cycle DataFormats/GeometryCommonDetAlgo - DataFormats/GeometrySurface

  "CommonTools/CandAlgos/interface/CloneProducer.h", #Invalid code, funny unique_ptr copying going on...
  "RecoEcal/EgammaClusterAlgos/interface/LogPositionCalc.h", #Uses EcalRecHitData which does no longer exist
  "TrackingTools/GsfTools/src/GaussianStateLessWeight.h", # Redefines class
  "CommonReco/GSFTools/interface/KeepingNonZeroWeightsMerger.h", #Uses template class without template args
  "TrackingTools/GsfTools/interface/LargestWeightsStateMerger.h", #Same as above
  "TrackingTools/GsfTools/interface/MahalanobisDistance.h", #Same as above
  "TrackingTools/GsfTools/interface/MultiTrajectoryStateCombiner.h", #Invalid and obsolete header... DONE

  "PhysicsTools/IsolationUtils/interface/CalIsolationAlgoNoExp.h", # Includes nonexistent stuff
  "PhysicsTools/IsolationAlgos/interface/CalIsolationNoExtrapol.h", #includes above header

  "ElectroWeakAnalysis/ZMuMu/interface/SmoothStepFunction.h", # Ingoring ZMuMu, totally broken
  "ElectroWeakAnalysis/ZMuMu/interface/ZMuMuBack.h", # Ingoring ZMuMu, totally broken
  "ElectroWeakAnalysis/ZMuMu/interface/ZMuMuBackNorm.h", # Ingoring ZMuMu, totally broken
  "ElectroWeakAnalysis/ZMuMu/interface/ZMuMuFunction.h", # Ingoring ZMuMu, totally broken
  "ElectroWeakAnalysis/ZMuMu/interface/ZMuMuNormalBack.h", # Ingoring ZMuMu, totally broken
  "ElectroWeakAnalysis/ZMuMu/interface/ZMuMuScaledFunction.h", # Ingoring ZMuMu, totally broken
  "ElectroWeakAnalysis/ZMuMu/interface/ZMuStandaloneFunction.h", # Ingoring ZMuMu, totally broken
  "ElectroWeakAnalysis/ZMuMu/interface/ZMuStandaloneScaledFunction.h", # Ingoring ZMuMu, totally broken
  "ElectroWeakAnalysis/ZMuMu/interface/ZMuTrackFunction.h", # Ingoring ZMuMu, totally broken
  "ElectroWeakAnalysis/ZMuMu/interface/ZMuTrackScaledFunction.h", # Ingoring ZMuMu, totally broken
  "ElectroWeakAnalysis/ZMuMu/interface/ZMuTrackScaledNormalBack.h", # Ingoring ZMuMu, totally broken

  "DetectorDescription/Core/interface/graph_path.h", # Broken code?
  "RecoTracker/Record/interface/Records.h", # Seems to be broken...
  "CommonTools/UtilAlgos/interface/ChargeSelector.h", # I don't even know. Seems really broken...
  "MagneticField/VolumeGeometry/interface/PlanarVolumeBoundary.h", #REferences unknown classes...
  "PhysicsTools/SelectorUtils/interface/Expressions.h", # Really broken meta-programming going on here...
  "RecoVertex/LinearizationPointFinders/interface/GenericLinearizationPointFinder.h", # Uses template class as a non-template class...
  "CondCore/PopCon/interface/VerifyState.h", # Includes nonexistent TagInfo.h
  "TrackPropagation/RungeKutta/src/RK4PreciseSolver.h", # Includes nonexistent things
  "Alignment/LaserAlignment/interface/LaserHitPairGenerator.h", # Copy constructor doesn't work here
  "Alignment/LaserAlignment/interface/SeedGeneratorForLaserBeams.h", #Uses the header above and isn't used anywhere...
  "MagneticField/VolumeGeometry/interface/MagneticFieldVolume.h", #Also doesn't compile. PositionType isn't define...
  "CondFormats/Calibration/interface/bitObj.h", # Broken. I don't even know... DONE
]
textual_headers = [
  "FWCore/Utilities/src/Guid.h",
  "FWCore/Utilities/interface/Signal.h",
  "FWCore/Framework/src/ProductResolvers.h",
  "FWCore/Framework/src/UnscheduledAuxiliary.h",
  "DataFormats/GeometryVector/interface/Basic3DVectorLD.h", # Different Basic3DVector templates that it depends on here...
  "CondFormats/Serialization/src/SerializationManual.h", #Repeatedly included
  "CondFormats/ESObjects/src/SerializationManual.h", #Repeatedly included
  "CondFormats/PhysicsToolsObjects/src/SerializationManual.h", #Repeatedly included
  "CondFormats/SiPixelObjects/interface/SerializationManual.h", #Repeatedly included
  "CondFormats/SiPixelObjects/src/SerializationManual.h", #Repeatedly included
  "CondFormats/Calibration/src/SerializationManual.h", #Repeatedly included
  "CondFormats/EcalObjects/src/SerializationManual.h", #Repeatedly included
]

# Returns the given text without the given prefix.
def remove_str_prefix(text, prefix):
  return text[len(prefix):] if text.startswith(prefix) else text

def make_module_name(path):
  path = path.replace("/", "_")
  if path.endswith(".h"):
    return path[:-2]
  return path

def handle_package(path):
  path = remove_str_prefix(path, "./")
  d = path
  subpackages = [os.path.join(d, o) for o in os.listdir(d)
                    if os.path.isdir(os.path.join(d,o))]
  subpackages.sort()
  for sub in subpackages:
    interface_dir = os.path.join(sub, "interface")
    found_any_header = False
    modulemap = ""
    modulemap += "module " + make_module_name(sub) + " {\n"
    if os.path.isdir(interface_dir):
      for root, dirnames, filenames in os.walk(interface_dir):
        for filename in filenames:
          header_name = os.path.join(root, filename)
          textual_str = ""
          if header_name in ignored_headers:
            continue
          if header_name in textual_headers:
            textual_str = "textual "
          if header_name.endswith(".h"):
            found_any_header = True
            modulemap += "  module \"" + make_module_name(filename) + "\" { " + textual_str + "header \"" + header_name + "\" export * }\n"
    modulemap += "  export *\n"
    modulemap += "}\n"
    if found_any_header:
      print(modulemap)

def main():
  d = "."
  packages = [os.path.join(d, o) for o in os.listdir(d)
                    if os.path.isdir(os.path.join(d,o))]
  packages.sort()
  for package in packages:
    handle_package(package)

if __name__ == "__main__":
  main()