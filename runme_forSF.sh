#!/bin/sh
#echo 'Which flag?'
#read flag
#flag=passingPresel
flag=passingIDMVA
echo 'You have chosen '$flag 'flag'
if [ "$flag" == "passingPresel" ]
then
    #sed -i etc/config/settings_Hgg_TnP.py
    python tnpEGM_fitter.py etc/config/settings_Hgg_TnP.py --flag passingPresel --checkBins
    python tnpEGM_fitter.py etc/config/settings_Hgg_TnP.py --flag passingPresel --createBins
    python tnpEGM_fitter.py etc/config/settings_Hgg_TnP.py --flag passingPresel --createHists
    python tnpEGM_fitter.py etc/config/settings_Hgg_TnP.py --flag passingPresel --doFit
    python tnpEGM_fitter.py etc/config/settings_Hgg_TnP.py --flag passingPresel --doFit --mcSig --altSig
    python tnpEGM_fitter.py etc/config/settings_Hgg_TnP.py --flag passingPresel --doFit --altSig
    python tnpEGM_fitter.py etc/config/settings_Hgg_TnP.py --flag passingPresel --doFit  --altBkg
    python tnpEGM_fitter.py etc/config/settings_Hgg_TnP.py --flag passingPresel --sumUp
fi

if [ "$flag" == "passingIDMVA" ]
then
    #sed -i etc/config/settings_Hgg_TnP.py
    python tnpEGM_fitter.py etc/config/settings_Hgg_TnP.py --flag passingIDMVA --checkBins
    python tnpEGM_fitter.py etc/config/settings_Hgg_TnP.py --flag passingIDMVA --createBins
    python tnpEGM_fitter.py etc/config/settings_Hgg_TnP.py --flag passingIDMVA --createHists
    python tnpEGM_fitter.py etc/config/settings_Hgg_TnP.py --flag passingIDMVA --doFit
    python tnpEGM_fitter.py etc/config/settings_Hgg_TnP.py --flag passingIDMVA --doFit --mcSig --altSig
    python tnpEGM_fitter.py etc/config/settings_Hgg_TnP.py --flag passingIDMVA --doFit --altSig
    python tnpEGM_fitter.py etc/config/settings_Hgg_TnP.py --flag passingIDMVA --doFit  --altBkg
    python tnpEGM_fitter.py etc/config/settings_Hgg_TnP.py --flag passingIDMVA --sumUp
fi
