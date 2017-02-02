#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 12:16:32 2016

@author: esther
"""
import numpy as np
from preprocessingFunctions import makeRewards
#from preprocessingFunctions import calcCorrect


#%%
def manualScoring(Mdat):
     countGroups = Mdat.groupby(level = ["Phase","Day"])
     nTotalTrials = countGroups.count()
     summed = Mdat.sum(axis = 0,level = ["Phase","Day"])
     ScoresPerDay = summed/nTotalTrials * 100
     ScoresPerDay[nTotalTrials < 7] = np.nan
     ScoresPerDay = ScoresPerDay.interpolate()
     
     return ScoresPerDay

     
#%% Raw scores (score choices without filters)     
def scoreChoicesUnfiltered(choices, sides):

    # calculate correct and incorrect
    correct = choices == sides
    incorrect = choices == 1 - sides
    # previous version choices =! sides counts nans as incorrect!
    # which isn't a problem for scoring as the corrects arent affected (if choices
    # and sides are both nan, then it gives a false, so not correct), however, when
    # using incorrect to filter the reaction times this might cause a problem
    
    countGroups = choices.groupby(level = ["Phase","Day"])
    nTotalTrials = countGroups.count()
    
    return correct, incorrect, nTotalTrials  
     
     
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

#%% calculate correctness of trials based on reward given and phase
def calcCorrect(df, r = 2, p = 1):
        
    phase = df.index.get_level_values(0).unique()[0]
    
    if phase > p:
        r = r - 1
     
    rew = df.xs('reward_size',level = 0, axis = 1) 
    add_rew = df.xs('additional_reward',level = 0, axis = 1)
    valid =  df.xs('valid',level = 0, axis = 1)
    
    correct = (rew[valid] + add_rew[valid]) > r 
    incorrect = (rew[valid] + add_rew[valid]) <= r

    return correct, incorrect, valid
    
    
#%%
def calcScoresPerDay(correct, nTotalTrials, minTrials = 7):
    
    correctSummed = correct.sum(axis = 0,level = ["Phase","Day"])
    
    ScoresPerDay = correctSummed/nTotalTrials * 100
    
    ScoresPerDay[nTotalTrials < minTrials] = np.nan
    
    ScoresPerDay = ScoresPerDay.interpolate()
    
    return ScoresPerDay
    
#%%
def calcScoresPerPhase(correct, nTotalTrials):
    
    correctSummed = correct.sum(axis = 0,level = ["Phase"] )
    
    ScoresPerPhase = correctSummed/nTotalTrials.sum(level = ["Phase"]) * 100
    
    return ScoresPerPhase


#%%
def scoring(df,rewPhaseThres):

    correct, _ , valid = calcCorrect(df, **rewPhaseThres)
    summed = correct.sum(axis = 0, level = ["Phase","Day"])
    countGroups = correct[valid].groupby(level = ["Phase","Day"])
    nTotalTrials = countGroups.count()
    
    scores = summed/nTotalTrials * 100
    scores[nTotalTrials < 7] = np.nan
    
    return scores
    
    
#%%
def scorePerPhase(Adat,Mdat,rewPhaseThres):
    # rewPhaseThres should be a dict  {'r': 2, 'p': 1}
    #make rewards dataframe that also includes columns that mark trials as valid based on manually cancelled trials (marked as nan in mdat)
    Rewards = makeRewards(Adat,Mdat)             
  
#   Scores = pd.DataFrame(index = rewards.index)
    Scores = Rewards.groupby(level =  ["Phase","Day"]).apply(scoring, *(rewPhaseThres,))
    Scores = Scores.interpolate()
    
    Scores.index = Scores.index.droplevel([2,3])
    
    
    return Scores
    

def scoreStrategy(df, sides):
    
    correct, incorrect, nTotalTrials = scoreChoicesUnfiltered(df,sides)
    scores = calcScoresPerDay(correct, nTotalTrials, minTrials = 15)
    
    return scores
    
    
    
def calcNormStratScores(stratSim,sides,choices):
    # calculate scores on strategy for animal
    stratScoreAnimal = scoreStrategy(stratSim,choices)
    
    # calculate scores on strategy for randomization
    stratScoreRand = scoreStrategy(stratSim,sides)
    
    normStratScore = stratScoreAnimal/stratScoreRand
    
    return stratScoreAnimal, stratScoreRand, normStratScore
    
    