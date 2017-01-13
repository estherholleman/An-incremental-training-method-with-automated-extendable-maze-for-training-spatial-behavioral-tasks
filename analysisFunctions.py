#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 12:19:32 2017

@author: esther
"""

from preprocessingFunctions import makeRewards
from preprocessingFunctions import calcCorrect



def testRTbasedOnPhaseScoring(Adat,Mdat):
    
    Rewards = makeRewards(Adat,Mdat)   
    
    correct, incorrect, valid = calcCorrect(Rewards)
    
    # extract reaction times
    rt = Adat.xs('reaction_time',level = 1, axis = 1)
    
    # and remove trials where experimenter gave reward before sensors were activated (0) 
    # or sensor activated by tail (anything less than 200ms)
    # That is, take only those trials with reaction times longer than 200ms
    rtFiltered = rt[rt > 200 ]
    
    return rtFiltered,correct,incorrect,valid
     