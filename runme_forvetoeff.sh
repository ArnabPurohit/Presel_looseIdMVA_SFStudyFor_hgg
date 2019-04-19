#!/bin/sh
#echo 'Which flag?'
#read flag
#flag=passingElecveto
flag=passinghaspixelseed
echo 'You have chosen '$flag 'flag'
if [ "$flag" == "passingElecveto" ]
then
    #sed -i etc/config/settings_Hgg_VetoEff.py
    python tnpEGM_fitter.py etc/config/settings_Hgg_VetoEff.py --flag passingElecveto --checkBins
    python tnpEGM_fitter.py etc/config/settings_Hgg_VetoEff.py --flag passingElecveto --createBins
    python tnpEGM_fitter.py etc/config/settings_Hgg_VetoEff.py --flag passingElecveto --createHists
    python tnpEGM_fitter.py etc/config/settings_Hgg_VetoEff.py --flag passingElecveto --doFit
    python tnpEGM_fitter.py etc/config/settings_Hgg_VetoEff.py --flag passingElecveto --doFit --mcSig --altSig
    python tnpEGM_fitter.py etc/config/settings_Hgg_VetoEff.py --flag passingElecveto --doFit --altSig
    python tnpEGM_fitter.py etc/config/settings_Hgg_VetoEff.py --flag passingElecveto --doFit  --altBkg
    python tnpEGM_fitter.py etc/config/settings_Hgg_VetoEff.py --flag passingElecveto --sumUp
fi

if [ "$flag" == "passinghaspixelseed" ]
then
    #sed -i etc/config/settings_Hgg_VetoEff.py
    python tnpEGM_fitter.py etc/config/settings_Hgg_VetoEff.py --flag passinghaspixelseed --checkBins
    python tnpEGM_fitter.py etc/config/settings_Hgg_VetoEff.py --flag passinghaspixelseed --createBins
    python tnpEGM_fitter.py etc/config/settings_Hgg_VetoEff.py --flag passinghaspixelseed --createHists
    python tnpEGM_fitter.py etc/config/settings_Hgg_VetoEff.py --flag passinghaspixelseed --doFit
    python tnpEGM_fitter.py etc/config/settings_Hgg_VetoEff.py --flag passinghaspixelseed --doFit --mcSig --altSig
    python tnpEGM_fitter.py etc/config/settings_Hgg_VetoEff.py --flag passinghaspixelseed --doFit --altSig
    python tnpEGM_fitter.py etc/config/settings_Hgg_VetoEff.py --flag passinghaspixelseed --doFit  --altBkg
    python tnpEGM_fitter.py etc/config/settings_Hgg_VetoEff.py --flag passinghaspixelseed --sumUp
fi
