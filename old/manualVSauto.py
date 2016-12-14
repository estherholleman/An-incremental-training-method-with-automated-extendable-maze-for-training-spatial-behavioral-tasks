# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 11:49:12 2016

@author: esther
"""
# test manual vs automatic scoring

import pandas as pd
import numpy as np



# load in manually scored data
Mdat = pd.read_csv("ManualScores.csv",index_col = ["Phase","Day","Block","Trial"])
Mdat.columns = [u'1', u'2', u'3', u'4']

# load in automatically scored data
Adat = pd.read_csv("AutoData.csv",header=[0,1],index_col = [0,1,2,3], tupleize_cols=False )


#%% Manual Scoring

Mdatsummed = Mdat.sum(axis = 0,level = ["Phase","Day"])
countGroups = Mdat.groupby(level = ["Phase","Day"])
scoresMdat = Mdatsummed/countGroups.count(axis=0) * 100
scoresMdat = scoresMdat.interpolate()




#%% Automatic Scoring
## testing scores without the timed out trials
sides =  Adat.xs('side',level = 1, axis = 1) 

# get animal choices
choices = Adat.xs('animal_answer',level = 1, axis = 1) 
# replace the timed out trials (animal answer = 2) 
choiceNo2 = choices.copy()
choiceNo2[choices == 2] = np.nan

correct = choiceNo2 == sides
summed = correct.sum(axis = 0,level = ["Phase","Day"])
countGroups = choiceNo2.groupby(level = ["Phase","Day"])
scores = summed/countGroups.count(axis=0) * 100




# exclude hints

rewards = Adat.xs('reward_size',level = 1, axis = 1) 
add_reward = Adat.xs('additional_reward',level = 1, axis = 1) 


hints = (rewards < 1) & (add_reward  > 0)


correct = choices == sides
correct = correct * 1

# the count method automatically excludes nans,so this result is currently without the timed out trials (good)
correctNoHints = choiceNo2[~hints] == sides[~hints]
correct = correctNoHints * 1
resultsNoHints = correct.sum(axis = 0,level = ["Phase","Day"])
countGroups = choices[~hints].groupby(level = ["Phase","Day"])
scores = resultsNoHints/countGroups.count(axis=0) * 100



#now would also like to not count the trials noted as nan in the manually scored data..
choiceNoNans = choiceNo2.copy()
mask = pd.isnull(Mdat)
choiceNoNans[mask] = np.nan

# exclude trials manually noted as cancelled and those with hints
correctNoNans = choiceNoNans[~hints] == sides[~hints]
correct = correctNoNans * 1
resultsNoHints = correct.sum(axis = 0,level = ["Phase","Day"])
countGroups = choiceNoNans[~hints].groupby(level = ["Phase","Day"])
scores = resultsNoHints/countGroups.count(axis=0) * 100
# phase 5 day 1 was horrible (system kept crashing, this day is noted as nan (doesn't count))
# interpolate to prevent gap in plot
scores = scores.interpolate()


# exclude trials manually noted as cancelled WITHOUT excluding hints
correctNoNans = choiceNoNans == sides
correct = correctNoNans * 1
resultsNoHints = correct.sum(axis = 0,level = ["Phase","Day"])
countGroups = choiceNoNans.groupby(level = ["Phase","Day"])
scores = resultsNoHints/countGroups.count(axis=0) * 100
# phase 5 day 1 was horrible (system kept crashing, this day is noted as nan (doesn't count))
# interpolate to prevent gap in plot
scores = scores.interpolate()


### problem is that in the first phase almost all trials are with hints...
# should exclude those, only then you can't get a density from them (not enough data points!) and the statistics go a bit wonky
### however, the scoring in the first phase also doesn't work really b/c the rat
# doesn't have to cross the sensors to get to the reward areas.
# though perhaps then it doesn't make sense to make density plots of the first phase, as the reaction times (when present)
# aren't accurate, and are usually caused by the tail. Perhaps in phase 2 this is also the case.

