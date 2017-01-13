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
indexes = ["Animal","Phase","Day","Block","trial_nr"]

for indx in indexes:   
    frame[indx] = frame[indx].astype(int)

# set animal to trial_nr columns as multi-index
df  = frame.set_index(indexes,drop = True)


df.drop('aditional_info', axis=1, inplace=True)

df['side'] = df['flavour'].combine_first(df['side'])

df.drop('flavour', axis=1, inplace=True)



#%% extract randomization 
Rat1RD = df["side"].iloc[df.index.get_level_values('Animal') == 1]
Rat2RD = df["side"].iloc[df.index.get_level_values('Animal') == 2]
Rat3RD = df["side"].iloc[df.index.get_level_values('Animal') == 3]
Rat4RD = df["side"].iloc[df.index.get_level_values('Animal') == 4]

rd1 = pd.DataFrame(Rat1RD)
rd1.index = rd1.index.droplevel()

rd2 = pd.DataFrame(Rat2RD)
rd2.index = rd2.index.droplevel()

rd3 = pd.DataFrame(Rat3RD)
rd3.index = rd3.index.droplevel()

rd4 = pd.DataFrame(Rat4RD)
rd4.index = rd4.index.droplevel()

Randomization = pd.concat([rd1,rd2,rd3,rd4], join = "outer", axis = 1)
cols = ["Rat1","Rat2","Rat3","Rat4"]
Randomization.columns = cols

for col in cols:
     Randomization[col] = Randomization[col].astype(float)



#%% make reaction time dataframe
Rat1RT = df["reaction_time"].iloc[df.index.get_level_values('Animal') == 1]
Rat2RT = df["reaction_time"].iloc[df.index.get_level_values('Animal') == 2]
Rat3RT = df["reaction_time"].iloc[df.index.get_level_values('Animal') == 3]
Rat4RT = df["reaction_time"].iloc[df.index.get_level_values('Animal') == 4]

rt1 = pd.DataFrame(Rat1RT)
rt1.index = rt1.index.droplevel()

rt2 = pd.DataFrame(Rat2RT)
rt2.index = rt2.index.droplevel()

rt3 = pd.DataFrame(Rat3RT)
rt3.index = rt3.index.droplevel()

rt4 = pd.DataFrame(Rat4RT)
rt4.index = rt4.index.droplevel()

ReactionTimes = pd.concat([rt1,rt2,rt3,rt4], join = "outer", axis = 1)
ReactionTimes.columns = ["Rat1","Rat2","Rat3","Rat4"]

# save reaction times
ReactionTimes.to_csv("ReactionTimes.csv", tupleize_cols = True)


#%% calculate hints given
hints = ((df.reward_size < 1) & (df.additional_reward > 0))

hints1 = hints.iloc[hints.index.get_level_values('Animal') == 1]
hints1 = pd.DataFrame(hints1)
hints1.index = hints1.index.droplevel()

hints2 = hints.iloc[hints.index.get_level_values('Animal') == 2]
hints2 = pd.DataFrame(hints2)
hints2.index = hints2.index.droplevel()

hints3 = hints.iloc[hints.index.get_level_values('Animal') == 3]
hints3 = pd.DataFrame(hints3)
hints3.index = hints3.index.droplevel()

hints4 = hints.iloc[hints.index.get_level_values('Animal') == 4]
hints4 = pd.DataFrame(hints4)
hints4.index = hints4.index.droplevel()

HintsGiven = (pd.concat([hints1,hints2,hints3,hints4], join = "outer", axis = 1)).astype('float')
HintsGiven.columns = ["Rat1","Rat2","Rat3","Rat4"]

# calculate totals per day
HintsPerDay = HintsGiven.sum(axis = 0,level = ["Phase","Day"])



#%% calculate scores based on sensors - these do not take timing into account, also not the fact that a hint may have been given
sensScore = df.side == df.animal_answer

ss1 = sensScore.iloc[sensScore.index.get_level_values('Animal') == 1]
ss1 = pd.DataFrame(ss1)
ss1.index = ss1.index.droplevel()

ss2 = sensScore.iloc[sensScore.index.get_level_values('Animal') == 2]
ss2 = pd.DataFrame(ss2)
ss2.index = ss2.index.droplevel()

ss3 = sensScore.iloc[sensScore.index.get_level_values('Animal') == 3]
ss3 = pd.DataFrame(ss3)
ss3.index = ss3.index.droplevel()

