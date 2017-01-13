# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 14:40:08 2016

@author: esther
"""


import pandas as pd
from myFunctions import unpackCSVs

# get dataframe with raw data from CSVs
frame = unpackCSVs()

#%% prepare dataframe for manipulations
indexes = ["Animal", "Day", "Block","trial_nr"]

for indx in indexes:   
    frame[indx] = frame[indx].astype(int)

df  = frame.set_index(indexes,drop = True)
df.drop('aditional_info', axis=1, inplace=True)

#%% make reaction time dataframe
Rat1RT = df["reaction_time"].iloc[df.index.get_level_values('Animal') == 1]
Rat2RT = df["reaction_time"].iloc[df.index.get_level_values('Animal') == 2]
Rat3RT = df["reaction_time"].iloc[df.index.get_level_values('Animal') == 3]

rt1 = pd.DataFrame(Rat1RT)
rt1.index = rt1.index.droplevel()

rt2 = pd.DataFrame(Rat2RT)
rt2.index = rt2.index.droplevel()

rt3 = pd.DataFrame(Rat3RT)
rt3.index = rt3.index.droplevel()

ReactionTimes = pd.concat([rt1,rt2,rt3], join = "outer", axis = 1)
ReactionTimes.columns = ["Rat1","Rat2","Rat3"]



#%% calculate scores based on sensors
sensScore = df.flavour == df.animal_answer

ss1 = sensScore.iloc[sensScore.index.get_level_values('Animal') == 1]
ss1 = pd.DataFrame(ss1)
ss1.index = ss1.index.droplevel()

ss2 = sensScore.iloc[sensScore.index.get_level_values('Animal') == 2]
ss2 = pd.DataFrame(ss2)
ss2.index = ss2.index.droplevel()

ss3 = sensScore.iloc[sensScore.index.get_level_values('Animal') == 3]
ss3 = pd.DataFrame(ss3)
ss3.index = ss3.index.droplevel()

SensorScores = pd.concat([ss1,ss2,ss3], join = "outer", axis = 1)
SensorScores.columns = ["Rat1","Rat2","Rat3"]

# calculate totals per day
SensorScoresSummed = SensorScores.sum(axis = 0,level = ["Day"])
SensorCounts = SensorScores.groupby(level = ["Day"])

SensorScoresPerDay = (SensorScoresSummed/SensorCounts.count(axis=0) * 100)

#%% calculate score based on additional rewards
RwScore = df.reward_size + df.additional_reward > 2

rw1 = RwScore.iloc[RwScore.index.get_level_values('Animal') == 1]
rw1 = pd.DataFrame(rw1)
rw1.index = rw1.index.droplevel()

rw2 = RwScore.iloc[RwScore.index.get_level_values('Animal') == 2]
rw2 = pd.DataFrame(rw2)
rw2.index = rw2.index.droplevel()

rw3 = RwScore.iloc[RwScore.index.get_level_values('Animal') == 3]
rw3 = pd.DataFrame(rw3)
rw3.index = rw3.index.droplevel()

RewardScores = (pd.concat([rw1,rw2,rw3], join = "outer", axis = 1)).astype('float')
RewardScores.columns = ["Rat1","Rat2","Rat3"]

# calculate totals per day
RewardScoresSummed = RewardScores.sum(axis = 0,level = ["Day"])
RewardCounts = RewardScores.groupby(level = ["Day"])

RewardScoresPerDay = RewardScoresSummed/RewardCounts.count(axis=0) * 100


#%% extract randomization 
Rat1RD = df["flavour"].iloc[df.index.get_level_values('Animal') == 1]
Rat2RD = df["flavour"].iloc[df.index.get_level_values('Animal') == 2]
Rat3RD = df["flavour"].iloc[df.index.get_level_values('Animal') == 3]

rd1 = pd.DataFrame(Rat1RD)
rd1.index = rd1.index.droplevel()

rd2 = pd.DataFrame(Rat2RD)
rd2.index = rd2.index.droplevel()

rd3 = pd.DataFrame(Rat3RD)
rd3.index = rd3.index.droplevel()

Randomization = pd.concat([rd1,rd2,rd3], join = "outer", axis = 1)
cols = ["Rat1","Rat2","Rat3"]
Randomization.columns = cols

for col in cols:
     Randomization[col] = Randomization[col].astype(float)

