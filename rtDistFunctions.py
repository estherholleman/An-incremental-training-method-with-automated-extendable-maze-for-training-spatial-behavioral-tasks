#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 13:39:16 2017

@author: esther
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
from __future__ import division




# Estimate probability density function through kernel density (gaussian_kde)
def computeDensity(data, covar_factor = 0.20):
    density = gaussian_kde(data)
    # determine bandwidth (of smoothing)
    density.covariance_factor = lambda : covar_factor
    density._compute_covariance()
    return density


def computeDensityPerPhase(rt, correct, incorrect, figname = "ReactionTimeDensities", mode = True):
    print("testing!")
    cor = ["Correct","Incorrect"]
    animals = ["1","2","3","4"]
    modesCorrect = pd.DataFrame(np.nan, columns = animals, index = range(1,8))
    modesIncorrect = pd.DataFrame(np.nan, columns = animals, index = range(1,8))

    # divide data into groups per phase
    phaseGrouped =rt.groupby(level = "Phase")
    
    f, axarr = plt.subplots(len(phaseGrouped),2, figsize = (15,22))
    
    for corr in cor:    
    
        if corr == 'Correct':
            sensScoreGrouped = correct.groupby(level = "Phase")
            c = 0
        else:
            sensScoreGrouped = incorrect.groupby(level = "Phase")
            c = 1
    
        for p,phase in phaseGrouped:
           
           # select phase
           rtPhase = phaseGrouped.get_group(p)
           sensScorePhase = sensScoreGrouped.get_group(p)
           
     
            # make x-axis
           xs = np.linspace(0,8000,100)
    #        # compute density
           
           
           for animal in animals:
               
               sel = ~np.isnan(rtPhase[animal]) & sensScorePhase[animal]
               rtAnimal = rtPhase[animal][sel]
               nTrials = len(rtAnimal)
               
               if nTrials < 5: continue
                   
               density = computeDensity(rtAnimal)
                  
               title = corr + " Trials Phase " + str(p)
               
               ## plot density
               axarr[p-1,c].plot(xs,density(xs)/0.2, label = "Rat " + animal + ", n = " + str(nTrials))
               axarr[p-1,c].set_title(title)
               axarr[p-1,c].set_xlabel("Reaction Time (ms)")
               axarr[p-1,c].set_ylabel("Density") 
               axarr[p-1,c].legend()
               axarr[p-1,c].set_ylim([0,0.0015])
	       print("testing!")

               
               if mode:
                   pdf = density.pdf(xs);    
                   mostcommon = xs[pdf == max(pdf)]
                   axarr[p-1,c].plot((mostcommon, mostcommon), (0, max(pdf)), 'k--')
                   if corr == 'Correct':
                       modesCorrect.iloc[p-1,int(animal)-1] = mostcommon
                   else:
                       modesIncorrect.iloc[p-1,int(animal)-1] = mostcommon
                                        
          
               plt.subplots_adjust(hspace = 0.7)
               plt.suptitle(figname, fontsize = 18)

    if mode:    
        figname = figname + '_Mode'
       
#    plt.savefig(figname + ".eps",format = "eps")
#    plt.savefig(figname + ".png",format = "png")

#    return modesCorrect, modesIncorrect


def computeDensityPerPhaseCorrIncorr(rt, CorrIncorr, figname = "ReactionTimeDensities", mode = True):
    
    cor = ["Correct","Incorrect"]
    animals = ["1","2","3","4"]
    modesCorrect = pd.DataFrame(np.nan, columns = animals, index = range(1,8))
    modesIncorrect = pd.DataFrame(np.nan, columns = animals, index = range(1,8))

    # divide data into groups per phase
    phaseGrouped =rt.groupby(level = "Phase")
    
    f, axarr = plt.subplots(len(phaseGrouped),2, figsize = (15,22))
    
    CorrValid = CorrIncorr['correct'] & CorrIncorr['valid']
    IncorrValid = CorrIncorr['incorrect'] & CorrIncorr['valid']
    
    
    for corr in cor:    
    
        if corr == 'Correct':
            sensScoreGrouped = CorrValid.groupby(level = "Phase")
            c = 0
        else:
            sensScoreGrouped = IncorrValid.groupby(level = "Phase")
            c = 1
    
        for p,phase in phaseGrouped:
           
           # select phase
           rtPhase = phaseGrouped.get_group(p)
           sensScorePhase = sensScoreGrouped.get_group(p)
           
     
            # make x-axis
           xs = np.linspace(0,8000,100)
    #        # compute density
           
           
           for animal in animals:
               
               sel = ~np.isnan(rtPhase[animal]) & sensScorePhase[animal]
               rtAnimal = rtPhase[animal][sel]
               nTrials = len(rtAnimal)
               
               if nTrials < 5: continue
                   
               density = computeDensity(rtAnimal)
                  
               title = corr + " Trials Phase " + str(p)
               
               ## plot density
               axarr[p-1,c].plot(xs,density(xs), label = "Rat " + animal + ", n = " + str(nTrials))
               axarr[p-1,c].set_title(title)
               axarr[p-1,c].set_xlabel("Reaction Time (ms)")
               axarr[p-1,c].set_ylabel("Density") 
               axarr[p-1,c].legend()
               
               if mode:
                   pdf = density.pdf(xs);    
                   mostcommon = xs[pdf == max(pdf)]
                   axarr[p-1,c].plot((mostcommon, mostcommon), (0, max(pdf)), 'k--')
                   if corr == 'Correct':
                       modesCorrect.iloc[p-1,int(animal)-1] = mostcommon
                   else:
                       modesIncorrect.iloc[p-1,int(animal)-1] = mostcommon
                                        
          
               plt.subplots_adjust(hspace = 0.7)
               plt.suptitle(figname, fontsize = 18)

    if mode:    
        figname = figname + '_Mode'
       
