# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 09:08:48 2016

@author: esther
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patch
import matplotlib
matplotlib.style.use('ggplot') #makes plots look pretty


weights = pd.read_csv("/home/esther/Desktop/BehavioralTraining/extra/weights/Weights.csv")


PhaseLengths = [];
phases = range(1,7)
phase = 1

for phase in phases:  
    PhaseLengths.append(len(weights.iloc[weights.index.get_level_values('Phase') == phase]))

DaysInPhase = np.cumsum(PhaseLengths)

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
for p in [
    patch.Rectangle(
        (0.1, 400), PhaseLengths[0], 119.9,
        alpha=0.4,
        facecolor = "#580029"
    ),
  
    patch.Rectangle(
        (DaysInPhase[0], 400), PhaseLengths[1], 119.9,
        alpha=0.35,
        facecolor = "#681f4c"
    ),

    patch.Rectangle(
        (DaysInPhase[1], 400), PhaseLengths[2], 119.9,
        alpha=0.4,
        facecolor = "#FA8072"
   ),
    patch.Rectangle(
        (DaysInPhase[2], 400), PhaseLengths[3], 119.9,
        alpha=0.35,
        facecolor = "#890045"
    ),
    patch.Rectangle(
        (DaysInPhase[3],400), PhaseLengths[4], 119.9,
        alpha=0.2,
        facecolor = "#9e015f"
    ),
    patch.Rectangle(
        (DaysInPhase[4], 400), PhaseLengths[5], 119.9,
        alpha=0.5,
        facecolor = "#F08080"
    )
]:
    ax1.add_patch(p)
    

ax2 = weights.plot(ax = ax1,colormap = 'winter', title = "Weights Group 2",figsize = (11.69,8.27))

patches,labels = ax2.get_legend_handles_labels()
ax2.legend(patches,labels,loc=4)
ax2.set_xlabel("(Phase,Trial)")
ax2.set_ylabel("Weight(grams)")

#plt.savefig("weightsTest.eps",format = "eps")
#plt.savefig("weightsTest.png",format = "png")