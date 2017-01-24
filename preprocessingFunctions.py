#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 15:58:39 2016

@author: esther
"""

import pandas as pd
import numpy as np


def loadData():
    
    # load in automatically scored data
    Adat = pd.read_csv("AutoData.csv",header=[0,1],index_col = [0,1,2,3], tupleize_cols=False )
    
    # load in manually scored data (to identify trials manually cancelled/marked as nan)
    Mdat = pd.read_csv("ManualScores.csv",index_col = ["Phase","Day","Block","Trial"])
    Mdat.columns = [u'1', u'2', u'3', u'4']
    
    return Adat, Mdat

    
#%% remove the trials that were manually cancelled during training
def removeCancelledTrials(df, Mdat): 
    mask = pd.isnull(Mdat)
    df[mask] = np.nan
    
    return df    
    
def removeTimedOutTrials(df):
    df[df == 2] = np.nan 

    return df
    
def preProcessChoices(Adat,Mdat):
    
    # extract choices and sides
    sidesRaw =  Adat.xs('side',level = 1, axis = 1) 
    choicesRaw = Adat.xs('animal_answer',level = 1, axis = 1)  

    # replace the timed out trials (animal answer = 2) 
    choicesSansTimedOut = removeTimedOutTrials(choicesRaw)
    
    # do not take the manually skipped trials into account (set as nan)
    choices = removeCancelledTrials(choicesSansTimedOut, Mdat)
    
    #also remove cancelled and timed out trials from sides
    sides = sidesRaw[~np.isnan(choices)]
                     
    return choices, sides

    
    
def loadAndPreProcess():
    Adat,Mdat = loadData()
    choices, sides = preProcessChoices(Adat,Mdat)
    
    return Adat,choices, sides


    
def makeRewards(Adat,Mdat):
    idx = pd.IndexSlice
    Rewards = Adat.loc[idx[:,:,:],idx[:,('reward_size','additional_reward')]].reorder_levels([1,0], axis=1)
    
    MdatIndx = makeExtraColumnIndex(~np.isnan(Mdat), name = 'valid')

    Rewards = Rewards.join(MdatIndx)  
    
    return Rewards

   
def preProcessReactionTimes(Adat, Mdat, lowerThres):
    #%% extract reaction times
    rt = Adat.xs('reaction_time',level = 1, axis = 1)
    # remove manually cancelled trials
    rtnohints = rt[~np.isnan(Mdat)]
    # and remove trials where experimenter gave reward before sensors were activated (0) or sensor activated by tail (anything less than 100ms)
    rtFiltered = rtnohints[rtnohints > lowerThres ]
    
    return rtFiltered
    

# calculate correctness of trials based on reward given and phase
def calcCorrect(df):
        
    phase = df.index.get_level_values(0).unique()[0]
    
    if phase < 2:
        r = 2
    else:
        r = 1
     
    rew = df.xs('reward_size',level = 0, axis = 1) 
    add_rew = df.xs('additional_reward',level = 0, axis = 1)
    valid =  df.xs('valid',level = 0, axis = 1)
    
    correct = (rew[valid] + add_rew[valid]) > r 
    incorrect = (rew[valid] + add_rew[valid]) <= r

    return correct, incorrect, valid

    


def makeExtraColumnIndex(dataframe, name = 'NameMe'):
    
    df = dataframe.copy()
    df['tempIndx'] = name
    df.set_index('tempIndx', append = True, inplace = True)
    df = df.reorder_levels(['tempIndx', 'Phase', 'Day','Block','Trial'])
    df = df.unstack(level=0).reorder_levels([1,0], axis=1)
    
    return df

def makeSideChoices(sides,choices):
    
    sidesIndx   = makeExtraColumnIndex(sides, name = 'side')
    choicesIndx = makeExtraColumnIndex(choices, name = 'choice')
    
    sideChoices = sidesIndx.join(choicesIndx)
   
    return sideChoices    
    
  
# make extra column entries for correct, incorrect, and valid trials    
def makeCorrIncorr(df):
    # mark which trials were correct, incorrect, and valid
    correct, incorrect , valid = calcCorrect(df)
    
    # make an extra column index in prep for concatenation
    correctCol = makeExtraColumnIndex(correct, name = 'correct')
    incorrectCol = makeExtraColumnIndex(incorrect, name = 'incorrect')
    validCol = makeExtraColumnIndex(valid, name = 'valid')
    
    return pd.concat([correctCol, incorrectCol, validCol], axis = 1)

# apply the makeCorrIncorr function to add correctness/validity columns to Rewards    
def makeCorrIncorrPerPhase(Adat,Mdat):
    
    Rewards = makeRewards(Adat,Mdat)             
  
#   Scores = pd.DataFrame(index = rewards.index)
    CorrIncorr = Rewards.groupby(level = "Phase").apply(makeCorrIncorr)

#    Scores.index = Scores.index.droplevel([2,3])

    return CorrIncorr
           
           