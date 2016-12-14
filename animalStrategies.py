# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 13:28:51 2016

@author: esther
"""

# detect strategies in animals choices


import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#import numpy as np
from myFunctions import testSimpleStrategies



# load in manually scored data
Mdat = pd.read_csv("ManualScores.csv",index_col = ["Phase","Day","Block","Trial"])

# load in automatically scored data
Adat = pd.read_csv("AutoData.csv",header=[0,1],index_col = [0,1,2,3], tupleize_cols=False )




# get animal choices
choices = Adat.xs('animal_answer',level = 1, axis = 1) 
# replace the timed out trials (animal answer = 2) 
choices[choices == 2] = np.nan


## testing scores without the timed out trials
sides =  Adat.xs('side',level = 1, axis = 1) 

# this just drops the entire row (all animals) if one of the animals timed out
choiceDropTest = choices.dropna()

correct = choiceDropTest == sides[~np.isnan(choices)].dropna()
summed = correct.sum(axis = 0,level = ["Phase","Day"])
countGroups = correct.groupby(level = ["Phase","Day"])
scores = summed/countGroups.count(axis=0) * 100



# an attempt at getting all animals (columns) seperately
rat1 = choices["1"][~np.isnan(choices["1"])] == sides["1"][~np.isnan(choices["1"])]
rat2 = choices["2"][~np.isnan(choices["2"])] == sides["2"][~np.isnan(choices["2"])]
rat3 = choices["3"][~np.isnan(choices["3"])] == sides["3"][~np.isnan(choices["3"])]
rat4 = choices["4"][~np.isnan(choices["4"])] == sides["4"][~np.isnan(choices["4"])]

rat1Summed = rat1.sum(axis = 0,level = ["Phase","Day"])
countGroups = rat1.groupby(level = ["Phase","Day"])
rat1Scores = rat1Summed/countGroups.count(axis=0) * 100

rat2Summed = rat2.sum(axis = 0,level = ["Phase","Day"])
countGroups = rat2.groupby(level = ["Phase","Day"])
rat2Scores = rat2Summed/countGroups.count(axis=0) * 100

rat3Summed = rat3.sum(axis = 0,level = ["Phase","Day"])
countGroups = rat3.groupby(level = ["Phase","Day"])
rat3Scores = rat3Summed/countGroups.count(axis=0) * 100

rat4Summed = rat4.sum(axis = 0,level = ["Phase","Day"])
countGroups = rat4.groupby(level = ["Phase","Day"])
rat4Scores = rat4Summed/countGroups.count(axis=0) * 100





correct = choices == sides
results = correct.sum(axis = 0,level = ["Phase","Day"])
countGroups = choices.groupby(level = ["Phase","Day"])
scores = results/countGroups.count(axis=0) * 100
# the count method automatically excludes nans,so this result is currently without the timed out trials
#now would also like to not count the trials noted as nan in the manually scored data..

# not working yet, why?
choices[np.isnan(Mdat)] = np.nan

# and exclude hints again?

rewards = Adat.xs('reward_size',level = 1, axis = 1) 
add_reward = Adat.xs('additional_reward',level = 1, axis = 1) 


hints = (rewards < 1) & (add_reward  > 0)


correct = choices == sides
correct = correct * 1


correctNoHints = choices[~hints] == sides[~hints]
correct = correctNoHints * 1
resultsNoHints = correct.sum(axis = 0,level = ["Phase","Day"])
countGroups = correct.groupby(level = ["Phase","Day"])
scores = resultsNoHints/countGroups.count(axis=0) * 100



simpleStrategiesOnChoices = choices.groupby(level = ["Phase", "Day", "Block"]).apply(testSimpleStrategies).unstack()
simpleStrategiesOnChoices.columns.names = ['Strategies','Animal']






#grp1 = choicesGrouped.get_group((1,1,1))






def testSimpleStrategies(group):
    
    nTrials = len(group)
    
    ## this doesn't really work, just comparing these strategies isn't accurate,
    # it doesn't say much about the relationship between the different trials
    # the transitions between trials. Need to find another way to test that
    
    # always alternates
    alt0 = (group == ([0,1] * nTrials)[:nTrials]).sum() / nTrials * 100
    alt1 = (group == ([1,0] * nTrials)[:nTrials]).sum() / nTrials * 100
    
    # always chooses the same side
    pref0 = (group  == ([0] * nTrials)[:nTrials]).sum() / nTrials * 100
    pref1 = (group ==  ([1] * nTrials)[:nTrials]).sum() / nTrials * 100
    
    # several different possible patterns
    alt2x0 = (group == ([0,0,1] * nTrials)[:nTrials]).sum() / nTrials * 100
    alt2x1 = (group ==([1,1,0] * nTrials)[:nTrials]).sum() / nTrials * 100
    
    alt2x02x1 = (group ==([0,0,1,1] * nTrials)[:nTrials]).sum() / nTrials * 100
    alt2x12x1 = (group ==([1,1,0,0] * nTrials)[:nTrials]).sum() / nTrials * 100
    
    alt3x0 = (group ==([0,0,0,1] * nTrials)[:nTrials]).sum()/ nTrials * 100
    alt3x1 = (group ==([1,1,1,0] * nTrials)[:nTrials]).sum() / nTrials * 100
    
    alt3x02x1 = (group ==([0,0,0,1,1] * nTrials)[:nTrials]).sum() / nTrials * 100
    alt3x12x1 = (group ==([1,1,1,0,0] * nTrials)[:nTrials]).sum() / nTrials * 100
    
    return pd.DataFrame({'alt0': alt0, 'alt1': alt1, 'pref0': pref0, 'pref1': pref1, 'alt2x0': alt2x0, 'alt2x1': alt2x1, 'alt2x02x1': alt2x02x1, 'alt2x12x1': alt2x12x1, 'alt3x0': alt3x0, 'alt3x1': alt3x1, 'alt3x02x1': alt3x02x1, 'alt3x12x1': alt3x12x1})
    
    
    



#alternating0 = strategiesOnChoices.xs('alt0',level = 0, axis = 1)
#alt0avg = alternating0.mean(level = ["Phase", "Day"])

# or all at once for quick testingL
((simpleStrategiesOnChoices.xs('alt2x0',level = 0, axis = 1)).mean(level = ["Phase", "Day"])).plot()


# could also consider studying the difference between the animals choices (diff) to detect alternation, or the diff of the diff (to detect going to the same place twice before alternating, etc)?






