#############################################################
########## General settings
#############################################################
# flag to be Tested
#cutpass80 = '(( abs(probe_sc_eta) < 0.8 && probe_Ele_nonTrigMVA > %f ) ||  ( abs(probe_sc_eta) > 0.8 && abs(probe_sc_eta) < 1.479&& probe_Ele_nonTrigMVA > %f ) || ( abs(probe_sc_eta) > 1.479 && probe_Ele_nonTrigMVA > %f ) )' % (0.967083,0.929117,0.726311)
#cutpass90 = '(( abs(probe_sc_eta) < 0.8 && probe_Ele_nonTrigMVA > %f ) ||  ( abs(probe_sc_eta) > 0.8 && abs(probe_sc_eta) < 1.479&& probe_Ele_nonTrigMVA > %f ) || ( abs(probe_sc_eta) > 1.479 && probe_Ele_nonTrigMVA > %f ) )' % (0.913286,0.805013,0.358969)


isEB=True
isCSElecVeto=False
# flag to be Tested
flags = {
    'passingElecveto' : 'probe_Pho_csev < 0.5',
    'passinghaspixelseed' : 'probe_Pho_hasPixelSeed > 0.5',
    'passingPresel'   : '(passingPresel   == 1)',
    #'passingIDMVA'   : '((passingPresel   == 1) && (passingIDMVA   == 1))',
    'passingIDMVA'   : '(passingIDMVA   == 1)',
    #'failingIDMVA'   : '((passingPresel   == 1) && (passingIDMVA   == 0))',
    }

if isCSElecVeto:
    if isEB:
        #baseOutDir = 'July1/results_genmatch_Full2017_pt25and35_veto/TnP_SF_passingElecveto_EB'
        baseOutDir = 'July1/results_genmatch_Full2017_pt25and35_veto/TnP_SF_passingElecveto_withPt'
    else:
        baseOutDir = 'July1/results_genmatch_Full2017_pt25and35_veto/TnP_SF_passingElecveto_EE'
else:
    if isEB:
        baseOutDir = 'July1/results_genmatch_2017Full_pt25and35_veto/TnP_SF_passinghaspixelseed_withPt'
    else:
        baseOutDir = 'July1/results_genmatch_2017Full_pt25and35_veto/TnP_SF_passinghaspixelseed_EE'
        
#baseOutDir = 'results_withold2016files/TnP_SF_passingPresel_EE'
#baseOutDir = 'results/TnP_SF_passingIDMVA_EB'

#############################################################
########## samples definition  - preparing the samples
#############################################################
### samples are defined in etc/inputs/tnpSampleDef_Hgg_TnP.py
### not: you can setup another sampleDef File in inputs
import etc.inputs.tnpSampleDef_Hgg_TnP as tnpSamples
tnpTreeDir = 'PhotonToRECO'

samplesDef = {
    #'data'   : tnpSamples.Moriond18_94X['2017data_showershapeCorr'].clone(),
    #'mcNom'  : tnpSamples.Moriond18_94X['2017MC_showershapeCorr_new'].clone(),
    'data'   : tnpSamples.Moriond18_94X['output_data_single_oldpreselectioncut'].clone(),
    'mcNom'  : tnpSamples.Moriond18_94X['output_mc_single_oldpreselectioncut'].clone(),
    #'mcAlt'  : tnpSamples.ICHEP2016['mc_DY_amcatnlo_ele'].clone(),
    'tagSel' : tnpSamples.Moriond18_94X['output_mc_single_oldpreselectioncut'].clone(),
    #'mcAlt'  : tnpSamples.ICHEP2016[''].clone(),
    #'tagSel' : tnpSamples.ICHEP2016[''].clone(),
}
## can add data sample easily
#samplesDef['data'].add_sample( tnpSamples.ICHEP2016['data_2016_runC_ele'] )
#samplesDef['data'].add_sample( tnpSamples.ICHEP2016['data_2016_runD_ele'] )

