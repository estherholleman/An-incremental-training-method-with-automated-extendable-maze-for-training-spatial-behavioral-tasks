# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 11:59:48 2016

@author: esther
"""
import pandas as pd

phase1 = [1] *41
phase2 = [2] * 6
phase3 = [3] * 9
phase4 = [4] * 6

phases = phase1 + phase2 + phase3 + phase4

indx1 = range(1,42)
indx2 = range(1,7)
indx3 = range(1,10)
indx4 = range(1,7)

indxes = indx1 + indx2 + indx3 + indx4

arrays = [phases,indxes]

tuples = list(zip(*arrays))

index = pd.MultiIndex.from_tuples(tuples, names=['Phase', 'Day'])

AllScoresWithIndx = AllScoresDf.set_index(index)


#subsetting to get only those scores of phase 1
Phase1Scores = AllScoresWithIndx.iloc[AllScoresWithIndx.index.get_level_values('Phase') == 1]