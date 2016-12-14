#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 15:58:39 2016

@author: esther
"""

import pandas as pd
import numpy as np
from myFunctions import makeExtraColumnIndex


def loadData():
    
    # load in automatically scored data
    Adat = pd.read_csv("AutoData.csv",header=[0,1],index_col = [0,1,2,3], tupleize_cols=False )
    
    # load in manually scored data (to identify trials manually cancelled/marked as nan)
    Mdat = pd.read_csv("ManualScores.csv",index_col = ["Phase","Day","Block","Trial"])
    Mdat.columns = [u'1', u'2', u'3', u'4']
    
    return Adat, Mdat




def preProcessChoices(Adat,Mdat):
    
    # extract choices and sides
    sides =  Adat.xs('side',level = 1, axis = 1) 
    choiceRaw = Adat.xs('animal_answer',level = 1, axis = 1)  

    # replace the timed out trials (animal answer = 2) 
    choicesNo2 = choiceRaw.copy()
    choicesNo2[choiceRaw == 2] = np.nan   
    # now also do not count the manually skipped trials (set as nan)
    choices = choicesNo2.copy()
    mask = pd.isnull(Mdat)
    choices[mask] = np.nan
    
    return choices, sides

    
    
def loadAndPreProcess():
    Adat,Mdat = loadData()
    choices, sides = preProcessChoices(Adat,Mdat)
    
    return Adat,choices, sides
    


   
def preProcessReactionTimes(Adat, validTrials):
    #%% extract reaction times
    rt = Adat.xs('reaction_time',level = 1, axis = 1)
    # remove hints and cancelled trials
    #rtnohints = rt[validTrials]
    # and remove trials where experimenter gave reward before sensors were activated (0) or sensor activated by tail (anything less than 100ms)
    rtFiltered = rt[rt > 100 ]
    
    return rtFiltered
    

def makeRewards(Adat,Mdat):
    idx = pd.IndexSlice
    Rewards = Adat.loc[idx[:,:,:],idx[:,('reward_size','additional_reward')]].reorder_levels([1,0], axis=1)
    
    MdatIndx = makeExtraColumnIndex(~np.isnan(Mdat), name = 'valid')

    Rewards = Rewards.join(MdatIndx)  
    
    return Rewards

    
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

    
def makeCorrIncorr(df):
    # mark which trials were correct, incorrect, and valid
    correct, incorrect , valid = calcCorrect(df)
    
    # make an extra column index in prep for concatenation
    correctCol = makeExtraColumnIndex(correct, name = 'correct')
    incorrectCol = makeExtraColumnIndex(incorrect, name = 'incorrect')
    validCol = makeExtraColumnIndex(valid, name = 'valid')
    
    return pd.concat([correctCol, incorrectCol, validCol], axis = 1)

    
def makeCorrIncorrPerPhase(Adat,Mdat):
    
    Rewards = makeRewards(Adat,Mdat)             
  
#   Scores = pd.DataFrame(index = rewards.index)
    CorrIncorr = Rewards.groupby(level = "Phase").apply(makeCorrIncorr)

#    Scores.index = Scores.index.droplevel([2,3])

    return CorrIncorr
           
           