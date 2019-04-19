# Presel_looseIdMVA_SFStudyFor_hgg

How to:

This package takes data MC flat trees as input.
Always start with "source etc/scritps/setup.sh" to setup the environment.
Step 1. Change the name of files in etc/inputs/tnpSampleDef.py
Step 2. Applying additional cuts on Tag and probe, mentioning flag for which efficiency is to be measured and tune intial values of fit parameters all of this can be done with etc/config/settings.py


## The different fitting steps
Everything will be done for a specific flag (so the settings can be the same for different flags). Hence, the flag to be used must be specified each time (named myWP in following).

**1. Create the bining.** To each bin is associated a cut that can be tuned bin by bin in the settings.py
   * After setting up the settings.py check bins 

>   python tnpEGM_fitter.py etc/config/settings.py  --flag myWP --checkBins
   
   * if  you need additinal cuts for some bins (cleaning cuts), tune cuts in the settings.py, then recheck. 
     Once satisfied, create the bining

>   python tnpEGM_fitter.py etc/config/settings.py  --flag myWP --createBins

   * CAUTION: when recreacting bins, the output directory is overwritten! So be sure to not redo that once you are at step2

**2. Create the histograms** with the different cuts... this is the longest step. Histograms will not be re-done later
   
>   python tnpEGM_fitter.py etc/config/settings.py --flag myWP --createHists

**3. Do your first round of fits.**
   * nominal fit
   
>   python tnpEGM_fitter.py etc/config/settings.py --flag myWP --doFit
   
   * MC fit to constrain alternate signal parameters [note this is the only MC fit that makes sense]
   
>   python tnpEGM_fitter.py etc/config/settings.py --flag myWP --doFit --mcSig --altSig

   * Alternate signal fit (using constraints from previous fits)
   
>   python tnpEGM_fitter.py etc/config/settings.py --flag myWP --doFit  --altSig

   * Alternate background fit (using constraints from previous fits)
   
>   python tnpEGM_fitter.py etc/config/settings.py --flag myWP --doFit  --altBkg