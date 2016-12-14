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
from myFunctions import removeCancelledTrials
from myFunctions import scoreChoices
from preprocessingFunctions import preProcessReactionTimes


#%% LOAD IN DATA
Adat,Mdat = loadData()


#%% PREPROCESS DATA (get sides and choices)
choices, sides = preProcessChoices(Adat, Mdat)

choices = removeCancelledTrials(choices, Mdat)


#%% Determine incorrect and correct trials
validTrials, correct, incorrect, nTotalTrials = scoreChoices(Adat, choices, sides)

rewards = Adat.xs('reward_size',level = 1, axis = 1) 
add_reward = Adat.xs('additional_reward',level = 1, axis = 1) 

hints = (rewards < 1) & (add_reward  == 1)



validTrials1 = ~np.isnan(choices[~hints])
rt = preProcessReactionTimes(Adat, validTrials1)

validTrials2 = choices[~hints]
rt = preProcessReactionTimes(Adat, validTrials2)

validTrials3 = ~np.isnan(choices)
rt = preProcessReactionTimes(Adat, validTrials3)




modesCorrect, modesIncorrect = computeDensityPerPhase(rt, correct, incorrect)