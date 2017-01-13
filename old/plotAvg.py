# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 11:37:27 2016

@author: esther
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patch
import matplotlib
matplotlib.style.use('ggplot') #makes plots look pretty

ScoresBinned = pd.read_csv("ScoresBinnedPer100.csv")
ScoresBinned  = ScoresBinned.set_index("Bin",drop = True)

## plot averages
avgs = ScoresBinned.mean(axis=1)
stds = ScoresBinned.std(axis=1)
t = avgs.index
#avgs.plot(yerr = stds)

# plot without phases in background
plt.figure(figsize=(11.69,8.27))
avgs.plot(colormap = 'winter')
plt.title('Learning Curve Group 2', fontsize=14);
plt.ylim(0,100);
plt.xlabel('Trials');
plt.ylabel('% correct');
#t = range(1,avgs.index[41]+1)
plt.fill_between(t, avgs-stds, avgs+stds, color='b', alpha=0.2)


# plot with phases in background
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
for p in [
    patch.Rectangle(
        (0.1, 0.1), 210, 99.9,
        alpha=0.4,
        facecolor = "#580029"
    ),
  
    patch.Rectangle(
        (210, 0.1), 1740, 99.9,
        alpha=0.35,
        facecolor = "#681f4c"
    ),

    patch.Rectangle(
        (1950, 0.1), 720, 99.9,
        alpha=0.3,
        facecolor = "#681f4c"
   ),
    patch.Rectangle(
        (2670, 0.1), 420, 99.9,
        alpha=0.3,
        facecolor = "#890045"
    ),
    patch.Rectangle(
        (3090, 0.1), 720, 99.9,
        alpha=0.2,
        facecolor = "#9e015f"
    ),
    patch.Rectangle(
        (3810, 0.1), 600, 99.9,
        alpha=0.1,
        facecolor = "#9e015f"
    ),
]:
    ax1.add_patch(p)
    
ax2 = avgs.plot(ax = ax1,colormap = 'winter', title = "Learning Curves Averaged Group 2",figsize = (11.69,8.27))
ax2.set_xlabel("Trials")
ax2.set_ylabel("% Correct")
ax2.fill_between(t, avgs-stds, avgs+stds, color='b', alpha=0.2)

plt.savefig("AveragesBinnedPer100Trials.eps",format = "eps")
plt.savefig("AveragesBinnedPer100Trials.png",format = "png")