ss4 = sensScore.iloc[sensScore.index.get_level_values('Animal') == 4]
ss4 = pd.DataFrame(ss4)
ss4.index = ss4.index.droplevel()

SensorScores = pd.concat([ss1,ss2,ss3,ss4], join = "outer", axis = 1)
SensorScores.columns = ["Rat1","Rat2","Rat3","Rat4"]


# calculate totals per day
SensorScoresSummed = SensorScores.sum(axis = 0,level = ["Phase","Day"])
SensorCounts = SensorScores.groupby(level = ["Phase","Day"])
TotalTrials = SensorCounts.count(axis=0)


SensorScoresPerDay = SensorScoresSummed/TotalTrials * 100


SensorScoresPerDayPhaseAvg = getPhaseAvg(SensorScoresPerDay)
SensorScoresPerDayAvg = SensorScoresPerDay.mean(axis = 1)

ax1 = SensorScoresPerDayAvg.plot(color="k",linewidth = 3,figsize = (11.69,8.27))
#ax1.set_xticklabels(range(1,8))
ax2 = SensorScoresPerDay.plot(ax = ax1,title="Scores Based on Sensor Activation",ylim=[0,100])
ax2.set_ylabel("% Correct")
patches,labels = ax2.get_legend_handles_labels()
ax2.legend(patches,labels,loc=4,prop={'size':10})

plt.savefig("SensorScoresPerDay.eps",format = "eps")
plt.savefig("SensorScoresPerDay.png",format = "png")


HintsBool = HintsGiven == 1
NoHints = ~HintsBool 


SensorScoresNoHints = SensorScores[NoHints]
SensorScoresNoHintsSummed = SensorScoresNoHints.sum(axis = 0,level = ["Phase","Day"])
SensorCountsNoHints = SensorScoresNoHints.groupby(level = ["Phase","Day"])
TotalTrialsNoHints = SensorCountsNoHints.count(axis=0)
SensorScoresPerDayNoHints = SensorScoresNoHintsSummed/TotalTrialsNoHints * 100

SensorScoresPhaseAvgNoHints = getPhaseAvg(SensorScoresPerDayNoHints)
SensorScoresAvgNoHints = SensorScoresPerDayNoHints.mean(axis = 1)

avgSensorScores = SensorScoresPerDayNoHints.mean(axis = 0,level = ["Phase"])

ax1 = SensorScoresPhaseAvgNoHints.plot(color="k",linewidth = 3,figsize = (11.69,8.27))
#ax1.set_xticklabels(range(1,8))
ax2 = SensorScoresPerDayNoHints.plot(ax = ax1,title="Sensor Scores, Excluding Hints",ylim=[0,100])
ax2.set_ylabel("% Correct")
patches,labels = ax2.get_legend_handles_labels()
ax2.legend(patches,labels,loc=4,prop={'size':10})

plt.savefig("SensorScoresNoHints.eps",format = "eps")
plt.savefig("SensorScoresNoHints.png",format = "png")


## select only those trials in which the rat reacted within a reasonable time
SensorScoresRT = SensorScores[(ReactionTimes > 700) & (ReactionTimes < 3000)]
SensorScoresRTSummed = SensorScoresRT.sum(axis = 0,level = ["Phase","Day"])
SensorCountsRT = SensorScoresRT.groupby(level = ["Phase","Day"])
TotalTrialsRT = SensorCountsRT.count(axis=0)

SensorScoresRTPerDay = SensorScoresRTSummed/TotalTrialsRT * 100


SensorScoresRTnoHints = SensorScoresRT[NoHints]

SensorScoresRTnoHintsSummed = SensorScoresRTnoHints.sum(axis = 0,level = ["Phase","Day"])
SensorCountsRTnoHints = SensorScoresRTnoHints.groupby(level = ["Phase","Day"])
TotalTrialsRTnoHints = SensorCountsRTnoHints.count(axis=0)

SensorScoresRTnoHintsPerDay = SensorScoresRTnoHintsSummed/TotalTrialsRTnoHints * 100



#%% calculate score based on additional rewards
AddRwScore = df.reward_size + df.additional_reward > 2

arw1 = AddRwScore.iloc[AddRwScore.index.get_level_values('Animal') == 1]
arw1 = pd.DataFrame(arw1)
arw1.index = arw1.index.droplevel()

arw2 = AddRwScore.iloc[AddRwScore.index.get_level_values('Animal') == 2]
arw2 = pd.DataFrame(arw2)
arw2.index = arw2.index.droplevel()

