# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 17:03:28 2016

@author: esther
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib
matplotlib.style.use('ggplot') #makes plots look pretty
from pylab import savefig # may need to change this back to *


makeBins.py

phase1 = [1] * 210
phase2 = [2] * 1740
phase3 = [3] * 720
phase4 = [4] * 420
phase5 = [5] * 720
phase6 = [6] * 600

phases = phase1 + phase2 + phase3 + phase4 + phase5 + phase6

arrays = [phases,Bins]

tuples = list(zip(*arrays))

index = pd.MultiIndex.from_tuples(tuples, names=['Phase', 'Bin'])

AllScoresIndx = AllScores.set_index(index)

AllScoresSummed = AllScoresIndx.sum(axis = 0,level = "Bin")

totalTrials = AllScoresIndx.count(axis = 0, level = "Bin");

ScoresBinned = AllScoresSummed/totalTrials * 100

plt.figure(figsize=(11.69,8.27))
ScoresBinned.plot(colormap = 'winter')
plt.title('Learning Curve Group 2', fontsize=14);
plt.ylim(0,100);
plt.xlabel('Trials');
plt.ylabel('% Correct');


avgs = ScoresBinned.mean(axis=1)
stds = ScoresBinned.std(axis=1)

avgs.plot(yerr = stds)

t = range(0,len(avgs))

plt.figure(figsize=(11.69,8.27))

plt.title('Learning Curve Group 2', fontsize=14);
plt.ylim(0,100);
plt.xlabel('Trials');
plt.ylabel('% correct');
ax = avgs.plot(colormap = 'winter')
ax.fill_between(t, avgs-stds, avgs+stds, color='b', alpha=0.2)
