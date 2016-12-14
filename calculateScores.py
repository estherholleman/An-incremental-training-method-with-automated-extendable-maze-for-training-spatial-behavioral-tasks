# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 18:56:04 2016

@author: esther
"""


from preprocessingFunctions import loadData
from preprocessingFunctions import preProcessChoices
from scoringFunctions import calcScoresPerDay
from scoringFunctions import manualScoring
from scoringFunctions import scoreChoices
from scoringFunctions import scoreChoicesManualReward
from scoringFunctions import scorePerPhase
from plottingFunctions import plotIt

Adat,Mdat = loadData()
choices,sides = preProcessChoices(Adat,Mdat)

#%% Manual Scoring
ScoresPerDayManual = manualScoring(Mdat)
plotIt(ScoresPerDayManual, title = "Scores Per Day: Manual Scoring", ylabel = "% Correct")

#%% Computer results
#Manual Reward (as recorded by computer)
correct, nTotalTrials = scoreChoicesManualReward(Adat, choices)

#%%Automatic (based on sensors)
validTrials, correct, incorrect, nTotalTrials = scoreChoices(Adat, choices, sides)


ScoresPerDay = calcScoresPerDay(correct, nTotalTrials)

# Plot scores
plotIt(ScoresPerDay, title = "Scores Per Day Based On Sensors", ylabel = "% Correct")

#%% Calculate Scores Per Phase so that 
ScoresPerDay = scorePerPhase(Adat,Mdat)

# Plot scores
plotIt(ScoresPerDay, title = "Scores Per Day Based On Reward Given", ylabel = "% Correct")

