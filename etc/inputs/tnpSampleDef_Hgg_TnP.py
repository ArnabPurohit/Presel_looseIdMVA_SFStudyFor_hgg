from libPython.tnpClassUtils import tnpSample
 
### qll stat
#eosDir1 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/v1/'
#eosDir2 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/v2/'
#eosDirREC = 'eos/cms/store/group/phys_egamma/tnp/80X/RecoSF/RECOSFs_2016/'
#eosWinter17 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/Moriond17_v1/'
#flashggMoriond18 = '/afs/cern.ch/work/a/arpurohi/public/H2gg/May18/CMSSW_9_4_5_cand1/src/flashgg/Validation/test/SF_studies/egm_tnp_analysis/'
#flashggMoriond18 = '/eos/user/a/arpurohi/2017_data_analysis_in2018/'
#flashggMoriond18 = '/eos/user/a/arpurohi/2017_data_analysis_in2018/outputfiles/'
#flashggMoriond18 = '/eos/user/a/arpurohi/TnP_Study_For_SF/July18/'
flashggMoriond18 = '/eos/user/a/arpurohi/2017_data_analysis_in2018/filesforshowershape/'
#flashggMoriond18 = '/eos/user/a/arpurohi/TnPfullDataset2016SingleElectron/PreselectionCutwithPixelMatching/TnPfullDataset2016SingleElectron/'
#/eos/user/a/arpurohi/2017_data_analysis_in2018/output_data_single_oldpreselection_noTagmatch.root
Moriond18_94X = {
    ### MiniAOD TnP for IDs scale factors
  #  'DY_madgraph'          : tnpSample('DY_madgraph',
   #                                    eosMoriond18 + 'mc/TnPTree_DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_all.root',
    #                                   isMC = True, nEvts =  -1 ),
   # 'DY_madgraph_Moriond18' : tnpSample('DY_madgraph_Moriond18', 
    #                                   eosMoriond18 + 'mc/TnPTree_DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_all.root',
    #                                    isMC = True, nEvts =  -1 ),
    'output_mc_single_oldpreselectioncut' : tnpSample('output_mc_single_oldpreselectioncut', 
                                                      #flashggMoriond18 + 'output_mc_single_oldpreselection_noTagmatch.root',
                                                      #flashggMoriond18 + 'TnP_MC_for2017B_withtagmatch.root',
                                                      #flashggMoriond18 + 'TnP_MC_Full2017_withtagmatch_pt25and35.root',
                                                      #flashggMoriond18 + 'TnP_MC_Full2017_tagmatch_pt25and35_veto.root',
                                                      flashggMoriond18 + 'validation_MC_23thSep_wCorr_noDiphotonMVA_tightPresel_ChIsoTag2gev_smearing.root',
                                                      #flashggMoriond18 + 'validation_MC_13Oct_wCorr_tightLowmassPresel_ChIsoTag2gev_smear.root',#Lowmass
                                                      # flashggMoriond18 + 'TnPTree_mc_newID.root',
                                       isMC = True, nEvts =  -1 ),

    #'data_Run2017B' : tnpSample('data_Run2017B' , eosMoriond18 + 'data/TnPTree_17Nov2017_RunB.root' , lumi = 4.891 ),
    #'data_Run2017C' : tnpSample('data_Run2017C' , eosMoriond18 + 'data/TnPTree_17Nov2017_RunC.root' , lumi = 9.9 ),
    #'data_Run2017D' : tnpSample('data_Run2017D' , eosMoriond18 + 'data/TnPTree_17Nov2017_RunD.root' , lumi = 4.36 ),
    #'data_Run2017E' : tnpSample('data_Run2017E' , eosMoriond18 + 'data/TnPTree_17Nov2017_RunE.root' , lumi = 9.53 ),
    #'data_Run2017F' : tnpSample('data_Run2017F' , eosMoriond18 + 'data/TnPTree_17Nov2017_RunF.root' , lumi = 13.96 ),
    'output_data_single_oldpreselectioncut': tnpSample('output_data_single_oldpreselectioncut' ,
                                                       #flashggMoriond18 + 'output_data_single_oldpreselection_noTagmatch.root' ,
                                                       #flashggMoriond18 + 'TnP_data_2017B_withtagmatch.root' ,
                                                       #flashggMoriond18 + 'TnP_data_Full2017_withtagmatch_pt25and35.root' ,
                                                       #flashggMoriond18 + 'TnP_data_Full2017_tagmatch_pt25and35_veto.root' ,
                                                       flashggMoriond18 + 'validation_data_23thSep_wCorr_noDiphotonMVA_TightPresel_ChIsoTag2gev_scale.root' ,
                                                       #flashggMoriond18 + 'validation_data_13Oct_wCorr_tightLowmassPresel_ChIsoTag2gev_scale.root' ,
                                                       #flashggMoriond18 + 'TnPTree_data_newID.root' ,
                                                       lumi = 41.37e+3 ),
                                                       #lumi = 4.794e+3 ),#for 2017B
                                                       #lumi = 9.633e+3 ),#for 2017C
                                                       #lumi = 4.248e+3 ),#for 2017D
                                                       #lumi = 9.315e+3 ),#for 2017E
                                                       #lumi = 13.540e+3 ),#for 2017F
                                                       #lumi = 12.1e+3 ),
    }
