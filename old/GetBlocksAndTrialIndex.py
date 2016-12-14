# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 10:21:53 2016

@author: esther
"""

import pandas as pd


# load AllScores 
AllScores = pd.read_csv("AllScoresAllTasksTyposCorrected.csv")

# get column with blocks and trials
blockTrials = AllScores.iloc[:,1]

# remove indexing columns
AllScores = AllScores.drop(AllScores.columns[[0,1]],axis = 1)

#make blocks and trials
blocks = [0]*4410;
trials = [0]*4410;

i = 0

for trial in blockTrials:
    blocks[i] = int(trial[3])
    trials[i] = int(trial[5:])
    i = i + 1
        
 
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

arrays = [phases,days,blocks,trials]

tuples = list(zip(*arrays))

index = pd.MultiIndex.from_tuples(tuples, names=['Phase', 'Day','Block','Trial'])

# Add index to scores matrix
AllScoresWithIndx = AllScores.set_index(index)
