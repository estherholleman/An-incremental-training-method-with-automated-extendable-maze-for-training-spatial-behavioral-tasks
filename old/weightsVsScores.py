# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 14:06:15 2016

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

#%%load in scores and calculate changes between days
scores = pd.read_csv("ScoresPerDay.csv")

Scores = scores[1:]

scoreChanges = pd.DataFrame(np.diff(scores, axis = 0), columns = ["Rat1","Rat2","Rat3", "Rat4"], index = index[1:])



#plt.plot(weightChanges,scoreChanges,'o')


#%% another option is to use polyfit from numpy
fig1, ax = plt.subplots()
plt.plot(weights,scores,'.')
plt.legend(["Rat1","Rat2","Rat3", "Rat4"],numpoints=1)
#ax.scatter(weightChanges,Scores)
ax.set_xlabel('weight change')
ax.set_ylabel('% correct')
x_min, x_max = ax.get_xlim()
ax.set_xlim([-20, 20])
ax.set_ylim([30, 100])


slope1, intercept1 = np.polyfit(weightChanges['Rat1'],Scores['Rat1'],1)
ax.plot(weightChanges['Rat1'],weightChanges['Rat1']*slope1 + intercept1,'r')

slope2, intercept2 = np.polyfit(weightChanges['Rat2'],Scores['Rat2'],1)
ax.plot(weightChanges['Rat2'],weightChanges['Rat2']*slope2 + intercept2,'c')

slope3, intercept3 = np.polyfit(weightChanges['Rat3'],Scores['Rat3'],1)
ax.plot(weightChanges['Rat3'],weightChanges['Rat3']*slope3 + intercept3,'m')

slope4, intercept4 = np.polyfit(weightChanges['Rat4'],Scores['Rat4'],1)
ax.plot(weightChanges['Rat4'],weightChanges['Rat4']*slope4 + intercept4,'y')

#%% find slope and intercept using linregress
#slopeRat1, interceptRat1, r_valueRat1, p_valueRat1, std_errRat1 = stats.linregress(weightChanges['Rat1'],scoreChanges['Rat1'])
#slopeRat2, interceptRat2, r_valueRat2, p_valueRat2, std_errRat2 = stats.linregress(weightChanges['Rat2'],scoreChanges['Rat2'])
#slopeRat3, interceptRat3, r_valueRat3, p_valueRat3, std_errRat3 = stats.linregress(weightChanges['Rat3'],scoreChanges['Rat3'])
#slopeRat4, interceptRat4, r_valueRat4, p_valueRat4, std_errRat4 = stats.linregress(weightChanges['Rat4'],scoreChanges['Rat4'])

#slopeRat1, interceptRat1, r_valueRat1, p_valueRat1, std_errRat1 = stats.linregress(weightChanges['Rat1'],Scores['Rat1'])
#slopeRat2, interceptRat2, r_valueRat2, p_valueRat2, std_errRat2 = stats.linregress(weightChanges['Rat2'],Scores['Rat2'])
#slopeRat3, interceptRat3, r_valueRat3, p_valueRat3, std_errRat3 = stats.linregress(weightChanges['Rat3'],Scores['Rat3'])
#slopeRat4, interceptRat4, r_valueRat4, p_valueRat4, std_errRat4 = stats.linregress(weightChanges['Rat4'],Scores['Rat4'])
#
slopeRat1, interceptRat1, r_valueRat1, p_valueRat1, std_errRat1 = stats.linregress(weights['Rat1'],scores['Rat1'])
slopeRat2, interceptRat2, r_valueRat2, p_valueRat2, std_errRat2 = stats.linregress(weights['Rat2'],scores['Rat2'])
slopeRat3, interceptRat3, r_valueRat3, p_valueRat3, std_errRat3 = stats.linregress(weights['Rat3'],scores['Rat3'])
slopeRat4, interceptRat4, r_valueRat4, p_valueRat4, std_errRat4 = stats.linregress(weights['Rat4'],scores['Rat4'])



#%%plot change in weight against changes in scores
fig1, ax = plt.subplots()
ax.scatter(weights,scores)
ax.set_xlabel('weights')
ax.set_ylabel('% correct')
x_min, x_max = ax.get_xlim()
#ax.set_xlim([-20, 20])
#ax.set_ylim([30, 100])


y_min1, y_max1 = interceptRat1, interceptRat1 + slopeRat1*(x_max-x_min)
ax.plot([x_min, x_max], [y_min1, y_max1],'m')

y_min2, y_max2 = interceptRat2, interceptRat2 + slopeRat2*(x_max-x_min)
ax.plot([x_min, x_max], [y_min2, y_max2],'r')

y_min3, y_max3 = interceptRat3, interceptRat3 + slopeRat3*(x_max-x_min)
ax.plot([x_min, x_max], [y_min3, y_max3],'y')

y_min4, y_max4 = interceptRat4, interceptRat4 + slopeRat4*(x_max-x_min)
ax.plot([x_min, x_max], [y_min4, y_max4],'c')
