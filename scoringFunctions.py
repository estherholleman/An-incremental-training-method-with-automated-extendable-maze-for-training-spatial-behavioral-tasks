#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 12:16:32 2016

@author: esther
"""
import numpy as np
from preprocessingFunctions import makeRewards
from preprocessingFunctions import calcCorrect


#%%
def manualScoring(Mdat):
     countGroups = Mdat.groupby(level = ["Phase","Day"])
     nTotalTrials = countGroups.count(axis=0)
     summed = Mdat.sum(axis = 0,level = ["Phase","Day"])
     ScoresPerDay = summed/nTotalTrials * 100
     ScoresPerDay[nTotalTrials < 7] = np.nan
     ScoresPerDay = ScoresPerDay.interpolate()
     
     return ScoresPerDay
#%%
def scoreChoices(Adat, choices, sides):
    
    rewards = Adat.xs('reward_size',level = 1, axis = 1) 
    add_reward = Adat.xs('additional_reward',level = 1, axis = 1)    

    # find hints (really only finds hints for incorrect trials in the early phases?)
    hints = (rewards < 1) & (add_reward  == 1)
    
    validTrials = ~np.isnan(choices[~hints])

    # calculate correct and incorrect
    correct = choices[~hints] == sides[~hints]
    incorrect = choices[~hints] != sides[~hints] 
    
    countGroups = choices[validTrials].groupby(level = ["Phase","Day"])
    nTotalTrials = countGroups.count(axis=0)
    
    return validTrials, correct, incorrect, nTotalTrials
    
#%%
def scoreChoicesManualReward(Adat, choices):
    
    rewards = Adat.xs('reward_size',level = 1, axis = 1) 
    add_reward = Adat.xs('additional_reward',level = 1, axis = 1)    
    
    hints = (rewards < 1) & (add_reward  == 1)
    
    #calculate correct and incorrect  
    correct = (rewards + add_reward) > 1 
    correct = correct[~np.isnan(choices) & ~hints]
                      
    incorrect = (rewards + add_reward) < 1
    incorrect = incorrect[~np.isnan(choices)]
  
    countGroups = correct.groupby(level = ["Phase","Day"])
    nTotalTrials = countGroups.count(axis=0)
    
    return correct, incorrect, nTotalTrials

#%%
def calcScoresPerDay(correct, nTotalTrials):
    
    correctSummed = correct.sum(axis = 0,level = ["Phase","Day"])
    
    ScoresPerDay = correctSummed/nTotalTrials * 100
    
    ScoresPerDay[nTotalTrials < 7] = np.nan
    
    ScoresPerDay = ScoresPerDay.interpolate()
    
    return ScoresPerDay
    


#%%
def scoring(df):

    correct, _ , valid = calcCorrect(df)
    summed = correct.sum(axis = 0, level = ["Phase","Day"])
    countGroups = correct[valid].groupby(level = ["Phase","Day"])
    nTotalTrials = countGroups.count(axis=0)
    
    scores = summed/nTotalTrials * 100
    scores[nTotalTrials < 7] = np.nan
    
    return scores
    
    
#%%
def scorePerPhase(Adat,Mdat):
    
    Rewards = makeRewards(Adat,Mdat)             
  
#   Scores = pd.DataFrame(index = rewards.index)
    Scores = Rewards.groupby(level =  ["Phase","Day"]).apply(scoring)
    Scores = Scores.interpolate()
    
    Scores.index = Scores.index.droplevel([2,3])
    
    
    return Scores
    
    