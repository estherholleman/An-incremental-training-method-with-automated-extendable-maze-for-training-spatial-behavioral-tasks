#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 18:01:54 2017

@author: esther
"""

import seaborn as sns
tips = sns.load_dataset("tips")
import os
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

os.chdir('/home/esther/Desktop/BehavioralTraining/code')

from preprocessingFunctions import loadData
from preprocessingFunctions import preProcessChoices
from preprocessingFunctions import preProcessReactionTimes
from preprocessingFunctions import makeSideChoices

from scoringFunctions import scoreChoices
from scoringFunctions import scoreChoicesUnfiltered
from scoringFunctions import scorePerPhase

from analysisFunctions import testRTbasedOnPhaseScoring

from rtDistFunctions import computeDensityPerPhase

from plottingFunctions import plotIt

os.chdir('/home/esther/Desktop/BehavioralTraining')

#%% LOAD IN DATA
Adat,Mdat = loadData()

#%% PREPROCESS DATA (get sides and choices)
choices, sides = preProcessChoices(Adat, Mdat)
# LOAD IN REACTION TIMES AND REMOVE CANCELLED AND TIMED OUT TRIALS
rt_raw = Adat.xs('reaction_time',level = 1, axis = 1)
#rtChoicesFilter = rt_raw[~np.isnan(choices)] # shouldn't need to do this as reaction times are masked by correct and incorrect (Which are already filtered)
rt = rt_raw[rt_raw > 100] # only include trials where researcher did not give reward before sensors were activated

correct, incorrect, nTotalTrials = scoreChoicesUnfiltered(choices, sides)
idx = pd.IndexSlice
cor = rt[correct].loc[idx[5:7]]
incor = rt[incorrect].loc[idx[5:7]]

cor2 = pd.DataFrame(cor.stack())
incor2 = pd.DataFrame(incor.stack())

cor2['corincor'] = 'correct'
incor2['corincor'] = 'incorrect'

cor2.reset_index(inplace=True)
incor2.reset_index(inplace=True)


cor2.columns = ['Phase','Day','Block','Trial','Animal','reaction_time','CorrectOrNot']
incor2.columns = ['Phase','Day','Block','Trial','Animal','reaction_time','CorrectOrNot']

reactionTimes = pd.merge(cor2,incor2, on=['Phase','Day','Block','Trial','Animal','reaction_time','CorrectOrNot'], how='outer')

ax = sns.violinplot(x="Phase", y="reaction_time", hue="CorrectOrNot", data=reactionTimes, split=True, inner="quart")
ax.set_title("Reaction Time Distributions Over Phases")