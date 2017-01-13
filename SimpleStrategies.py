# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 16:39:03 2016

@author: esther
"""

import pandas as pd
from myFunctions import generate_flavors
import matplotlib.pyplot as plt


sides = pd.read_csv("Randomization.csv")

randIndx = ["Phase","Day","Block", "trial_nr"]
Rnd = sides.set_index(randIndx,drop = True)

nTrials = len(Rnd)

# always alternates
alt0 = [0,1] * (nTrials/2) + [0]
alt1 = [1,0] * (nTrials/2) + [1]

# always chooses the same side
pref0 = [0] * nTrials
pref1 = [1] * nTrials

# several different possible patterns
alt2x0 = [0,0,1] * (nTrials/3) + [0]
alt2x1 = [1,1,0] * (nTrials/3) + [1]

alt3x0 = [0,0,0,1] * (nTrials/4) + [0]
alt3x1 = [1,1,1,0] * (nTrials/4) + [1]

alt3x02x1 = [0,0,0,1,1] * (nTrials/5)
alt3x12x1 = [1,1,1,0,0] * (nTrials/5)

# using own randomization
ownRand = generate_flavors()

#%% calculate scores for each type of strategy
AltScores0 = Rnd == alt0
AltScores1 = Rnd == alt1

PrefScores0 = Rnd == pref0
PrefScores1 = Rnd == pref1

AltScores2x0 = Rnd == alt2x0
AltScores2x1 = Rnd == alt2x1

AltScores3x0 = Rnd == alt3x0
AltScores3x1 = Rnd == alt3x1

AltScores3x02x1 = Rnd == alt3x02x1
AltScores3x12x1 = Rnd == alt3x12x1

OwnRandScores = Rnd == ownRand

# compare randomizations for each rat against those for all other rats
Rat1RandScores = Rnd.fillna(0) == [Rnd["Rat1"].fillna(0)]
Rat2RandScores = Rnd.fillna(0) == [Rnd["Rat2"].fillna(0)]
Rat3RandScores = Rnd.fillna(0) == [Rnd["Rat3"].fillna(0)]
Rat4RandScores = Rnd.fillna(0) == [Rnd["Rat4"].fillna(0)]

#%% sum scores per day
AltScores0Summed = AltScores0.sum(axis = 0,level = ["Phase","Day"])
AltScores1Summed = AltScores1.sum(axis = 0,level = ["Phase","Day"])

PrefScores0Summed = PrefScores0.sum(axis = 0,level = ["Phase","Day"])
PrefScores1Summed = PrefScores1.sum(axis = 0,level = ["Phase","Day"])

AltScores2x0Summed = AltScores2x0.sum(axis = 0,level = ["Phase","Day"])
AltScores2x1Summed = AltScores2x1.sum(axis = 0,level = ["Phase","Day"])

AltScores3x0Summed = AltScores3x0.sum(axis = 0,level = ["Phase","Day"])
AltScores3x1Summed = AltScores3x1.sum(axis = 0,level = ["Phase","Day"])

AltScores3x02x1Summed = AltScores3x02x1.sum(axis = 0,level = ["Phase","Day"])
AltScores3x12x1Summed = AltScores3x12x1.sum(axis = 0,level = ["Phase","Day"])

OwnRandScoresSummed = OwnRandScores.sum(axis = 0,level = ["Phase","Day"])

Rat1RandScoresSummed = Rat1RandScores.sum(axis = 0,level = ["Phase","Day"])
Rat2RandScoresSummed = Rat2RandScores.sum(axis = 0,level = ["Phase","Day"])
Rat3RandScoresSummed = Rat3RandScores.sum(axis = 0,level = ["Phase","Day"])
Rat4RandScoresSummed = Rat4RandScores.sum(axis = 0,level = ["Phase","Day"])

# calculate total trials per day
totalTrials = AltScores0.groupby(level = ["Phase","Day"])


#%% calculate percent correct by dividing by totalTrials
AltScores1PerDay = AltScores0Summed/totalTrials.count(axis=0) * 100
AltScores2PerDay = AltScores1Summed/totalTrials.count(axis=0) * 100
PrefScores1PerDay = PrefScores0Summed/totalTrials.count(axis=0) * 100
PrefScores2PerDay = PrefScores1Summed/totalTrials.count(axis=0) * 100
AltScores2x0PerDay = AltScores2x0Summed/totalTrials.count(axis=0) * 100
AltScores2x1PerDay = AltScores2x1Summed/totalTrials.count(axis=0) * 100
AltScores3x0PerDay = AltScores3x0Summed/totalTrials.count(axis=0) * 100
AltScores3x1PerDay = AltScores3x1Summed/totalTrials.count(axis=0) * 100
AltScores3x02x1PerDay = AltScores3x02x1Summed/totalTrials.count(axis=0) * 100
AltScores3x12x0PerDay = AltScores3x12x1Summed/totalTrials.count(axis=0) * 100
OwnRandScoresPerDay = OwnRandScoresSummed/totalTrials.count(axis=0) * 100
Rat1RandScoresPerDay = Rat1RandScoresSummed/totalTrials.count(axis=0) * 100
Rat2RandScoresPerDay = Rat2RandScoresSummed/totalTrials.count(axis=0) * 100
Rat3RandScoresPerDay = Rat3RandScoresSummed/totalTrials.count(axis=0) * 100
Rat4RandScoresPerDay = Rat4RandScoresSummed/totalTrials.count(axis=0) * 100

#%% Plot scores from different strategies

## Alternation
# scores when alternating, starting left


# get average per phase for alternation starting left
AltScores1PerDayAvgPerPhase = AltScores1PerDay.mean(axis = 0,level = ["Phase"])
AltScores1PerDayAvgAllAnimalsPerPhase = AltScores1PerDayAvgPerPhase.mean(axis = 1)

AltScores1PerDayAvgDf = pd.DataFrame(AltScores1PerDayAvgAllAnimalsPerPhase)
AltScores1PerDayAvgDf.index = [(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]
AltScores1PerDayAvgReIndx = AltScores1PerDayAvgDf.reindex(AltScores1PerDay.index)
AltScores1PerDayAvgReIndx = AltScores1PerDayAvgReIndx.apply(pd.Series.interpolate)

AltScores1PerDayAvgReIndx.columns = ['Average']

ax1 = AltScores1PerDayAvgReIndx.plot(color="k",linewidth = 3,figsize = (11.69,8.27))
#ax1.set_xticklabels(range(1,8))
ax2 = AltScores1PerDay.plot(ax = ax1,title="Alternate Starting Left Strategy",ylim=[0,100])
ax2.set_ylabel("% Correct")
patches,labels = ax2.get_legend_handles_labels()
ax2.legend(patches,labels,loc=4,prop={'size':10})

plt.savefig("Alternate Starting Left.eps",format = "eps")
plt.savefig("Alternate Starting Left.png",format = "png")





# scores when alternating, starting right


# get average per phase for alternation starting right
AltScores2PerDayAvgPerPhase = AltScores2PerDay.mean(axis = 0,level = ["Phase"])
AltScores2PerDayAvgAllAnimalsPerPhase = AltScores2PerDayAvgPerPhase.mean(axis = 1)

AltScores2PerDayAvgDf = pd.DataFrame(AltScores2PerDayAvgAllAnimalsPerPhase)
AltScores2PerDayAvgDf.index = [(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]
AltScores2PerDayAvgReIndx = AltScores2PerDayAvgDf.reindex(AltScores2PerDay.index)
AltScores2PerDayAvgReIndx = AltScores2PerDayAvgReIndx.apply(pd.Series.interpolate)

AltScores2PerDayAvgReIndx.columns = ['Average']

ax1 = AltScores2PerDayAvgReIndx.plot(color="k",linewidth = 3,figsize = (11.69,8.27))
#ax1.set_xticklabels(range(1,8))
ax2 = AltScores2PerDay.plot(ax = ax1,title="Alternate Starting Right Strategy",ylim=[0,100])
ax2.set_ylabel("% Correct")
patches,labels = ax2.get_legend_handles_labels()
ax2.legend(patches,labels,loc=4,prop={'size':10})

plt.savefig("Alternate Starting Right.eps",format = "eps")
plt.savefig("Alternate Starting Right.png",format = "png")





## Preference for one side only
# scores when only choosing left

PrefScores1PerDayAvgPerPhase = PrefScores1PerDay.mean(axis = 0,level = ["Phase"])
PrefScores1PerDayAvgAllAnimalsPerPhase = PrefScores1PerDayAvgPerPhase.mean(axis = 1)

PrefScores1PerDayAvgDf = pd.DataFrame(PrefScores1PerDayAvgAllAnimalsPerPhase)
PrefScores1PerDayAvgDf.index = [(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]
PrefScores1PerDayAvgReIndx = PrefScores1PerDayAvgDf.reindex(PrefScores1PerDay.index)
PrefScores1PerDayAvgReIndx = PrefScores1PerDayAvgReIndx.apply(pd.Series.interpolate)

PrefScores1PerDayAvgReIndx.columns = ['Average']

ax1 = PrefScores1PerDayAvgReIndx.plot(color="k",linewidth = 3,figsize = (11.69,8.27))
#ax1.set_xticklabels(range(1,8))
ax2 = PrefScores1PerDay.plot(ax = ax1,title="Left Side Only",ylim=[0,100])
ax2.set_ylabel("% Correct")
patches,labels = ax2.get_legend_handles_labels()
ax2.legend(patches,labels,loc=4,prop={'size':10})

plt.savefig("LeftOnly.eps",format = "eps")
plt.savefig("LeftOnly.png",format = "png")


# scores when only choosing right

PrefScores2PerDayAvgPerPhase = PrefScores2PerDay.mean(axis = 0,level = ["Phase"])
PrefScores2PerDayAvgAllAnimalsPerPhase = PrefScores2PerDayAvgPerPhase.mean(axis = 1)

PrefScores2PerDayAvgDf = pd.DataFrame(PrefScores2PerDayAvgAllAnimalsPerPhase)
PrefScores2PerDayAvgDf.index = [(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]
PrefScores2PerDayAvgReIndx = PrefScores2PerDayAvgDf.reindex(PrefScores2PerDay.index)
PrefScores2PerDayAvgReIndx = PrefScores2PerDayAvgReIndx.apply(pd.Series.interpolate)

PrefScores2PerDayAvgReIndx.columns = ['Average']

ax1 = PrefScores2PerDayAvgReIndx.plot(color="k",linewidth = 3,figsize = (11.69,8.27))
#ax1.set_xticklabels(range(1,8))
ax2 = PrefScores2PerDay.plot(ax = ax1,title="Right Side Only",ylim=[0,100])
ax2.set_ylabel("% Correct")
patches,labels = ax2.get_legend_handles_labels()
ax2.legend(patches,labels,loc=4,prop={'size':10})

plt.savefig("RightOnly.eps",format = "eps")
plt.savefig("RightOnly.png",format = "png")


## Various Alternation Patterns
# scores when alternating, twice left, once right (repetitively)
AltScores2x0PerDayAvgPerPhase = AltScores2x0PerDay.mean(axis = 0,level = ["Phase"])
AltScores2x0PerDayAvgAllAnimalsPerPhase = AltScores2x0PerDayAvgPerPhase.mean(axis = 1)

AltScores2x0PerDayAvgDf = pd.DataFrame(AltScores2x0PerDayAvgAllAnimalsPerPhase)
AltScores2x0PerDayAvgDf.index = [(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]
AltScores2x0PerDayAvgReIndx = AltScores2x0PerDayAvgDf.reindex(AltScores2x0PerDay.index)
AltScores2x0PerDayAvgReIndx = AltScores2x0PerDayAvgReIndx.apply(pd.Series.interpolate)

AltScores2x0PerDayAvgReIndx.columns = ['Average']

ax1 = AltScores2x0PerDayAvgReIndx.plot(color="k",linewidth = 3,figsize = (11.69,8.27))
#ax1.set_xticklabels(range(1,8))
ax2 = AltScores2x0PerDay.plot(ax = ax1,title="Pattern 2x Left, 1x Right",ylim=[0,100])
ax2.set_ylabel("% Correct")
patches,labels = ax2.get_legend_handles_labels()
ax2.legend(patches,labels,loc=4,prop={'size':10})

plt.savefig("TwiceLeftOnceRight.eps",format = "eps")
plt.savefig("TwiceLeftOnceRight.png",format = "png")





# scores when alternating, twice right, once left
AltScores2x1PerDayAvgPerPhase = AltScores2x1PerDay.mean(axis = 0,level = ["Phase"])
AltScores2x1PerDayAvgAllAnimalsPerPhase = AltScores2x1PerDayAvgPerPhase.mean(axis = 1)

AltScores2x1PerDayAvgDf = pd.DataFrame(AltScores2x1PerDayAvgAllAnimalsPerPhase)
AltScores2x1PerDayAvgDf.index = [(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]
AltScores2x1PerDayAvgReIndx = AltScores2x1PerDayAvgDf.reindex(AltScores2x1PerDay.index)
AltScores2x1PerDayAvgReIndx = AltScores2x1PerDayAvgReIndx.apply(pd.Series.interpolate)

AltScores2x1PerDayAvgReIndx.columns = ['Average']

ax1 = AltScores2x1PerDayAvgReIndx.plot(color="k",linewidth = 3,figsize = (11.69,8.27))
#ax1.set_xticklabels(range(1,8))
ax2 = AltScores2x1PerDay.plot(ax = ax1,title="Pattern 2x Right, 1x Left",ylim=[0,100])
ax2.set_ylabel("% Correct")
patches,labels = ax2.get_legend_handles_labels()
ax2.legend(patches,labels,loc=4,prop={'size':10})

plt.savefig("TwiceRightOnceLeft.eps",format = "eps")
plt.savefig("TwiceRightOnceLeft.png",format = "png")




# scores when alternating, twice left, once right (repetitively)
AltScores3x0PerDayAvgPerPhase = AltScores3x0PerDay.mean(axis = 0,level = ["Phase"])
AltScores3x0PerDayAvgAllAnimalsPerPhase = AltScores3x0PerDayAvgPerPhase.mean(axis = 1)

AltScores3x0PerDayAvgDf = pd.DataFrame(AltScores3x0PerDayAvgAllAnimalsPerPhase)
AltScores3x0PerDayAvgDf.index = [(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]
AltScores3x0PerDayAvgReIndx = AltScores3x0PerDayAvgDf.reindex(AltScores3x0PerDay.index)
AltScores3x0PerDayAvgReIndx = AltScores3x0PerDayAvgReIndx.apply(pd.Series.interpolate)

AltScores3x0PerDayAvgReIndx.columns = ['Average']

ax1 = AltScores3x0PerDayAvgReIndx.plot(color="k",linewidth = 3,figsize = (11.69,8.27))
#ax1.set_xticklabels(range(1,8))
ax2 = AltScores3x0PerDay.plot(ax = ax1,title="Pattern 3x Left, 1x Right",ylim=[0,100])
ax2.set_ylabel("% Correct")
patches,labels = ax2.get_legend_handles_labels()
ax2.legend(patches,labels,loc=4,prop={'size':10})

plt.savefig("3xLeft1xRight.eps",format = "eps")
plt.savefig("3xLeft1xRight.png",format = "png")


# scores when alternating, 3x right, once left
AltScores3x1PerDay.plot(title='Pattern 3x Right, 1x Left')

AltScores3x1PerDayAvgPerPhase = AltScores3x1PerDay.mean(axis = 0,level = ["Phase"])
AltScores3x1PerDayAvgAllAnimalsPerPhase = AltScores3x1PerDayAvgPerPhase.mean(axis = 1)

AltScores3x1PerDayAvgDf = pd.DataFrame(AltScores3x1PerDayAvgAllAnimalsPerPhase)
AltScores3x1PerDayAvgDf.index = [(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]
AltScores3x1PerDayAvgReIndx = AltScores3x1PerDayAvgDf.reindex(AltScores3x1PerDay.index)
AltScores3x1PerDayAvgReIndx = AltScores3x1PerDayAvgReIndx.apply(pd.Series.interpolate)

AltScores3x1PerDayAvgReIndx.columns = ['Average']

ax1 = AltScores3x1PerDayAvgReIndx.plot(color="k",linewidth = 3,figsize = (11.69,8.27))
ax2 = AltScores3x1PerDay.plot(ax = ax1,title="Pattern 3x Right, 1x Left",ylim=[0,100])
ax2.set_ylabel("% Correct")
patches,labels = ax2.get_legend_handles_labels()
ax2.legend(patches,labels,loc=4,prop={'size':10})

plt.savefig("3xRight1xLeft.eps",format = "eps")
plt.savefig("3xRight1xLeft.png",format = "png")


# scores when alternating, 3x left, twice right (repetitively)
AltScores3x02x1PerDayAvgPerPhase = AltScores3x02x1PerDay.mean(axis = 0,level = ["Phase"])
AltScores3x02x1PerDayAvgAllAnimalsPerPhase = AltScores3x02x1PerDayAvgPerPhase.mean(axis = 1)

AltScores3x02x1PerDayAvgDf = pd.DataFrame(AltScores3x02x1PerDayAvgAllAnimalsPerPhase)
AltScores3x02x1PerDayAvgDf.index = [(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]
AltScores3x02x1PerDayAvgReIndx = AltScores3x02x1PerDayAvgDf.reindex(AltScores3x1PerDay.index)
AltScores3x02x1PerDayAvgReIndx = AltScores3x02x1PerDayAvgReIndx.apply(pd.Series.interpolate)

AltScores3x02x1PerDayAvgReIndx.columns = ['Average']

ax1 = AltScores3x02x1PerDayAvgReIndx.plot(color="k",linewidth = 3,figsize = (11.69,8.27))
ax2 = AltScores3x02x1PerDay.plot(ax = ax1,title="Pattern 3x Left, 2x Right",ylim=[0,100])
ax2.set_ylabel("% Correct")
patches,labels = ax2.get_legend_handles_labels()
ax2.legend(patches,labels,loc=4,prop={'size':10})

plt.savefig("3xLeft2xRight.eps",format = "eps")
plt.savefig("3xLeft2xRight.png",format = "png")




# scores when alternating, 3x right, twice left
AltScores3x12x0PerDay.plot(title='Pattern 3x Right, 1x Left')

AltScores3x12x0PerDayAvgPerPhase = AltScores3x12x0PerDay.mean(axis = 0,level = ["Phase"])
AltScores3x12x0PerDayAvgAllAnimalsPerPhase = AltScores3x12x0PerDayAvgPerPhase.mean(axis = 1)

AltScores3x12x0PerDayAvgDf = pd.DataFrame(AltScores3x12x0PerDayAvgAllAnimalsPerPhase)
AltScores3x12x0PerDayAvgDf.index = [(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]
AltScores3x12x0PerDayAvgReIndx = AltScores3x12x0PerDayAvgDf.reindex(AltScores3x12x0PerDay.index)
AltScores3x12x0PerDayAvgReIndx = AltScores3x12x0PerDayAvgReIndx.apply(pd.Series.interpolate)

AltScores3x12x0PerDayAvgReIndx.columns = ['Average']

ax1 = AltScores3x12x0PerDayAvgReIndx.plot(color="k",linewidth = 3,figsize = (11.69,8.27))
ax2 = AltScores3x12x0PerDay.plot(ax = ax1,title="Pattern 3x Right, 2x Left",ylim=[0,100])
ax2.set_ylabel("% Correct")
patches,labels = ax2.get_legend_handles_labels()
ax2.legend(patches,labels,loc=4,prop={'size':10})

plt.savefig("3xRight2xLeft.eps",format = "eps")
plt.savefig("3xRight2xLeft.png",format = "png")


## Scores of one instance of own randomization against another generated by the same code
OwnRandScoresPerDayAvgPerPhase = OwnRandScoresPerDay.mean(axis = 0,level = ["Phase"])
OwnRandScoresPerDayAvgAllAnimalsPerPhase = OwnRandScoresPerDayAvgPerPhase.mean(axis = 1)

OwnRandScoresPerDayAvgDf = pd.DataFrame(OwnRandScoresPerDayAvgAllAnimalsPerPhase)
OwnRandScoresPerDayAvgDf.index = [(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]
OwnRandScoresPerDayAvgReIndx = OwnRandScoresPerDayAvgDf.reindex(OwnRandScoresPerDay.index)
OwnRandScoresPerDayAvgReIndx = OwnRandScoresPerDayAvgReIndx.apply(pd.Series.interpolate)

OwnRandScoresPerDayAvgReIndx.columns = ['Average']

ax1 = OwnRandScoresPerDayAvgReIndx.plot(color="k",linewidth = 3,figsize = (11.69,8.27))
ax2 = OwnRandScoresPerDay.plot(ax = ax1,title="Randomization against itself",ylim=[0,100])
ax2.set_ylabel("% Correct")
patches,labels = ax2.get_legend_handles_labels()
ax2.legend(patches,labels,loc=4,prop={'size':10})

plt.savefig("RandVSRand.eps",format = "eps")
plt.savefig("RandVSRand.png",format = "png")


## Randomization of 1 rat applied to the randomization of the others (including itself (= 100% correct))
# This is a double check as these randomizations were created together at the start of each day of training. 
Rat1RandScoresPerDay.plot(title='Randomization Of Rat 1 Against Rand. of Other Rats')
Rat2RandScoresPerDay.plot(title='Randomization Of Rat 2 Against Rand. of Other Rats')
Rat3RandScoresPerDay.plot(title='Randomization Of Rat 3 Against Rand. of Other Rats')
Rat4RandScoresPerDay.plot(title='Randomization Of Rat 4 Against Rand. of Other Rats')
