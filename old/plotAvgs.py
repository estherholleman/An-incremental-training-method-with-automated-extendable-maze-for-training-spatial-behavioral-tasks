# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 13:39:04 2016

@author: esther
"""

from pylab import rcParams
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot') #makes plots look pretty
from pylab import savefig # may need to change this back to *

avgs = AllScoresWithIndx.mean(axis=1)
stds = AllScoresWithIndx.std(axis=1)

avg3days = allScores.groupby(allScores.index/3).mean();

avgs.plot(yerr = stds)

plt.figure(figsize=(11.69,8.27))
avgs.plot(colormap = 'winter')
plt.title('Learning Curve Group 2', fontsize=14);
plt.ylim(0,100);
plt.xlabel('training days');
plt.ylabel('% correct');

t = range(0,len(avgs))
avgs.plot(color='b')
plt.fill_between(t, avgs-stds, avgs+stds, color='b', alpha=0.2)
