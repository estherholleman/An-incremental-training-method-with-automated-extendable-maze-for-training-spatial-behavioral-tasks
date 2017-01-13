#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 11:45:18 2017

@author: esther
"""
from preprocessingFunctions import loadData
from preprocessingFunctions import makeRewards
from preprocessingFunctions import calcCorrect

from myFunctions import computeDensityPerPhase


def TestRTbasedOnPhaseScoring():
    Adat,Mdat = loadData()
    
    Rewards = makeRewards(Adat,Mdat)   
    
    correct, incorrect, valid = calcCorrect(Rewards)
    
    # extract reaction times
    rt = Adat.xs('reaction_time',level = 1, axis = 1)
    
    # and remove trials where experimenter gave reward before sensors were activated (0) 
    # or sensor activated by tail (anything less than 200ms)
    # That is, take only those trials with reaction times longer than 200ms
    rtFiltered = rt[rt > 200 ]
    
    modesCorrect, modesIncorrect = computeDensityPerPhase(rtFiltered, correct, incorrect)

