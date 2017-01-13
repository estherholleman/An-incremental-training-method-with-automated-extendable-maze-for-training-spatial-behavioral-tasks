# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 10:06:28 2016

@author: esther
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patch
import matplotlib
matplotlib.style.use('ggplot') #makes plots look pretty


# calculate scores per day

# load AllScores 
AllScores = pd.read_csv("AllScoresAllTasksTyposCorrected.csv")

# drop columns that were saved as index
AllScores = AllScores.drop(AllScores.columns[[0,1]],axis = 1)

## drop day 1 of phase 4 (all nans)
#AllScores = AllScores.drop(AllScores.index[[range(2670,2730)]])



# prepare index for days
phase1 = [1] * 210
phase2 = [2] * 1740
phase3 = [3] * 720
phase4 = [4] * 420
phase5 = [5] * 720
phase6 = [6] * 600


phases = phase1 + phase2 + phase3 + phase4 + phase5 + phase6

days1 = sorted(range(1,8)*30)
days2 = sorted(range(1,30)*60)
days3 = sorted(range(1,13)*60)
days4 = sorted(range(1,8)*60)
days5 = sorted(range(1,10)*80)
days6 = sorted(range(1,7)*100)


days = days1 + days2 + days3 + days4 + days5 + days6

arrays = [phases,days]

tuples = list(zip(*arrays))

index = pd.MultiIndex.from_tuples(tuples, names=['Phase', 'Day'])

# Add index to scores matrix
AllScoresWithIndx = AllScores.set_index(index)


# calculate totals per day
AllScoresSummed = AllScoresWithIndx.sum(axis = 0,level = ["Phase","Day"])
countGroups = AllScoresWithIndx.groupby(level = ["Phase","Day"])


ScoresPerDay = AllScoresSummed/countGroups.count(axis=0) * 100

PhaseLengths = [];
phases = range(1,7)
phase = 1

for phase in phases:  
    PhaseLengths.append(len(ScoresPerDay.iloc[ScoresPerDay.index.get_level_values('Phase') == phase]))

DaysInPhase = np.cumsum(PhaseLengths)

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
for p in [
    patch.Rectangle(
        (0.1, 0.1), PhaseLengths[0], 99.9,
        alpha=0.4,
        facecolor = "#580029"
    ),
  
    patch.Rectangle(
        (DaysInPhase[0], 0.1), PhaseLengths[1], 99.9,
        alpha=0.35,
        facecolor = "#681f4c"
    ),

    patch.Rectangle(
        (DaysInPhase[1], 0.1), PhaseLengths[2], 99.9,
        alpha=0.4,
        facecolor = "#FA8072"
   ),
    patch.Rectangle(
        (DaysInPhase[2], 0.1), PhaseLengths[3], 99.9,
        alpha=0.35,
        facecolor = "#890045"
    ),
    patch.Rectangle(
        (DaysInPhase[3], 0.1), PhaseLengths[4], 99.9,
        alpha=0.2,
        facecolor = "#9e015f"
    ),
    patch.Rectangle(
        (DaysInPhase[4], 0.1), PhaseLengths[5], 99.9,
        alpha=0.5,
        facecolor = "#F08080"
    )
]:
    ax1.add_patch(p)
    

ax2 = ScoresPerDay.plot(ax = ax1,colormap = 'winter', title = "Learning Curves Group 2",figsize = (11.69,8.27))

patches,labels = ax2.get_legend_handles_labels()
ax2.legend(patches,labels,loc=4)
ax2.set_xlabel("(Phase,Trial)")
ax2.set_ylabel("% Correct")


plt.savefig("ScoresPerDay.eps",format = "eps")
plt.savefig("ScoresPerDay.png",format = "png")