# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 15:15:59 2016

@author: esther
"""

from random import randint
import numpy as np
from scipy.stats import gaussian_kde
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# calculate densities over blocks for all phases together
def computeDensityPerBlock(Adat, scores, animal = 1):
    
    cor = ["Correct","Incorrect"]
    rt = Adat.xs('reaction_time',level = 1, axis = 1) 
    #hints = (Adat[animal].reward_size < 1) & (Adat[animal].additional_reward > 0)
    phases = rt.index.get_level_values(0).unique()
    
    sensScore = scores*1
    
    # divide data into groups per phase
    blockGrouped =rt.groupby(level = ["Phase","Block"])
    sensScoreGrouped = sensScore.groupby(level = ["Phase","Block"])
    
    f, axarr = plt.subplots(len(phases),2, figsize = (15,22))

    c = 0
    
    for corr in cor:
        
        
        for b,block in blockGrouped:
            
            # select reaction times for block
           rtBlock = blockGrouped.get_group(b)
           sensScoreBlock = sensScoreGrouped.get_group(b)

           if corr == 'Incorrect':
               sensScoreBlock = ~ sensScoreBlock
               c = 1
               
           # compute density
           density = computeDensity(rtBlock[animal][(rtBlock[animal] > 4) & sensScoreBlock[animal] ])
           
           ## prepare plot
           # make x-axis
           xs = np.linspace(0,8000,100)
           title = corr + " Trials: Reaction Time Distribution Per Phase for Animal " +  animal
           #figname = "ReactionTimeDensities_" + corr + "Trials_Rat" + animal
           
           phase = rtBlock.index.get_level_values(0).unique()[0]
           
           ## plot density
           axarr[phase-1,c].plot(xs,density(xs), label = "block " + str(b))
           axarr[phase-1,c].set_title(title)
           axarr[phase-1,c].set_xlabel("Reaction Time (ms)")
           axarr[phase-1,c].set_ylabel("Density")    
           plt.subplots_adjust(hspace = 0.7)
#       






def computeDensityPerBlock(Adat, scores, animal = 1, correct = True):
    
    if correct:
        sensScore =  scores*1
        c = 1
    else:
        sensScore = ~scores*1
        c = 2
    
    
    rt = Adat.xs('reaction_time',level = 1, axis = 1) 
    #hints = (Adat[animal].reward_size < 1) & (Adat[animal].additional_reward > 0)
        
    # divide data into groups per phase
    phaseGrouped = rt.groupby(level = ["Phase"])
    senseScoreGrouped = sensScore.groupby(level = ["Phase"])


    # create figure for subplots
    f, axarr = plt.subplots(len(phaseGrouped),2)
    
    p = 0
    
    for phase, score in zip(phaseGrouped,senseScoreGrouped):
        print phase
        #print score
        
        if correct:
            title = "Correct Trials Phase " + str(p) + ": Reaction Time Distribution Per Block for Animal " +  animal
            figname = "ReactionTimeDensitiesPerBlockCorrectTrials_Rat" + animal
        else:
            title = "Incorrect Trials Phase " + str(p) + ": Reaction Time Distribution Per Block for Animal " +  animal
            figname = "ReactionTimeDensitiesPerBlockIncorrectTrials_Rat" + animal
        
        
        blockGrouped = phase.groupby(level = ["Block"])
        senseScoreGrouped = score.groupby(level = ["Block"])
        
        b = 1
        
        for block, sense in zip(blockGrouped,senseScoreGrouped):      
        
#            # select block
#            rtBlock = blockGrouped.get_group(b)
#            sensScoreBlock = sensScoreGrouped.get_group(b)
               
            # make x-axis
            xs = np.linspace(0,8000,100)
            # compute density
            density = computeDensity(block[animal][(block[animal] > 4) & sense[animal] ])
               
            # plot density
            axarr[p+1,c].plot(xs,density(xs), label = "phase " + str(b))
            axarr[p+1,c].set_title(title)
            axarr[p+1,c].set_xlabel("Reaction Time (ms)")
            axarr[p+1,c].set_ylabel("Density")
            
            b = b + 1
      
        p = p + 1
       
    plt.savefig(figname,format = "eps")
    plt.savefig(figname,format = "png")







def computeDensityPerBlock2(Adat, scores, animal = 1, correct = True):
    
    if correct:
        sensScore =  scores*1
        c = 1
    else:
        sensScore = ~scores*1
        c = 2
    
    
    rt = Adat.xs('reaction_time',level = 1, axis = 1) 
    #hints = (Adat[animal].reward_size < 1) & (Adat[animal].additional_reward > 0)
    
    # divide data into groups per phase
    phaseGrouped = rt.groupby(level = ["Phase"])   
    blockGrouped = rt.groupby(level = ["Phase","Block"])
    senseScoreGrouped = sensScore.groupby(level = ["Phase","Block"])


    # create figure for subplots
    f, axarr = plt.subplots(len(phaseGrouped),2)
        
    for p,phase in phaseGrouped:
             
        if correct:
            title = "Correct Trials Phase " + str(p) + ": Reaction Time Distribution Per Block for Animal " +  animal
            figname = "ReactionTimeDensitiesPerBlockCorrectTrials_Rat" + animal
        else:
            title = "Incorrect Trials Phase " + str(p) + ": Reaction Time Distribution Per Block for Animal " +  animal
            figname = "ReactionTimeDensitiesPerBlockIncorrectTrials_Rat" + animal
            
        for b, block in blockGrouped:
      
    #       select block
            rtBlock = blockGrouped.get_group((p,b))
            senseScoreBlock = senseScoreGrouped.get_group((p,b))
               
            # make x-axis
            xs = np.linspace(0,8000,100)
            # compute density
            density = computeDensity(rtBlock[animal][(rtBlock[animal] > 4) & senseScoreBlock[animal] ])
               
            # plot density
            axarr[p+1,c].plot(xs,density(xs), label = "phase " + str(b))
            axarr[p+1,c].set_title(title)
            axarr[p+1,c].set_xlabel("Reaction Time (ms)")
            axarr[p+1,c].set_ylabel("Density")
             
#    plt.savefig(figname,format = "eps")
#    plt.savefig(figname,format = "png")
        































def computeDensityPerBlock(Adat, scores, animal = 1, correct = True):
    
    if correct:
        sensScore =  scores*1
        c = 1
    else:
        sensScore = ~scores*1
        c = 2
    
    
    rt = Adat.xs('reaction_time',level = 1, axis = 1) 
    #hints = (Adat[animal].reward_size < 1) & (Adat[animal].additional_reward > 0)
        
    # divide data into groups per phase
    phaseGrouped = rt.groupby(level = ["Phase"])   
    blockGrouped = rt.groupby(level = ["Phase","Block"])
    senseScoreGrouped = sensScore.groupby(level = ["Phase","Block"])
    
    for b, block in blockGrouped:
        
        f, axarr = plt.subplots(len(phaseGrouped),2)
        


        if correct:
            title = "Correct Trials Phase " + str(p) + ": Reaction Time Distribution Per Block for Animal " +  animal
            figname = "ReactionTimeDensitiesPerBlockCorrectTrials_Rat" + animal
        else:
            title = "Incorrect Trials Phase " + str(p) + ": Reaction Time Distribution Per Block for Animal " +  animal
            figname = "ReactionTimeDensitiesPerBlockIncorrectTrials_Rat" + animal

#       select block
        rtBlock = blockGrouped.get_group((p,b))
        senseScoreBlock = senseScoreGrouped.get_group((p,b))
           
        # make x-axis
        xs = np.linspace(0,8000,100)
        # compute density
        density = computeDensity(rtBlock[animal][(rtBlock[animal] > 4) & senseScoreBlock[animal] ])
           
        # plot density
        axarr[p+1,c].plot(xs,density(xs), label = "phase " + str(b))
        axarr[p+1,c].set_title(title)
        axarr[p+1,c].set_xlabel("Reaction Time (ms)")
        axarr[p+1,c].set_ylabel("Density")


