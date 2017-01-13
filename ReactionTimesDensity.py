# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 14:26:08 2016

@author: esther
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
from myFunctions import computeDensity


# load in manually scored data
Mdat = pd.read_csv("ManualScores.csv",index_col = ["Phase","Day","Block","Trial"])

# load in automatically scored data
Adat = pd.read_csv("AutoData.csv",header=[0,1],index_col = [0,1,2,3], tupleize_cols=False )


# make dataframe of reaction times for each rat
#RT = Adat.loc[:, Adat.columns.get_level_values(1) == 'reaction_time']
##drop reaction_time column labels
#RT.columns = RT.columns.droplevel(level = 1)

# make dataframe of reaction times for each rat (use lowercase Variable explorer doesn't like uppercase apparently!)
rt = Adat.xs('reaction_time',level = 1, axis = 1) 

# compute the density for rat 1, 2, 3, or 4 
computeDensity(rt["2"][(rt["2"] > 4) & (~np.isnan(Mdat["Rat2"]))] )

# compute the density of the reaction times for correct trials
computeDensity(rt["2"][(rt["2"] > 4) & (Mdat["Rat2"] == 1) ] )


# compute reaction time density for trials taking hints into consideration
# find when a hint was given
hints = (Adat["2"].reward_size < 1) & (Adat["2"].additional_reward > 0)

# density of correct trials without hints
computeDensity(rt["2"][(rt["2"] > 4) & (Mdat["Rat2"] == 1)  & ~hints ] )

# density of correct trials with hints
computeDensity(rt["2"][(rt["2"] > 4) & (Mdat["Rat2"] == 1)  & hints ] )

# compute the density of the reaction times for incorrect trials
computeDensity(rt["2"][(rt["2"] > 4) & (Mdat["Rat2"] == 0) ] )



# reaction time density for corrrect trials, per phase
computeDensity(rt["2"][(rt["2"] > 4) & (Mdat["Rat2"] == 1) ] )

#AllScoresSummed = AllScoresWithIndx.sum(axis = 0,level = ["Phase","Day"])
phaseGroups =rt.groupby(level = "Phase")

phase1 = phaseGroups.get_group(1)
computeDensity(phase1["2"][(phase1["2"] > 4)])

#OR:
phaseGroups.aggregate(computeDensity)









# give string as animal (eg "2")
def computeDensityPerPhase(Adat, Mdat, animal, correct = True):
    
    
    rt = Adat.xs('reaction_time',level = 1, axis = 1) 
    #hints = (Adat[animal].reward_size < 1) & (Adat[animal].additional_reward > 0)
    
    if correct:     
        sensScore = (Adat[animal].side == Adat[animal].animal_answer) | (Adat[animal].additional_reward > 2) 
        title = "Correct Trials: Reaction Time Distribution Per Phase for Animal " +  animal
    else:
        sensScore = Adat[animal].side != Adat[animal].animal_answer 
        title = "Incorrect Trials: Reaction Time Distribution Per Phase for Animal " +  animal
    
    # divide data into groups per phase
    phaseGrouped =rt.groupby(level = "Phase")
    #scoreGrouped = Mdat.groupby(level = "Phase")  
    #hintsGrouped = hints.groupby(level = "Phase")
    sensScoreGrouped = sensScore.groupby(level = "Phase")
    
    for p, phase in phaseGrouped:
       
       # select phase
       rtPhase = phaseGrouped.get_group(p)
       #scoresPhase = scoreGrouped.get_group(p)
       #hintsPhase = hintsGrouped.get_group(p)
       sensScorePhase = sensScoreGrouped.get_group(p)
       
        # make x-axis
       xs = np.linspace(0,8000,100)
#        # compute density
       #density = computeDensity(rtPhase[animal][(rtPhase[animal] > 4) & (scoresPhase["Rat"+ animal] == 0 ) & ~hintsPhase ])
       density = computeDensity(rtPhase[animal][(rtPhase[animal] > 4) & sensScorePhase ])
       
       # plot density
       plt.plot(xs,density(xs), label = "phase " + str(p))
       plt.title(title)
       plt.legend()



