# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 12:20:21 2016

@author: esther
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from itertools import groupby


# load in manually scored data
Mdat = pd.read_csv("ManualScores.csv",index_col = ["Phase","Day","Block","Trial"])
Mdat.columns = [u'1', u'2', u'3', u'4']

# load in automatically scored data
Adat = pd.read_csv("AutoData.csv",header=[0,1],index_col = [0,1,2,3], tupleize_cols=False )


#%% Manual Scoring

Mdatsummed = Mdat.sum(axis = 0,level = ["Phase","Day"])
countGroups = Mdat.groupby(level = ["Phase","Day"])
scoresMdat = Mdatsummed/countGroups.count(axis=0) * 100
scoresMdat = scoresMdat.interpolate()




#%% Automatic Scoring
## testing scores without the timed out trials
sides =  Adat.xs('side',level = 1, axis = 1) 

# get animal choices
choices = Adat.xs('animal_answer',level = 1, axis = 1) 
# replace the timed out trials (animal answer = 2) 
choiceNo2 = choices.copy()
choiceNo2[choices == 2] = np.nan


# analyze alternations in animal choices
choiceDiff = abs(choiceNo2.diff(axis = 0))
choiceDiffSum = choiceDiff.sum(axis = 0,level = ["Phase","Day"])
countGroups = choiceDiff.groupby(level = ["Phase","Day"])
altScoreAnimal = choiceDiffSum/countGroups.count(axis=0) * 100


# analyze alternations in randomization
sidesDiff = abs(sides.diff(axis = 0))
sidesDiffSum = sidesDiff.sum(axis = 0,level = ["Phase","Day"])
countGroups = sidesDiff.groupby(level = ["Phase","Day"])
altScoreRand = sidesDiffSum/countGroups.count(axis=0) * 100


#%% analyze alternations in animal choices BY PHASE ONLY
choiceDiff = abs(choiceNo2.diff(axis = 0))
choiceDiffSum = choiceDiff.sum(axis = 0,level = ["Phase"])
countGroups = choiceDiff.groupby(level = ["Phase"])
altScoreAnimal = choiceDiffSum/countGroups.count(axis=0) * 100


# analyze alternations in randomization
sidesDiff = abs(sides.diff(axis = 0))
sidesDiffSum = sidesDiff.sum(axis = 0,level = ["Phase"])
countGroups = sidesDiff.groupby(level = ["Phase"])
altScoreRand = sidesDiffSum/countGroups.count(axis=0) * 100



#%% normalized alternation score (1 = alternating exactly like the  randomization)
altScore = altScoreAnimal/altScoreRand

ax = altScore.plot()
plt.axhline(y =1,xmin = 0, xmax=1, linewidth = 2, color = 'black', ls ="--")
ax.legend(numpoints = 1, loc = 'upper left')
#


#%%%

altScoreAnimal['Animal/Rand'] = 'Animal'
altScoreAnimal.set_index('Animal/Rand', append = True, inplace = True)
altScoreAnimal = altScoreAnimal.reorder_levels(['Animal/Rand', 'Phase', 'Day'])
altScoreAnimal = altScoreAnimal.unstack(level=0).reorder_levels([1,0], axis=1)


altScoreRand['Animal/Rand'] = 'Rand'
altScoreRand.set_index('Animal/Rand', append = True, inplace = True)
altScoreRand = altScoreRand.reorder_levels(['Animal/Rand', 'Phase', 'Day'])
altScoreRand = altScoreRand.unstack(level=0).reorder_levels([1,0], axis=1)


# now join the two together
altScores = altScoreAnimal.join(altScoreRand)
animals = ["1","2","3","4"]

for animal in animals:

    # indexing 
    rat = pd.DataFrame(altScores['Animal',animal])
    alt = rat.join(altScores['Rand',animal])
    alt.columns = alt.columns.droplevel(level = 1)
    
    
    groups = alt.groupby(level = ["Phase"])
    
    fig, ax = plt.subplots(figsize = (11.69,8.27))
    for name, group in groups:
        figname = "Alternations Rat" + animal
        ax.plot(group.Rand,group.Animal, marker='o', linestyle='', ms=6, label= "Phase " + str(name), )
        ax.legend(numpoints = 1, loc = 'bottom right')
        ax.set(xlim=(0,100), ylim=(0,100))
        ax.set_xlabel("Randomization Alternation")
        ax.set_ylabel("Animal Alternation")
        ax.set_title(figname)
        unity_line = ax.plot(ax.get_xlim(), ax.get_ylim(), ls="--", c=".3")   
        plt.savefig(figname +".eps",format = "eps")
        plt.savefig(figname + ".png",format = "png")





#ax = altScores.plot.scatter(x=altScores['Animal','1'], y=altScores['Rand','1'], color='DarkBlue', label='Group 1');
#altScores.plot.scatter(x=altScores['Animal','2'], y=altScores['Rand','2'], color='DarkGreen', label='Group 2', ax=ax);
#
#plt.scatter(altScores['Animal','1'], altScores['Rand','1'], color='DarkBlue', label='Group 1');
#plt.scatter(altScores['Animal','2'], altScores['Rand','2'], color='DarkGreen', label='Group 2');
#
#phaseGroups = altScoreRand.groupby(level = ["Phase"])
#
#f, ax = plt.subplots()
#ax.scatter(altScoreAnimal,altScoreRand)
#    
#ax.set(xlim=(0,100), ylim=(0,100))
#unity_line = ax.plot(ax.get_xlim(), ax.get_ylim(), ls="--", c=".3")
#
#def on_change(axes):
#    # When this function is called it checks the current
#    # values of xlim and ylim and modifies diag_line
#    # accordingly.
#    x_lims = ax.get_xlim()
#    y_lims = ax.get_ylim()
#    unity_line.set_data(x_lims, y_lims)
#
## Connect two callbacks to your axis instance.
## These will call the function "on_change" whenever
## xlim or ylim is changed.
#ax.callbacks.connect('xlim_changed', on_change)
#ax.callbacks.connect('ylim_changed', on_change)
#
#plt.show()