arw3 = AddRwScore.iloc[AddRwScore.index.get_level_values('Animal') == 3]
arw3 = pd.DataFrame(arw3)
arw3.index = arw3.index.droplevel()

arw4 = AddRwScore.iloc[AddRwScore.index.get_level_values('Animal') == 4]
arw4 = pd.DataFrame(arw4)
arw4.index = arw4.index.droplevel()

AddRewardScores = (pd.concat([arw1,arw2,arw3,arw4], join = "outer", axis = 1)).astype('float')
AddRewardScores.columns = ["Rat1","Rat2","Rat3","Rat4"]

# calculate totals per day
AddRewardScoresSummed = AddRewardScores.sum(axis = 0,level = ["Phase","Day"])
AddRewardCounts = AddRewardScores.groupby(level = ["Phase","Day"])

AddRewardScoresPerDay = AddRewardScoresSummed/AddRewardCounts.count(axis=0) * 100




#%% calculate score based on sensor triggered rewards given (these kind of rewards are not given if additional reward was given before the sensor was crossed (hint))
RwScore = df.reward_size  > 0

rw1 = RwScore.iloc[RwScore.index.get_level_values('Animal') == 1]
rw1 = pd.DataFrame(rw1)
rw1.index = rw1.index.droplevel()

rw2 = RwScore.iloc[RwScore.index.get_level_values('Animal') == 2]
rw2 = pd.DataFrame(rw2)
rw2.index = rw2.index.droplevel()

rw3 = RwScore.iloc[RwScore.index.get_level_values('Animal') == 3]
rw3 = pd.DataFrame(rw3)
rw3.index = rw3.index.droplevel()

rw4 = RwScore.iloc[RwScore.index.get_level_values('Animal') == 4]
rw4 = pd.DataFrame(rw4)
rw4.index = rw4.index.droplevel()

RewardScores = (pd.concat([rw1,rw2,rw3,rw4], join = "outer", axis = 1)).astype('float')
RewardScores.columns = ["Rat1","Rat2","Rat3","Rat4"]

RewardScoresSummed = RewardScores.sum(axis = 0,level = ["Phase","Day"])
RewardCounts = RewardScores.groupby(level = ["Phase","Day"])
TotalTrials = RewardCounts.count(axis=0) 
TotalTrialsNoHints = TotalTrials - HintsPerDay

RewardScoresPerDay = RewardScoresSummed/TotalTrials * 100
RewardScoresPerDayNoHints = RewardScoresSummed/TotalTrialsNoHints * 100



# calculate totals per day
def getPhaseAvg(data):
    avg = data.mean(axis = 0,level = ["Phase"])
    avgAllAnimals = avg.mean(axis = 1)
    df = pd.DataFrame(avgAllAnimals)
    df.index = [(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]
    df = df.reindex(data.index)
    df = df.apply(pd.Series.interpolate)
    df.columns = ['Average']
    return df
    
    
    

RewardScoresPhaseAvg = getPhaseAvg(RewardScoresPerDay)
RewardScoresAvg = RewardScoresPerDay.mean(axis = 1)

RewardScoresPhaseAvgNoHints = getPhaseAvg(RewardScoresPerDayNoHints)
RewardScoresAvgNoHints = RewardScoresPerDayNoHints.mean(axis = 1)

ax1 = RewardScoresAvgNoHints.plot(color="k",linewidth = 3,figsize = (11.69,8.27))
#ax1.set_xticklabels(range(1,8))
ax2 = RewardScoresPerDayNoHints.plot(ax = ax1,title="Scores Based on Reward Given by Computer Excluding Hints",ylim=[0,100])
ax2.set_ylabel("% Correct")
patches,labels = ax2.get_legend_handles_labels()
ax2.legend(patches,labels,loc=4,prop={'size':10})

plt.savefig("RewardScoresNoHints.eps",format = "eps")
plt.savefig("RewardScoresNoHints.png",format = "png")


ax1 = RewardScoresPhaseAvgNoHints.plot(color="k",linewidth = 3,figsize = (11.69,8.27))
#ax1.set_xticklabels(range(1,8))
ax2 = RewardScoresPerDayNoHints.plot(ax = ax1,title="Scores Based on Reward Given by Computer Excluding Hints",ylim=[0,100])
ax2.set_ylabel("% Correct")
patches,labels = ax2.get_legend_handles_labels()
ax2.legend(patches,labels,loc=4,prop={'size':10})

plt.savefig("RewardScoresNoHintsPhaseAvg.eps",format = "eps")
plt.savefig("RewardScoresNoHintsPhaseAvg.png",format = "png")

