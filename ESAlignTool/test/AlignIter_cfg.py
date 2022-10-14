import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_cff import Run3
process = cms.Process("ESAlignmentTool", Run3)
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load("TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAlong_cfi")

###################### Modify following Global tag ################################
## See https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideFrontierConditions
from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, '80X_dataRun2_Prompt_v8', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, '123X_dataRun3_Prompt_v6', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, '124X_dataRun3_Prompt_v4', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, '124X_dataRun3_Prompt_Candidate_2022_08_18_14_11_06', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, '124X_dataRun3_Prompt_Candidate_2022_09_30_12_13_38', '')
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run3_data', '')

process.GlobalTag.toGet = cms.VPSet(
        #cms.PSet(record = cms.string("ESAlignmentRcd"),
        #         tag = cms.string("ES"),
        #         connect = cms.string('sqlite_file:ESAlignments_Run3_2022B_iter11.db')
        #),
        #cms.PSet(record = cms.string("ESAlignmentRcd"),
        #         tag = cms.string("ESAlignment_measured_v01_express"),
        #         connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
        #),
        cms.PSet(record = cms.string("TrackerAlignmentRcd"),
                 tag = cms.string("TrackerAlignment_collisions22_v7"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
        )
)

process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32( 1000 )

## to continue processing events after a ProductNotFound exception
#process.options = cms.untracked.PSet(
#        SkipEvent = cms.untracked.vstring('ProductNotFound')
#)

#------------------------------
# Default Parameter options
#------------------------------
from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing('python')
options.register('IterN', 1,
        VarParsing.multiplicity.singleton,
        VarParsing.varType.int,
        "Alignment iteration number"
        )
options.register('MaxEvents', -1,
        VarParsing.multiplicity.singleton,
        VarParsing.varType.int,
        "Run events max"
        )
options.register('myInputTag', 'default',
        VarParsing.multiplicity.singleton,
        VarParsing.varType.string,
        "Input tag to a group of input files"
        )
options.register('OutFilename', 'AlignmentFile.root',
        VarParsing.multiplicity.singleton,
        VarParsing.varType.string,
        "Output File name"
        )
options.register('JSONFilename', '',
        VarParsing.multiplicity.singleton,
        VarParsing.varType.string,
        "Input JSON"
        )
options.register('Debug', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Debug"
    )
options.register('InputRefitter', True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Input with refit-files"
    )
options.register('DrawMagField', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Draw Magnic Field"
    )
options.register('PrintPosition', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Print Position"
    )
options.register('PrintMatrix', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Print Matrix"
    )
options.register('CalculateESorigin', True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Calulate ES origin from Geometry"
    )
options.register('CalculateESaxes', True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Calulate ES Axes from Geometry"
    )
options.register('StoreDetail', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Store detail branches"
    )
options.register('OverwriteRotationM', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Overwrite Rotation Matrix from Geomatry"
    )
options.register('ReSetRfromOutside', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "ReSet Radio from Outside"
    )
options.register('RecHitLabel', 'ecalPreshowerRecHit:EcalRecHitsES',
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "ES Reco hits label"
    )
options.register('TrackLabel', 'TrackRefitter',
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "Track label"
    )
options.parseArguments()

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.MaxEvents) )

### input
from inputFiles_cfi import * #FileNames 
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(FileNames[options.myInputTag])
)

### output
process.TFileService = cms.Service("TFileService",
    fileName = cms.string(options.OutFilename) 
)

### Check parameters options
if options.InputRefitter == False and options.TrackLabel == 'TrackRefitter':
    print('WARNING: Not using Refit files, options.TrackLabel = generalTracks')
    options.TrackLabel = 'generalTracks' 
print('Load lables:')
print(' options.RecHitLabel = '+options.RecHitLabel)
print(' options.TrackLabel = '+options.TrackLabel)

if options.IterN == 1 and options.OverwriteRotationM == False:
    print('WARNING: First iter, options.OverwriteRotationM = True')
    options.OverwriteRotationM = True

### Input parameters
from AlignmentTool.ESAlignTool.DefaultESLocation_cfi import *  
from inputMatrixElements_cfi import * #MatrixElementsTmp # Modify inputMatrixElements_cfi.py for Matrix Elements 
process.ESAlignmentTool = cms.EDAnalyzer('ESAlignTool',
    RecHitLabel        = cms.InputTag(options.RecHitLabel),
    TrackLabel         = cms.InputTag(options.TrackLabel),
    IterN              = cms.uint32(options.IterN),
    Debug              = cms.bool(options.Debug),
    InputRefitter      = cms.bool(options.InputRefitter),
    DrawMagField       = cms.bool(options.DrawMagField),
    PrintPosition      = cms.bool(options.PrintPosition),
    PrintMatrix        = cms.bool(options.PrintMatrix),
    CalculateESorigin  = cms.bool(options.CalculateESorigin),
    CalculateESaxes    = cms.bool(options.CalculateESaxes),
    OverwriteRotationM = cms.bool(options.OverwriteRotationM),
    StoreDetail        = cms.bool(options.StoreDetail),
    ReSetRfromOutside  = cms.bool(options.ReSetRfromOutside),
    e_xxlimit          = cms.double(1.),
    e_yylimit          = cms.double(1.),
    e_yxlimit          = cms.double(1.),
    winlimit           = cms.double(3.),
    Selected_idee      = cms.uint32(0),
    Selected_RUNmin    = cms.int32(0),
    Selected_RUNmax    = cms.int32(0),
    DefaultESLocation  = DefaultESLocation.clone(),
    MatrixElements     = MatrixElementsTmp.clone(),
)

### Input JSON
if options.JSONFilename != "":
    import FWCore.PythonUtilities.LumiList as LumiList
    process.source.lumisToProcess = LumiList.LumiList(filename=options.JSONFilename).getVLuminosityBlockRange()

process.load("RecoLocalCalo.EcalRecProducers.ecalPreshowerRecHit_cfi") # For ES ALCA RECO dataset
process.p = cms.Path( process.ecalPreshowerRecHit*process.ESAlignmentTool)
