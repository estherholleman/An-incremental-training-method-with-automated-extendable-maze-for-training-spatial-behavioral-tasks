# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 17:20:56 2016

@author: esther
"""
import numpy as np
import pandas as pd
from myFunctions import computeDensity
import matplotlib.pyplot as plt


# load in manually scored data
Mdat = pd.read_csv("ManualScores.csv",index_col = ["Phase","Day","Block","Trial"])
Mdat.columns = [u'1', u'2', u'3', u'4']

# load in automatically scored data
Adat = pd.read_csv("AutoData.csv",header=[0,1],index_col = [0,1,2,3], tupleize_cols=False )


rt = Adat.xs('reaction_time',level = 1, axis = 1) 
xs = np.linspace(0,8000,100)
animal = "1"
phase = 1

#%% Automatic Scoring
## testing scores without the timed out trials
sides =  Adat.xs('side',level = 1, axis = 1) 

# get animal choices
choices = Adat.xs('animal_answer',level = 1, axis = 1) 
# replace the timed out trials (animal answer = 2) 
choiceNo2 = choices.copy()
choiceNo2[choices == 2] = np.nan


#now would also like to not count the trials noted as nan in the manually scored data..
choiceNoNans = choiceNo2.copy()
mask = pd.isnull(Mdat)
choiceNoNans[mask] = np.nan


# find hints
rewards = Adat.xs('reward_size',level = 1, axis = 1) 
add_reward = Adat.xs('additional_reward',level = 1, axis = 1) 


hints = (rewards < 1) & (add_reward  > 0)

# exclude trials manually noted as cancelled and those with hints
correctNoNans = choiceNoNans[~hints] == sides[~hints]
correct = correctNoNans * 1
sensScore = correct

phaseGrouped =rt.groupby(level = "Phase")
sensScoreGrouped = sensScore.groupby(level = "Phase")
 
rtPhase = phaseGrouped.get_group(phase)
sensScorePhase = sensScoreGrouped.get_group(phase)   

density = computeDensity(rtPhase[animal][(rtPhase[animal] > 4) & sensScorePhase[animal] ])

pdf = density.pdf(xs);


mostcommon = xs[pdf == max(pdf)]

plt.plot(xs,density(xs))
plt.plot((mostcommon, mostcommon), (0, max(pdf)), 'k--')
plt.show()