# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 16:07:47 2016

@author: esther
"""
import pandas as pd

phase1 = [1] * 7
phase2 = [2] * 29
phase3 = [3] * 12
phase4 = [4] * 7
phase5 = [5] * 9
phase6 = [6] * 6

days1 = range(1,8)
days2 = range(1,30)
days3 = range(1,13)
days4 = range(1,8)
days5 = range(1,10)
days6 = range(1,7)


phases = phase1 + phase2 + phase3 + phase4 + phase5 + phase6

days = days1 + days2 + days3 + days4 + days5 + days6

arrays = [phases,days]

tuples = list(zip(*arrays))

index = pd.MultiIndex.from_tuples(tuples, names=['Phase', 'Day'])

Weights = pd.DataFrame(0, index = range(1,71), columns =['Rat1', 'Rat2', 'Rat3','Rat4'])

