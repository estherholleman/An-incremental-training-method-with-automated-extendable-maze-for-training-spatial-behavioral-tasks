#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 12:19:32 2017

@author: esther
"""
import pandas as pd
from preprocessingFunctions import makeRewards




def calcCorrectRT(df, r = 2, p = 1):
        
    phase = df.index.get_level_values(0).unique()[0]
    
    if phase > p:
        r = r - 1
     
    rew = df.xs('reward_size',level = 0, axis = 1) 
    add_rew = df.xs('additional_reward',level = 0, axis = 1)
    valid =  df.xs('valid',level = 0, axis = 1)
    
    correct = (rew[valid] + add_rew[valid]) > r 
    incorrect = (rew[valid] + add_rew[valid]) <= r

    return pd.concat([correct,incorrect], axis = 1, keys =['correct','incorrect'])
    
def testRTbasedOnPhaseScoring(Adat,Mdat):
    
    Rewards = makeRewards(Adat,Mdat)   

    masks = Rewards.groupby(level =  ["Phase","Day"]).apply(calcCorrectRT)
    
    # extract reaction times
    rt = Adat.xs('reaction_time',level = 1, axis = 1)
    rtFiltered = rt[rt > 200 ]
    
    return rtFiltered, masks.correct, masks.incorrect
     