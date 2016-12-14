# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:06:45 2016

@author: esther
"""

#import pandas as pd
import numpy as np

from myFunctions import computeDensityPerPhase
from myFunctions import loadData
from myFunctions import preProcessChoices
from myFunctions import scoreChoices
from myFunctions import analyseWinStay
from myFunctions import makeSideChoices
from myFunctions import removeCancelledTrials
from myFunctions import calcScoresPerDay
from myFunctions import calcScoresPerPhase
from plottingFunctions import plotIt
from preprocessingFunctions import preProcessReactionTimes


#%% LOAD IN DATA
Adat,Mdat = loadData()


#%% PREPROCESS DATA (get sides and choices)
choices, sides = preProcessChoices(Adat, Mdat)

choices = removeCancelledTrials(choices, Mdat)


#%% Determine incorrect and correct trials
validTrials, correct, incorrect, nTotalTrials = scoreChoices(Adat, choices, sides)

#%% GET FILTERED REACTION TIMES
rt = preProcessReactionTimes(Adat, validTrials)

#%% Compute density for correct and incorrect trials
modesCorrect, modesIncorrect = computeDensityPerPhase(rt, correct, incorrect)


#%% FIND ALTERNATIONS
Diffs = abs(choices.groupby(level =  ["Phase","Day","Block"]).diff(periods = 1, axis = 0))



#%% GET REACTION TIMES OF TRIALS WHERE THE RAT ALTERNATED
altMask = Diffs == True # keep in mind this will set the nan's to false also (but since here I'm only looking at trials where alternation is true (not summing) that's exactly what I want)
computeDensityPerPhase(rt, correct[altMask] == True , incorrect[altMask] == True, figname = "ReactionTimeDensitiesAlternationTrials")


#%% join dataframes to feed into simulation loop
sideChoices = makeSideChoices(sides,choices)


#%% ANALYSE TRIALS FOR WIN STAY AND WIN SHIFT STRATEGIES
WinStay, WinShift = analyseWinStay(sideChoices)




#%% WIN STAY SCORES
WinStayScoreDay = calcScoresPerDay(WinStay, nTotalTrials)
WinStayScorePhase = calcScoresPerPhase(WinStay, nTotalTrials)
WinStayScorePhase.mean(axis = 1).plot()

#%% WIN SHIFT SCORES
WinShiftScoreDay = calcScoresPerDay(WinShift, nTotalTrials)
WinShiftScorePhase = calcScoresPerPhase(WinShift, nTotalTrials)
WinShiftScorePhase.mean(axis = 1).plot()


#%% GET REACTION TIMES OF TRIALS WHERE THE RAT USED A WIN-STAY STRATEGY
winStayMask = WinStay == True
winStayRTall = rt[winStayMask]
winStayRTcorrect = rt[winStayMask & correct]
winStayRTincorrect = rt[winStayMask & incorrect]

winStayRTStats = winStayRTall.groupby(level = ["Phase","Day"]).aggregate([np.median,np.mean, np.std])
winStayRTStats = winStayRTStats.interpolate()

medianWinStayRT = winStayRTStats.xs("median", level = 1, axis = 1)
meanWinStayRT = winStayRTStats.xs("mean", level = 1, axis = 1)

winStayRTcorrectStats = winStayRTcorrect.groupby(level = "Phase").aggregate([np.median,np.mean, np.std])
medianWinStayRTcorrect = winStayRTcorrectStats.xs("median", level = 1, axis = 1)
meanWinStayRTcorrect = winStayRTcorrectStats.xs("mean", level = 1, axis = 1)


plotIt(medianWinStayRT, title = "Medians Win Stay Reaction Times")
plotIt(meanWinStayRT, title = "Average Win Stay Reaction Times")

#%% GET REACTION TIMES OF TRIALS WHERE THE RAT USED A WIN-STAY STRATEGY
winShiftMask = WinShift == True

winShiftRTall = rt[winShiftMask]
winShiftRTcorrect = rt[winShiftMask & correct]
winShiftRTincorrect = rt[winShiftMask & incorrect]

winShiftRTStats = winShiftRTall.groupby(level = ["Phase","Day"]).aggregate([np.median,np.mean, np.std])
winShiftRTStats = winShiftRTStats.interpolate()

medianWinShiftRT = winShiftRTStats.xs("median", level = 1, axis = 1)
meanWinShiftRT = winShiftRTStats.xs("mean", level = 1, axis = 1)

meanWinShiftRT.mean(axis = 1).plot()

winShiftRTcorrectStats = winShiftRTcorrect.groupby(level = "Phase").aggregate([np.median,np.mean, np.std])
medianWinShiftRTcorrect = winShiftRTcorrectStats.xs("median", level = 1, axis = 1)
meanWinShiftRTcorrect = winShiftRTcorrectStats.xs("mean", level = 1, axis = 1)

plotIt(medianWinShiftRT, title = "Medians Win Shift Reaction Times")
plotIt(meanWinShiftRT, title = "Average Win Shift Reaction Times")


#%% DENSITY OF WIN STAY REACTION TIMES
computeDensityPerPhase(rt, correct[winStayMask] == True , incorrect[winStayMask] == True, figname = "ReactionTimeDensitiesWinStayTrials")


#%% GET REACTION TIMES OF TRIALS WHERE THE RAT USED A WIN-SHIFT STRATEGY
winShiftMask = WinShift == True 
computeDensityPerPhase(rt, correct[winShiftMask] == True , incorrect[winShiftMask] == True, figname = "ReactionTimeDensitiesWinShiftTrials")


#%% ANALYZE ALTERNATIONS
## count the number of times the animal alternates
nAltsAnimal = Diffs.groupby(level =  ["Phase","Day","Block"]).sum()

## number of times the randomization alterates
# first take the trials that were cancelled out so they're not counted
sidesFilt = sides[~np.isnan(choices)]
nAltsRand = sidesFilt.groupby(level =  ["Phase","Day","Block"]).sum()

#%% calculate normalized alternation score based on the number of alternations the animal did compared to the n alternations in the randomization
normAltScoreBlock = nAltsAnimal/nAltsRand
normAltScore = normAltScoreBlock.groupby(level =["Phase","Day"]).mean()
normAltScore = normAltScore.interpolate()
##%% calculate average alternation score per phase
#normAltScoreAvgPerPhase = normAltScore.groupby(level ="Phase").mean()
#
## take average over animals to see global trends
#normAltScorePhaseAvg = normAltScoreAvgPerPhase.mean(axis = 1)
#
##%% calculate average alternation score per day
#normAltScoreAvgPerDay = normAltScore.groupby(level =["Phase","Day"]).mean()


plotIt(normAltScore, "Normalized Alternation Scores", Norm = True )
