# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 16:29:17 2016

@author: esther
"""
import pandas as pd
import numpy as np
from random import randint
import matplotlib.pyplot as plt

#%% start by analyzing strategies applied to actual randomization
rnd = pd.read_csv("Randomization.csv")

Rnd = rnd.drop(rnd.columns[range(0,4)],axis = 1)

nTrials = len(Rnd)


#%% make bins for indexing

# bin per same number of trials as actual data
## make the bins
Bins = []
bins = range(105,4515,105)

for bin in bins:
    Bins = Bins + [bin]*105


phase1 = [1] * 210
phase2 = [2] * 1740
phase3 = [3] * 720
phase4 = [4] * 420
phase5 = [5] * 720
phase6 = [6] * 600

phases = phase1 + phase2 + phase3 + phase4 + phase5 + phase6

arrays = [phases,Bins]

tuples = list(zip(*arrays))

tuples = tuples[:-5]

index = pd.MultiIndex.from_tuples(tuples, names=['Phase', 'Bin'])


#%% Change on wrong choice, stay if correct: WinStay
#Make dataframe of nans to write result into:
WinStay = Rnd.copy()
WinStay[:] = np.nan


#% fill in the first row with a random choice of side
WinStay.ix[0] = [randint(0,1) for r in xrange(4)]


#loop through all trials
for choice, row in WinStay.iterrows():
    
    currentChoice = WinStay.ix[choice]
    incorrect = currentChoice[currentChoice != Rnd.ix[choice]]
    
    # fill in next choice with current choice (choose same side again)
    WinStay.ix[choice+1] = currentChoice
    # if answer is incorrect then go to the opposite site next
    WinStay.ix[choice+1,incorrect.index] = [1-t for t in incorrect]


WinStay = WinStay[:-1]


ScoresWinStay = WinStay == Rnd
# average scores for win-stay strategy
ScoresWinStayAvg = ScoresWinStay.sum() / len(WinStay) * 100


WinStayIndx = ScoresWinStay.set_index(index)

WinStaySummed = WinStayIndx.sum(axis = 0,level = "Bin")

totalTrials = WinStayIndx.count(axis = 0, level = "Bin");

WinStayScoresBinned = WinStaySummed/totalTrials * 100

# plot Win Stay Scores
ax2 = WinStayScoresBinned.plot(title="Win-Stay Strategy")
patches,labels = ax2.get_legend_handles_labels()
ax2.legend(patches,labels,loc=4)
ax2.set_xlabel("Trials")
ax2.set_ylabel("% Correct")



# give WinStay the index of the actual trials and days for comparison to data
randIndx = ["Phase","Day","Block", "trial_nr"]
rnd = rnd.set_index(randIndx,drop = True)

ScoresWinStay = ScoresWinStay.set_index(rnd.index)

WinStaySummed = ScoresWinStay.sum(axis = 0,level = ["Phase","Day"])
countGroups = ScoresWinStay.groupby(level = ["Phase","Day"])


ScoresPerDay = WinStaySummed/countGroups.count(axis=0) * 100


# get average per phase Win-Stay
WinStayAvgPerPhase = ScoresPerDay.mean(axis = 0,level = ["Phase"])
WinStayAvgAllAnimalsPerPhase = WinStayAvgPerPhase.mean(axis = 1)

WinStayAvgDf = pd.DataFrame(WinStayAvgAllAnimalsPerPhase)
WinStayAvgDf.index = [(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]
WinStayAvgReIndx = WinStayAvgDf.reindex(ScoresPerDay.index)
WinStayAvgReIndx = WinStayAvgReIndx.apply(pd.Series.interpolate)

WinStayAvgReIndx.columns = ['Average']

ax1 = WinStayAvgReIndx.plot(color="k",linewidth = 3,figsize = (11.69,8.27))
#ax1.set_xticklabels(range(1,8))
ax2 = ScoresPerDay.plot(ax = ax1,title="Win-Stay Strategy",ylim=[0,100])
ax2.set_ylabel("% Correct")
patches,labels = ax2.get_legend_handles_labels()
ax2.legend(patches,labels,loc=4,prop={'size':10})

plt.savefig("WinStayStrategy.eps",format = "eps")
plt.savefig("WinStayStrategy.png",format = "png")

#%% Change on correct choice, stay if incorrect (WinShift)

WinShift = Rnd.copy()
WinShift[:] = np.nan

#% fill in the first row with a random choice of side
WinShift.ix[0] = [randint(0,1) for r in xrange(4)]


#loop through all trials
for choice, row in WinShift.iterrows():
    
    currentChoice = WinShift.ix[choice]
    correct = currentChoice[currentChoice == Rnd.ix[choice]]
    
    # fill in next choice with current choice (choose same side again)
    WinShift.ix[choice+1] = currentChoice
    # if answer is correct then choose the opposite next time
    WinShift.ix[choice+1,correct.index] = [1-t for t in correct]


WinShift = WinShift[:-1]


ScoresWinShift = WinShift == Rnd
# average scores for win-stay strategy
ScoresWinShiftAvg = ScoresWinShift.sum() / len(WinShift) * 100


WinShiftIndx = ScoresWinShift.set_index(index)

WinShiftSummed = WinShiftIndx.sum(axis = 0,level = "Bin")

totalTrials = WinShiftIndx.count(axis = 0, level = "Bin");

WinShiftScoresBinned = WinShiftSummed/totalTrials * 100


# give WinStay the index of the actual trials and days for comparison to data

ScoresWinShift = ScoresWinShift.set_index(rnd.index)

WinShiftSummed = ScoresWinShift.sum(axis = 0,level = ["Phase","Day"])
countGroups = ScoresWinShift.groupby(level = ["Phase","Day"])


ScoresPerDayWinShift = WinShiftSummed/countGroups.count(axis=0) * 100



# get average per phase Win-Shift
WinShiftAvgPerPhase = ScoresPerDayWinShift.mean(axis = 0,level = ["Phase"])
WinShiftAvgAllAnimalsPerPhase = WinShiftAvgPerPhase.mean(axis = 1)

WinShiftAvgDf = pd.DataFrame(WinShiftAvgAllAnimalsPerPhase)
WinShiftAvgDf.index = [(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]
WinShiftAvgReIndx = WinShiftAvgDf.reindex(ScoresPerDayWinShift.index)
WinShiftAvgReIndx = WinShiftAvgReIndx.apply(pd.Series.interpolate)

WinShiftAvgReIndx.columns = ['Average']

ax1 = WinShiftAvgReIndx.plot(color="k",linewidth = 3,figsize = (11.69,8.27))
#ax1.set_xticklabels(range(1,8))
ax2 = ScoresPerDayWinShift.plot(ax = ax1,title="Win-Shift Strategy",ylim=[0,100])
ax2.set_ylabel("% Correct")
patches,labels = ax2.get_legend_handles_labels()
ax2.legend(patches,labels,loc=4,prop={'size':10})

plt.savefig("WinShiftStrategy.eps",format = "eps")
plt.savefig("WinShiftStrategy.png",format = "png")





#%% WinStay unless it's been the same side twice in a row

#Make dataframe of nans to write result into:
WinStay2 = Rnd.copy()
WinStay2[:] = np.nan


#% fill in the first row with a random choice of side
WinStay2.ix[0] = [randint(0,1) for r in xrange(4)]


#loop through all trials
for choice, row in WinStay2.iterrows():
    
    currentChoice = WinStay2.ix[choice]
    incorrect = currentChoice[currentChoice != Rnd.ix[choice]]
    correct = currentChoice[currentChoice == Rnd.ix[choice]]
  
    # fill in next choice with current choice (choose same side again)
    WinStay2.ix[choice+1] = currentChoice
    # if answer is incorrect then go to the opposite site next
    WinStay2.ix[choice+1,incorrect.index] = [1-t for t in incorrect]
    
    if choice > 1:
        double = correct[correct  ==  WinStay2.ix[choice-1,correct.index] ]
        WinStay2.ix[choice+1,double.index] = [1-t for t in incorrect]
        del double
    
    # of the correct answers check if for any rat this location is the same as the previous one
#    def checkDbl(choice, WinStay2):
#        if choice > 1:
#            double = correct[correct  ==  WinStay2.ix[choice-1,correct.index] ]
#            WinStay2.ix[choice+1,double.index] = [1-t for t in incorrect]
#            return WinStay2
#        else:
#            return WinStay2
#    
#    WinStay2 = checkDbl(choice, WinStay2)
       
 
WinStay2 = WinStay2[:-1]


ScoresWinStay2 = WinStay2 == Rnd
# average scores for win-stay strategy
ScoresWinStay2Avg = ScoresWinStay2.sum() / len(WinStay2) * 100


WinStay2Indx = ScoresWinStay2.set_index(index)

WinStay2Summed = WinStay2Indx.sum(axis = 0,level = "Bin")

totalTrials = WinStay2Indx.count(axis = 0, level = "Bin");

WinStay2ScoresBinned = WinStay2Summed/totalTrials * 100



# give WinStay2 the index of the actual trials and days for comparison to data
randIndx = ["Phase","Day","Block", "trial_nr"]
rnd = rnd.set_index(randIndx,drop = True)

ScoresWinStay2 = ScoresWinStay2.set_index(rnd.index)

WinStay2Summed = ScoresWinStay2.sum(axis = 0,level = ["Phase","Day"])
countGroups = ScoresWinStay2.groupby(level = ["Phase","Day"])


ScoresWinStay2 = WinStay2Summed/countGroups.count(axis=0) * 100





#%% WinStay unless it's been the same side 3x...








#%% Change when the tone changes
Change = Rnd.diff()

ToneChange = Rnd.copy()
ToneChange[:] = np.nan

ToneChange.ix[0] = [randint(0,1) for r in xrange(4)]

for choice, row in ToneChange.iterrows():
    
    currentChoice = ToneChange.ix[choice]
    change = Change.ix[choice] != 0 
    
    # choose same side again
    ToneChange.ix[choice+1] = currentChoice
    # unless the tone changed, then switch sides
    ToneChange.ix[choice+1,change.index] = [1-t for t in change]


ToneChange = ToneChange[:-1]

ScoresToneChange = ToneChange == Rnd
# average scores for win-stay strategy
ScoresToneChangeAvg = ScoresToneChange.sum() / len(ToneChange) * 100


ToneChangeIndx = ScoresToneChange.set_index(index)

ToneChangeSummed = ToneChangeIndx.sum(axis = 0,level = "Bin")

totalTrials = ToneChangeIndx.count(axis = 0, level = "Bin");

ToneChangeScoresBinned = ToneChangeSummed/totalTrials * 100


# give ToneChange the index of the actual trials and days for comparison to data
ScoresToneChange = ScoresToneChange.set_index(rnd.index)

ToneChangeSummed = ScoresToneChange.sum(axis = 0,level = ["Phase","Day"])
countGroups = ScoresToneChange.groupby(level = ["Phase","Day"])


ScoresToneChange = ToneChangeSummed/countGroups.count(axis=0) * 100


# get average per phase Win-Shift
ToneChangeAvgPerPhase = ScoresToneChange.mean(axis = 0,level = ["Phase"])
ToneChangeAvgAllAnimalsPerPhase = ToneChangeAvgPerPhase.mean(axis = 1)

ToneChangeAvgDf = pd.DataFrame(ToneChangeAvgAllAnimalsPerPhase)
ToneChangeAvgDf.index = [(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]
ToneChangeAvgReIndx = ToneChangeAvgDf.reindex(ScoresToneChange.index)
ToneChangeAvgReIndx = ToneChangeAvgReIndx.apply(pd.Series.interpolate)

ToneChangeAvgReIndx.columns = ['Average']

# plot Tone Change
ax1 = ToneChangeAvgReIndx.plot(color="k",linewidth = 3,figsize = (11.69,8.27))
#ax1.set_xticklabels(range(1,8))
ax2 = ScoresToneChange.plot(ax = ax1,title="Change On Tone Strategy",ylim=[0,100])
ax2.set_ylabel("% Correct")
patches,labels = ax2.get_legend_handles_labels()
ax2.legend(patches,labels,loc=4,prop={'size':10})

plt.savefig("ToneChangeStrategy.eps",format = "eps")
plt.savefig("ToneChangeStrategy.png",format = "png")


#for r in RndDiffTest:
#    
#    if RndDiffTest['Rat1'][r] == RndDiffTest['Rat1'][r-1]: 
#




#%% Change when tone changes, but get distracted every 5 trials (and randomly pick a side, then switch again on tone)
Change = Rnd.diff()

ToneChange5 = Rnd.copy()
ToneChange5[:] = np.nan

ToneChange5.ix[0] = [randint(0,1) for r in xrange(4)]

for choice, row in ToneChange5.iterrows():
    
    if choice%5 == 0:
        ToneChange5.ix[choice+1] = [randint(0,1) for r in xrange(4)]
     
    else:
        currentChoice = ToneChange5.ix[choice]
        change = Change.ix[choice] != 0 
        
        # choose same side again
        ToneChange5.ix[choice+1] = currentChoice
        # unless the tone changed, then switch sides
        ToneChange5.ix[choice+1,change.index] = [1-t for t in change]


ToneChange5 = ToneChange5[:-1]

ScoresToneChange5 = ToneChange5 == Rnd

# average scores for tone change + distracted every 5 trials strategy
ScoresToneChange5Avg = ScoresToneChange5.sum() / len(ToneChange5) * 100


ToneChange5Indx = ScoresToneChange5.set_index(index)

ToneChange5Summed = ToneChange5Indx.sum(axis = 0,level = "Bin")

totalTrials = ToneChange5Indx.count(axis = 0, level = "Bin");

ToneChange5ScoresBinned = ToneChange5Summed/totalTrials * 100


# give ToneChange the index of the actual trials and days for comparison to data
ScoresToneChange5 = ScoresToneChange5.set_index(rnd.index)

ToneChange5Summed = ScoresToneChange5.sum(axis = 0,level = ["Phase","Day"])
countGroups = ScoresToneChange5.groupby(level = ["Phase","Day"])


ScoresToneChange5 = ToneChange5Summed/countGroups.count(axis=0) * 100


# get average per phase Win-Shift
ToneChange5AvgPerPhase = ScoresToneChange5.mean(axis = 0,level = ["Phase"])
ToneChange5AvgAllAnimalsPerPhase = ToneChange5AvgPerPhase.mean(axis = 1)

ToneChange5AvgDf = pd.DataFrame(ToneChange5AvgAllAnimalsPerPhase)
ToneChange5AvgDf.index = [(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]
ToneChange5AvgReIndx = ToneChange5AvgDf.reindex(ScoresToneChange5.index)
ToneChange5AvgReIndx = ToneChange5AvgReIndx.apply(pd.Series.interpolate)

ToneChange5AvgReIndx.columns = ['Average']

# plot Tone Change
ax1 = ToneChange5AvgReIndx.plot(color="k",linewidth = 3,figsize = (11.69,8.27))
#ax1.set_xticklabels(range(1,8))
ax2 = ScoresToneChange5.plot(ax = ax1,title="Change On Tone, Distracted Every 5 sec",ylim=[0,100])
ax2.set_ylabel("% Correct")
patches,labels = ax2.get_legend_handles_labels()
ax2.legend(patches,labels,loc=4,prop={'size':10})

plt.savefig("ToneChange5Strategy.eps",format = "eps")
plt.savefig("ToneChange5Strategy.png",format = "png")





#%% Change when tone changes, but get distracted every 10 trials (and randomly pick a side, then switch again on tone)

Change = Rnd.diff()

ToneChange10 = Rnd.copy()
ToneChange10[:] = np.nan

ToneChange10.ix[0] = [randint(0,1) for r in xrange(4)]

for choice, row in ToneChange10.iterrows():
    
    if choice%10 == 0:
        ToneChange10.ix[choice+1] = [randint(0,1) for r in xrange(4)]
     
    else:
        currentChoice = ToneChange10.ix[choice]
        change = Change.ix[choice] != 0 
        
        # choose same side again
        ToneChange10.ix[choice+1] = currentChoice
        # unless the tone changed, then switch sides
        ToneChange10.ix[choice+1,change.index] = [1-t for t in change]


ToneChange10 = ToneChange10[:-1]

ScoresToneChange10 = ToneChange10 == Rnd

# average scores for tone change + distracted every 10 trials strategy
ScoresToneChange10Avg = ScoresToneChange10.sum() / len(ToneChange10) * 100


ToneChange10Indx = ScoresToneChange10.set_index(index)

ToneChange10Summed = ToneChange10Indx.sum(axis = 0,level = "Bin")

totalTrials = ToneChange10Indx.count(axis = 0, level = "Bin");

ToneChange10ScoresBinned = ToneChange10Summed/totalTrials * 100




# give ToneChange the index of the actual trials and days for comparison to data
ScoresToneChange10 = ScoresToneChange10.set_index(rnd.index)

ToneChange10Summed = ScoresToneChange10.sum(axis = 0,level = ["Phase","Day"])
countGroups = ScoresToneChange10.groupby(level = ["Phase","Day"])


ScoresToneChange10 = ToneChange10Summed/countGroups.count(axis=0) * 100


# get average per phase Win-Shift
ToneChange10AvgPerPhase = ScoresToneChange10.mean(axis = 0,level = ["Phase"])
ToneChange10AvgAllAnimalsPerPhase = ToneChange10AvgPerPhase.mean(axis = 1)

ToneChange10AvgDf = pd.DataFrame(ToneChange10AvgAllAnimalsPerPhase)
ToneChange10AvgDf.index = [(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]
ToneChange10AvgReIndx = ToneChange10AvgDf.reindex(ScoresToneChange10.index)
ToneChange10AvgReIndx = ToneChange10AvgReIndx.apply(pd.Series.interpolate)

ToneChange10AvgReIndx.columns = ['Average']

# plot Tone Change
ax1 = ToneChange10AvgReIndx.plot(color="k",linewidth = 3,figsize = (11.69,8.27))
#ax1.set_xticklabels(range(1,8))
ax2 = ScoresToneChange10.plot(ax = ax1,title="Change On Tone, Distracted every 10 sec",ylim=[0,100])
ax2.set_ylabel("% Correct")
patches,labels = ax2.get_legend_handles_labels()
ax2.legend(patches,labels,loc=4,prop={'size':10})

plt.savefig("ToneChangeStrategy10.eps",format = "eps")
plt.savefig("ToneChangeStrategy10.png",format = "png")








#%% Change when tone changes, but get distracted every 5 to 10 trials (randomly determined) 
ToneChangeRand = Rnd.copy()
ToneChangeRand[:] = np.nan

ToneChangeRand.ix[0] = [randint(0,1) for r in xrange(4)]

for choice, row in ToneChange10.iterrows():
    
    if choice%randint(5,10) == 0:
        ToneChangeRand.ix[choice+1] = [randint(0,1) for r in xrange(4)]
     
    else:
        currentChoice = ToneChangeRand.ix[choice]
        change = Change.ix[choice] != 0 
        
        # choose same side again
        ToneChangeRand.ix[choice+1] = currentChoice
        # unless the tone changed, then switch sides
        ToneChangeRand.ix[choice+1,change.index] = [1-t for t in change]


ToneChangeRand = ToneChangeRand[:-1]

ScoresToneChangeRand = ToneChangeRand == Rnd

# average scores for tone change + distracted every 5 to 10 trials strategy
ScoresToneChangeRandAvg = ScoresToneChangeRand.sum() / len(ToneChangeRand) * 100


ToneChangeRandIndx = ScoresToneChangeRand.set_index(index)

ToneChangeRandSummed = ToneChangeRandIndx.sum(axis = 0,level = "Bin")

totalTrials = ToneChangeRandIndx.count(axis = 0, level = "Bin");

ToneChangeRandScoresBinned = ToneChangeRandSummed/totalTrials * 100


# give ToneChange the index of the actual trials and days for comparison to data
ScoresToneChangeRand = ScoresToneChangeRand.set_index(rnd.index)

ToneChangeRandSummed = ScoresToneChangeRand.sum(axis = 0,level = ["Phase","Day"])
countGroups = ScoresToneChangeRand.groupby(level = ["Phase","Day"])


ScoresToneChangeRand = ToneChangeRandSummed/countGroups.count(axis=0) * 100


# get average per phase Win-Shift
ToneChangeRandAvgPerPhase = ScoresToneChangeRand.mean(axis = 0,level = ["Phase"])
ToneChangeRandAvgAllAnimalsPerPhase = ToneChangeRandAvgPerPhase.mean(axis = 1)

ToneChangeRandAvgDf = pd.DataFrame(ToneChangeRandAvgAllAnimalsPerPhase)
ToneChangeRandAvgDf.index = [(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]
ToneChangeRandAvgReIndx = ToneChangeRandAvgDf.reindex(ScoresToneChangeRand.index)
ToneChangeRandAvgReIndx = ToneChangeRandAvgReIndx.apply(pd.Series.interpolate)

ToneChangeRandAvgReIndx.columns = ['Average']

# plot Tone Change
ax1 = ToneChangeRandAvgReIndx.plot(color="k",linewidth = 3,figsize = (11.69,8.27))
#ax1.set_xticklabels(range(1,8))
ax2 = ScoresToneChangeRand.plot(ax = ax1,title="Change On Tone, Distracted Randomly every 5 to 10 sec",ylim=[0,100])
ax2.set_ylabel("% Correct")
patches,labels = ax2.get_legend_handles_labels()
ax2.legend(patches,labels,loc=4,prop={'size':10})

plt.savefig("ToneChangeStrategyRand.eps",format = "eps")
plt.savefig("ToneChangeStrategyRand.png",format = "png")
