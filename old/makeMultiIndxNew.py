# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 11:59:48 2016

@author: esther
"""

# make phases
phase1 = [1] * 210
phase2 = [2] * 1740
phase3 = [3] * 720
phase4 = [4] * 420
phase5 = [5] * 720
phase6 = [6] * 600

phases = phase1 + phase2 + phase3 + phase4 + phase5 + phase6


# make days
days1 = sorted(range(1,8)*30)
days2 = sorted(range(1,30)*60)
days3 = sorted(range(1,13)*60)
days4 = sorted(range(1,8)*60)
days5 = sorted(range(1,10)*80)
days6 = sorted(range(1,7)*100)

days = days1 + days2 + days3 + days4 + days5 + days6


# make blocks?


# make trials?


arrays = [phases,days]

tuples = list(zip(*arrays))

index = pd.MultiIndex.from_tuples(tuples, names=['Phase', 'Day'])

AllScoresWithIndx = AllScores.set_index(index)


#subsetting to get only those scores of phase 1
Phase1Scores = AllScoresWithIndx.iloc[AllScoresWithIndx.index.get_level_values('Phase') == 1]