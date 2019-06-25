#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 14:59:27 2017

@author: esther
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def computeIntegral(rt, correct, incorrect, figname = "Integral Comparison"):
    
    cor = ["Correct","Incorrect"]
    animals = ["1","2","3","4"]
    integralsCorrect = pd.DataFrame(np.nan, columns = animals, index = range(1,8))
    integralsIncorrect = pd.DataFrame(np.nan, columns = animals, index = range(1,8))
    
    Xbins = range(0,5000)

    # divide data into groups per phase
    phaseGrouped =rt.groupby(level = "Phase")
    
#    f, axarr = plt.subplots(len(phaseGrouped),2, figsize = (15,22))
    
    for corr in cor:    
    
        if corr == 'Correct':
            sensScoreGrouped = correct.groupby(level = "Phase")
            #c = 0
        else:
            sensScoreGrouped = incorrect.groupby(level = "Phase")
            #c = 1
    
        for p,phase in phaseGrouped:
           
           # select phase
           rtPhase = phaseGrouped.get_group(p)
           sensScorePhase = sensScoreGrouped.get_group(p)
           
     
            # make x-axis
           #xs = np.linspace(0,8000,100)
    #        # compute density
           
           
           for animal in animals:
               
               sel = ~np.isnan(rtPhase[animal]) & sensScorePhase[animal]
               rtAnimal = rtPhase[animal][sel]
               nTrials = len(rtAnimal)
               
               if nTrials < 5: continue
           
               countRtAnimal, bins, ignore = plt.hist(rtAnimal, Xbins, histtype='step')
               
               integral = np.trapz(countRtAnimal, Xbins[:-1])
                  
               #title = corr + " Trials Phase " + str(p)
               
               ## plot density
#               axarr[p-1,c].plot.hist(integral, xs, label = "Rat " + animal + ", n = " + str(nTrials))
#               axarr[p-1,c].set_title(title)
#               axarr[p-1,c].set_xlabel("Reaction Time (ms)")
#               axarr[p-1,c].set_ylabel("Density") 
#               axarr[p-1,c].legend()
#               axarr[p-1,c].set_ylim([0,0.0015])
               

               if corr == 'Correct':
                   integralsCorrect.iloc[p-1,int(animal)-1] = integral
               else:
                   integralsIncorrect.iloc[p-1,int(animal)-1] = integral
                                        
          
    integrals = pd.concat([integralsCorrect,integralsIncorrect], axis = 1, keys =['correct','incorrect'])
#        plt.subplots_adjust(hspace = 0.7)
#        plt.suptitle(figname, fontsize = 18)
    return integrals