#    plt.savefig(figname + ".eps",format = "eps")
#    plt.savefig(figname + ".png",format = "png")

    return modesCorrect, modesIncorrect    
    
    
    
    
    
def computeDensityPerBlock(Adat, correct, incorrect, animal = "1", mode = True):
    
    cor = ["Correct","Incorrect"]
    rt = Adat.xs('reaction_time',level = 1, axis = 1) 
    #hints = (Adat[animal].reward_size < 1) & (Adat[animal].additional_reward > 0)
    phases = rt.index.get_level_values(0).unique()
        
    # divide data into groups per phase
    blockGrouped =rt.groupby(level = ["Phase","Block"])
    
    f, axarr = plt.subplots(len(phases),2, figsize = (15,22))

    
    for corr in cor:
        if corr == 'Correct':
            sensScoreGrouped = correct.groupby(level = ["Phase","Block"])
            c = 0
        else:
            sensScoreGrouped = incorrect.groupby(level = ["Phase","Block"])
            c = 1
        
        
        for b,block in blockGrouped:
            
            # select reaction times for block
           rtBlock = blockGrouped.get_group(b)
           sensScoreBlock = sensScoreGrouped.get_group(b)
         
           rtAnimal = rtBlock[animal][(rtBlock[animal] > 4) & sensScoreBlock[animal]] 
           nTrials = len(rtAnimal)                       
           
           if nTrials < 2: continue
               
           # compute density
           density = computeDensity(rtAnimal)
           
           phase = rtBlock.index.get_level_values(0).unique()[0]
           
           ## prepare plot
           # make x-axis
           xs = np.linspace(0,8000,100)
           title = corr + " Trials, Phase" + str(phase) + ": Reaction Time Distribution for Rat " +  animal           
           #figname = "ReactionTimeDensities_" + corr + "Trials_Rat" + animal
           ## plot density
           axarr[phase-1,c].plot(xs,density(xs), label = "block " + str(b[1]) + ", n= " + str(nTrials))
           axarr[phase-1,c].set_title(title)
           axarr[phase-1,c].set_xlabel("Reaction Time (ms)")
           axarr[phase-1,c].set_ylabel("Density")  
           axarr[phase-1,c].legend()

           if mode:
               pdf = density.pdf(xs);    
               mostcommon = xs[pdf == max(pdf)]
               axarr[phase-1,c].plot((mostcommon, mostcommon), (0, max(pdf)), 'k--')           

           plt.subplots_adjust(hspace = 0.7)
#   
    figname = "ReactionTimeDensitiesBlocks_Rat" + animal     
           
    if mode:    
        figname = figname + '_Mode'           
           
    plt.savefig(figname + ".eps",format = "eps")
    plt.savefig(figname + ".png",format = "png")

    
    
    
    

def computeDensityForStrategy(rt, strategyApplied, strategyNotApplied, figname = "ReactionTimeDensitiesForStrategy", mode = True):
    
    cor = ["strategyApplied","strategyNotApplied"]
    animals = ["1","2","3","4"]
    modesCorrect = pd.DataFrame(np.nan, columns = animals, index = range(1,8))
    modesIncorrect = pd.DataFrame(np.nan, columns = animals, index = range(1,8))

    # divide data into groups per phase
    phaseGrouped =rt.groupby(level = "Phase")
    
    f, axarr = plt.subplots(len(phaseGrouped),2, figsize = (15,22))
    
    for corr in cor:    
    
        if corr == 'strategyApplied':
            sensScoreGrouped = strategyApplied.groupby(level = "Phase")
            c = 0
        else:
            sensScoreGrouped = strategyNotApplied.groupby(level = "Phase")
            c = 1
    
        for p,phase in phaseGrouped:
           
           # select phase
           rtPhase = phaseGrouped.get_group(p)
           sensScorePhase = sensScoreGrouped.get_group(p)
           
     
            # make x-axis
           xs = np.linspace(0,8000,100)
    #        # compute density
           
           
           for animal in animals:
               
               sel = ~np.isnan(rtPhase[animal]) & sensScorePhase[animal]
               rtAnimal = rtPhase[animal][sel]
               nTrials = len(rtAnimal)
               
               if nTrials < 5: continue
                   
               density = computeDensity(rtAnimal)
                  
               title = corr + " Trials Phase " + str(p)
               
               ## plot density
               axarr[p-1,c].plot(xs,density(xs), label = "Rat " + animal + ", n = " + str(nTrials))
               axarr[p-1,c].set_title(title)
               axarr[p-1,c].set_xlabel("Reaction Time (ms)")
               axarr[p-1,c].set_ylabel("Density") 
               axarr[p-1,c].legend()
               
               if mode:
                   pdf = density.pdf(xs);    
                   mostcommon = xs[pdf == max(pdf)]
                   axarr[p-1,c].plot((mostcommon, mostcommon), (0, max(pdf)), 'k--')
                   if corr == 'Correct':
                       modesCorrect.iloc[p-1,int(animal)-1] = mostcommon
                   else:
                       modesIncorrect.iloc[p-1,int(animal)-1] = mostcommon
                                        
          
               plt.subplots_adjust(hspace = 0.7)
               plt.suptitle(figname, fontsize = 18)

#    if mode:    
#        figname = figname + '_Mode'
#       
#    plt.savefig(figname + ".eps",format = "eps")
#    plt.savefig(figname + ".png",format = "png")

#    return modesCorrect, modesIncorrect    
