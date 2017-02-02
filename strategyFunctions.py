#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 13:48:37 2017

@author: esther
"""

import pandas as pd


def simulate_winstay(df):  
   
   winStay = pd.DataFrame()
   
   for i, row in df.iterrows():
        
        currentChoice = row['choice']
        incorrect = currentChoice[currentChoice != row['side']]
        
        # predict what the rat would do in the next trial if using win-stay strategy
        # by default choose the same side next
        winStayNxt = currentChoice
        # except if the current trial was incorrect, then switch sides
        winStayNxt[incorrect.index] = [1-t for t in incorrect]
        winStay = winStay.append(winStayNxt)
  
   return winStay

   
   
def simulate_winshift(df):  
   
   winShift = pd.DataFrame()
   
   for i, row in df.iterrows():
        
        currentChoice = row['choice']
        correct = currentChoice[currentChoice == row['side']]
        
        # predict what the rat would do in the next trial if using win-shift strategy
        # by default choose the same side next
        winShiftNxt = currentChoice
        # except if the current trial was correct, then switch sides
        winShiftNxt[correct.index] = [1-t for t in correct]
        winShift = winShift.append(winShiftNxt)
  
   return winShift
    

def simulate_alternation(df):  
   
   alt = pd.DataFrame()
   
   for i, row in df.iterrows():
        
        nxtChoice = row['choice']
        nxtChoice[nxtChoice.index] = [1-t for t in nxtChoice]
        alt = alt.append([nxtChoice])
  
   return alt  
   
   
   
def simulateStrategies(sideChoices):   
## Giving the argument sideChoices (where sides is the side in the randomization 
## actually given to the animal in the experiment, and choices are the actual choices
## made by the animal during the experiment) means the function will take the animals
## choice for the previous trial and respond as a rat using a particular strategy would
## in the same situation (for each trial independently). 
## This is a useful approach when wanting to score how close the animals actual responses
## were to a strategy response in the same situation, on a per trial basis. That is, 
## if the animal decided half way through the block to start applying a certain strategy
## it will be visible with this analysis (whereas if the entire block is predetermined 
## according to a strategy layed out at the beginning of the block the animal would have
## to have been applying the specific strategy for the entire block in order for it to 
## be evident/show up in the results). 
  
    WinStay = sideChoices.groupby(level =  ["Phase","Day","Block"]).apply(simulate_winstay)
    WinShift = sideChoices.groupby(level =  ["Phase","Day","Block"]).apply(simulate_winshift)
    Alt = sideChoices.groupby(level =  ["Phase","Day","Block"]).apply(simulate_alternation)

    # the first row needs to be nan's (no prev choices to base next choice on, and all the rows
    # should be shifted down one (the prediction was for the next choice, based on the current trial)
    # in this process the last row should be/is deleted
    WinStay  = WinStay.shift(1)
    WinShift = WinShift.shift(1)
    Alt = Alt.shift(1)
    # to get the win shift strategy reverse the win-stay answers
    ### have left this out for now as I'm not sure if it actually calculates correctly, 
    ### will do it the more laborious way instead)
    ### yet even with this adjustment the second peak in win-stay remains...
    #WinShift = 1 - WinStay
    
    return WinStay, WinShift, Alt
    
    
#def calcNormStrategyScores(stratPerTrial,sides,choices):
#    
#    ## count the number of times the animal applied the strategy
#    nStratAnimal = stratPerTrial.groupby(level =  ["Phase","Day","Block"]).sum()
#    # put this one here too? sidesFilt = sides[~np.isnan(choices)] 
#                                      
#    ## number of times the randomization alterates
#    # first take the trials that were cancelled out so they're not counted
#    sidesFilt = sides[~np.isnan(choices)]
#    # how is this counting the alternations in sides (it now appears to simply be summing up the amount of times the side is right.. (1))
#    nStratRand = sidesFilt.groupby(level =  ["Phase","Day","Block"]).sum()
#    
#    #%% calculate normalized alternation score based on the number of alternations the animal did compared to the n alternations in the randomization
#    normAltScoreBlock = nAltsAnimal/nAltsRand
#    normAltScore = normAltScoreBlock.groupby(level =["Phase","Day"]).mean()
#    normAltScore = normAltScore.interpolate()

   
