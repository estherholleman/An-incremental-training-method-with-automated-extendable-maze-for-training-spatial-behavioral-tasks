#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 15:54:41 2016

@author: esther
"""

#%% Testing valid trials

import numpy as np

from myFunctions import loadData
from myFunctions import preProcessChoices
from myFunctions import scoreChoices
from myFunctions import computeDensityPerPhase
from preprocessingFunctions import preProcessReactionTimes



#%% LOAD IN DATA
Adat,Mdat = loadData()


#%% PREPROCESS DATA (get sides and choices)
choices, sides = preProcessChoices(Adat, Mdat)


#%% Determine incorrect and correct trials
#validTrials, correct, incorrect, nTotalTrials = scoreChoices(Adat, choices, sides)


#%% score choices by hand to test filters (such as removal of hints and nans)
rewards = Adat.xs('reward_size',level = 1, axis = 1) 
add_reward = Adat.xs('additional_reward',level = 1, axis = 1) 

hints = (rewards < 1) & (add_reward  == 1)

#%% determine correct and incorrect
correct = choices[~hints] == sides[~hints]
incorrect = choices[~hints] != sides[~hints] 

    
    
validTrials1 = ~np.isnan(choices[~hints])
rt1 = preProcessReactionTimes(Adat, validTrials1)

validTrials2 = choices[~hints]
rt2 = preProcessReactionTimes(Adat, validTrials2)

validTrials3 = ~np.isnan(choices)
rt3 = preProcessReactionTimes(Adat, validTrials3)


rtFiltered = rt1[rt1 > 100 ]

#%% compute density
modesCorrect, modesIncorrect = computeDensityPerPhase(rtFiltered, correct, incorrect)
