# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 17:17:28 2016

@author: esther
"""
from scipy import signal
from scipy import stats


## find the impact of weight on scores

# import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patch
import matplotlib
matplotlib.style.use('ggplot')


from myFunctions import loadData
from myFunctions import preProcessChoices
from myFunctions import scoreChoices
from myFunctions import calcScoresPerDay



Adat,Mdat = loadData()
choices,sides = preProcessChoices(Adat,Mdat)
validTrials, correct, incorrect, nTotalTrials = scoreChoices(Adat, choices, sides)


ScoresPerDay = calcScoresPerDay(correct, nTotalTrials)




def getWeights():
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
    
    weights = weights.set_index(index)
    weightChanges = weightChanges.set_index(index[1:])
    
    return weights,weightChanges


weights,weightChanges = getWeights()





fig1, ax = plt.subplots()
plt.plot(weights,ScoresPerDay,'.')
plt.legend(["Rat1","Rat2","Rat3", "Rat4"],numpoints=1)
#ax.scatter(weightChanges,Scores)
ax.set_xlabel('weight')
ax.set_ylabel('% correct')
#x_min, x_max = ax.get_xlim()
#ax.set_xlim([-20, 20])
#ax.set_ylim([30, 100])


slope1, intercept1 = np.polyfit(weights['Rat1'],ScoresPerDay['1'],1)
ax.plot(weights['Rat1'],weights['Rat1']*slope1 + intercept1,'r')

slope2, intercept2 = np.polyfit(weights['Rat2'],ScoresPerDay['2'],1)
ax.plot(weights['Rat2'],weights['Rat2']*slope2 + intercept2,'c')

slope3, intercept3 = np.polyfit(weights['Rat3'],ScoresPerDay['3'],1)
ax.plot(weights['Rat3'],weights['Rat3']*slope3 + intercept3,'m')

slope4, intercept4 = np.polyfit(weights['Rat4'],ScoresPerDay['4'],1)
ax.plot(weights['Rat4'],weights['Rat4']*slope4 + intercept4,'y')



fig2, ax = plt.subplots()
plt.plot(weightChanges,ScoresPerDay[1:],'.')
plt.legend(["Rat1","Rat2","Rat3", "Rat4"],numpoints=1)
#ax.scatter(weightChanges,Scores)
ax.set_xlabel('Weight Change Between Days (grams)')
ax.set_ylabel('% correct')
ax.set_title('Influence of Weight Changes on Scores')

#x_min, x_max = ax.get_xlim()
#ax.set_xlim([-20, 20])
#ax.set_ylim([30, 100])


slope1, intercept1 = np.polyfit(weightChanges['Rat1'],ScoresPerDay[1:]['1'],1)
ax.plot(weightChanges['Rat1'],weightChanges['Rat1']*slope1 + intercept1, c = "#ee3e03")

slope2, intercept2 = np.polyfit(weightChanges['Rat2'],ScoresPerDay[1:]['2'],1)
ax.plot(weightChanges['Rat2'],weightChanges['Rat2']*slope2 + intercept2, c ='#5792bf')

slope3, intercept3 = np.polyfit(weightChanges['Rat3'],ScoresPerDay[1:]['3'],1)
ax.plot(weightChanges['Rat3'],weightChanges['Rat3']*slope3 + intercept3,c ='#a991b6')

slope4, intercept4 = np.polyfit(weightChanges['Rat4'],ScoresPerDay[1:]['4'],1)
ax.plot(weightChanges['Rat4'],weightChanges['Rat4']*slope4 + intercept4,c ='#908e94')


plt.savefig("InfluenceOfWeightChangesOnScores.eps",format = "eps")
plt.savefig("InfluenceOfWeightChangesOnScores.png",format = "png")