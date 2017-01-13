# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 10:02:31 2016

@author: esther
"""
import numpy as np
from myFunctions import loadData
from myFunctions import preProcessChoices
from myFunctions import scoreChoices

from preProcessingFunctions import preProcessReactionTimes

from plottingFunctions import plotIt

Adat,Mdat = loadData()
choices,sides = preProcessChoices(Adat,Mdat)
validTrials, correct, incorrect, nTotalTrials = scoreChoices(Adat, choices, sides)


def getStats(Adat, validTrials, correct):
    
    rt = preProcessReactionTimes(Adat, validTrials)
    rtSel = rt[correct] 
    return rtSel.groupby(level = ["Phase","Day"]).aggregate([np.median,np.mean, np.std])
    



statsCorrect = getStats(Adat,validTrials,correct)

medianCorrect = statsCorrect.xs("median", level = 1, axis = 1)
meanCorrect = statsCorrect.xs("mean", level = 1, axis = 1)

plotIt(medianCorrect.interpolate(), title = "Medians Correct Reaction Times")
plotIt(meanCorrect.interpolate(), title = "Average Correct Reaction Times")


statsIncorrect = getStats(Adat,validTrials,incorrect)

medianIncorrect = statsIncorrect.xs("median", level = 1, axis = 1)
meanIncorrect = statsIncorrect.xs("mean", level = 1, axis = 1)

plotIt(medianIncorrect.interpolate(), title = "Medians Incorrect Reaction Times")
plotIt(meanIncorrect.interpolate(), title = "Average Incorrect Reaction Times")