## some sample-based cuts... general cuts defined here after
## require mcTruth on MC DY samples and additional cuts
## all the samples MUST have different names (i.e. sample.name must be different for all)
## if you need to use 2 times the same sample, then rename the second one
#samplesDef['data'  ].set_cut('run >= 273726')
#if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_mcTruth()
#if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_mcTruth()
#if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_mcTruth()
#if not samplesDef['tagSel'] is None:
#    samplesDef['tagSel'].rename('mcAltSel_DY_madgraph_ele')
#    samplesDef['tagSel'].set_cut('tag_Ele_pt > 33  && tag_Ele_nonTrigMVA > 0.90')

## set MC weight, simple way (use tree weight) 
weightName = 'totWeight'
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
#if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
if not samplesDef['tagSel'] is None:
    samplesDef['tagSel'].set_weight(weightName)
    samplesDef['tagSel'].rename('mcAltSel_DY_madgraph_ele')                                                    
    samplesDef['tagSel'].set_cut('tag_Pho_pt > 43')    
#############################################################
########## bining definition  [can be nD bining]
#############################################################
#for EB
if isEB:
    biningDef = [
        #{ 'var' : 'event_rho' , 'type': 'float', 'bins': [0.0,5.,10.0,15.,20.,25.,30.0,35.0,47.0] },
        #{ 'var' : 'event_nPV' , 'type': 'float', 'bins': [0.0,5.,7.,9.,11.,13.,15.,17.,19.0,23.,27.,31.,35.,39.,45.] },
        { 'var' : 'probe_Pho_pt' , 'type': 'float', 'bins': [20,35,50,75,100,150,200,300,400,500] },
        { 'var' : 'probe_sc_abseta' , 'type': 'float', 'bins': [ 0.0, 1.479,2.5] },
        #{ 'var' : 'probe_Pho_r9' , 'type': 'float', 'bins': [0.0,0.85,1.0] },
        #{ 'var' : 'probe_Pho_r9' , 'type': 'float', 'bins': [0.0,1.0] },
        #{ 'var' : 'probe_sc_abseta' , 'type': 'float', 'bins': [ 0.0, 0.8, 1.4442] },


        ]
else:    
    #for EE
    biningDef = [
        #{ 'var' : 'probe_sc_abseta' , 'type': 'float', 'bins': [ 1.479,2.5] },
        #{ 'var' : 'probe_Pho_r9' , 'type': 'float', 'bins': [0.,0.9,1.0] },
        #{ 'var' : 'event_rho' , 'type': 'float', 'bins': [0.0,5.,10.0,15.,20.,25.,30.0,35.0,47.0] },
        #{ 'var' : 'event_nPV' , 'type': 'float', 'bins': [0.0,5.,7.,9.,11.,13.,15.,17.,19.0,23.,27.,31.,35.,39.,45.] },
        #{ 'var' : 'probe_Pho_r9' , 'type': 'float', 'bins': [0.0,1.0] },
        #{ 'var' : 'probe_sc_abseta' , 'type': 'float', 'bins': [ 1.566, 2.0, 2.5] },
        ]
    
#############################################################
########## Cuts definition for all samples
#############################################################
### cut
#cutBase   ='mass>60.0 && mass<120.0'
#cutBase = '(passingPresel   == 1)'
if isCSElecVeto:
    cutBase = '(passingPresel   == 1) && (tag_Pho_csev < 0.5)'
else:
    cutBase = '(passingPresel   == 1) && (tag_Pho_hasPixelSeed > 0.5)'
# can add addtionnal cuts for some bins (first check bin number using tnpEGM --checkBins)
#additionalCuts = { 
#    0 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#    1 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#    2 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#    3 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#    4 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#    5 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#    6 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#    7 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#    8 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#    9 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45'
#}

#### or remove any additional cut (default)
additionalCuts = None
#additionalCuts = '(tag_Pho_csev < 0.5)'
#additionalCuts = '(tag_Pho_hasPixelSeed > 0.5)'


#############################################################
########## fitting params to tune fit by hand if necessary
#############################################################
tnpParNomFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.5,0.1,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.5,0.1,5.0]",
    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, 0, 1]","peakP[90.0]",
    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, 0, 1]","peakF[90.0]",
    ]

tnpParAltSigFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    "acmsF[60.,50.,75.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",
    ]
     
tnpParAltBkgFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.5,0.1,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.5,0.1,5.0]",
    "alphaP[0.,-5.,5.]",
    "alphaF[0.,-5.,5.]",
    ]
        
