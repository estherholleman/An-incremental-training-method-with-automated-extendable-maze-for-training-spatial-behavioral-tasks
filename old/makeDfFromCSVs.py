# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 13:00:10 2016

@author: esther
"""

import pandas as pd
from myFunctions import unpackCSVs

# get dataframe with raw data from CSVs
frame = unpackCSVs()

#%% prepare dataframe for manipulations
indexes = ["Animal","Phase","Day","Block","trial_nr"]

for indx in indexes:   
    frame[indx] = frame[indx].astype(int)

# set animal to trial_nr columns as multi-index
df  = frame.set_index(indexes,drop = True)

df.drop('aditional_info', axis=1, inplace=True)
df['side'] = df['flavour'].combine_first(df['side'])
df.drop('flavour', axis=1, inplace=True)


# make column multi-index based on animals (and reorder so that animals are on top (level 0))
df = df.unstack(level=0).reorder_levels([1,0], axis=1)
df.sortlevel(0, axis = 1, inplace = True)



#Rows to drop (testing, not actual results)
#  no tones were used on day 1, was just for testing
toDrop = df.ix[(1,1,1,1):(1,1,3,10)]
toDrop = toDrop.index
df = df.drop(toDrop)

# problems with the system crashing, first 5 trials should not be counted
toDrop = df.ix[(1,8,2,1):(1,8,2,5)]
toDrop = toDrop.index
df = df.drop(toDrop)

toDrop = df.ix[(1,8,3,1):(1,8,3,5)]
IndexesToDrop = toDrop.index
df = df.drop(toDrop)

indx = ["Phase","Day","Block","Trial"]
ManScor = pd.read_csv("ManualScores.csv")
ManScor = ManScor.set_index(indx,drop = True)
AutoData = df.set_index(ManScor.index)

AutoData.to_csv("AutoData.csv", index = True, tupleize_cols = False)

