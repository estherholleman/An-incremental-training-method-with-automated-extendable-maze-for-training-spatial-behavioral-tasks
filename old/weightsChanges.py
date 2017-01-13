# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 14:06:15 2016

@author: esther
"""
## find the impact of weight on scores

# import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patch
import matplotlib
matplotlib.style.use('ggplot')


# read in necessary files
weights = pd.read_csv("weights.csv")


# make dataframe of weight changes
weightChanges = pd.DataFrame(np.diff(weights, axis = 0), columns = ["Rat1","Rat2","Rat3", "Rat4"])


# make an index
phase1 = [1] * 7
phase2 = [2] * 29
phase3 = [3] * 12
phase4 = [4] * 7
phase5 = [5] * 9
phase6 = [6] * 6

phases = phase1 + phase2 + phase3 + phase4 + phase5 + phase6

days1 = range(1,8)
days2 = range(1,30)
days3 = range(1,13)
days4 = range(1,8)
days5 = range(1,10)
days6 = range(1,7)

days = days1 + days2 + days3 + days4 + days5 + days6

arrays = [phases,days]

tuples = list(zip(*arrays))

index = pd.MultiIndex.from_tuples(tuples, names=['Phase', 'Day'])

weightChanges = weightChanges.set_index(index[1:])


w1 = weightChanges.plot(colormap = 'winter', title = "Weights Changes",figsize = (11.69,8.27))
w1.set_ylabel("Weight Change (g)")