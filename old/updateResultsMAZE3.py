# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 09:20:45 2016

@author: esther
"""

import pandas as pd
from pylab import rcParams
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot') #makes plots look pretty
from pylab import savefig # may need to change this back to *
from __future__ import division

# load the results for all rats
ResultsRat1ToneTaskMAZE3_TEST = pd.read_csv('ResultsRat1ToneTaskMAZE3_6days.csv');
ResultsRat2ToneTaskMAZE3_TEST = pd.read_csv('ResultsRat2ToneTaskMAZE3_6days.csv');
ResultsRat3ToneTaskMAZE3_TEST = pd.read_csv('ResultsRat3ToneTaskMAZE3_6days.csv');
ResultsRat4ToneTaskMAZE3_TEST = pd.read_csv('ResultsRat4ToneTaskMAZE3_6days.csv');

#%% save results
ResultsRat1ToneTaskMAZE3.to_csv('ResultsRat1ToneTaskMAZE3_6days.csv', index = False);
ResultsRat2ToneTaskMAZE3.to_csv('ResultsRat2ToneTaskMAZE3_6days.csv', index = False);
ResultsRat3ToneTaskMAZE3.to_csv('ResultsRat3ToneTaskMAZE3_6days.csv', index = False);
ResultsRat4ToneTaskMAZE3.to_csv('ResultsRat4ToneTaskMAZE3_6days.csv', index = False);


#%% calculate percentage correct

totalTrials = pd.DataFrame({'Rat 1': ResultsRat1ToneTaskMAZE3_TEST.count(axis = 1) ,'Rat 2': ResultsRat2ToneTaskMAZE3_TEST.count(axis = 1), 'Rat 3': ResultsRat3ToneTaskMAZE3_TEST.count(axis = 1), 'Rat 4':ResultsRat4ToneTaskMAZE3_TEST.count(axis = 1)});

scores = pd.DataFrame({'Rat 1': ResultsRat1ToneTaskMAZE3_TEST.sum(axis = 1) ,'Rat 2': ResultsRat2ToneTaskMAZE3_TEST.sum(axis = 1), 'Rat 3': ResultsRat3ToneTaskMAZE3_TEST.sum(axis = 1), 'Rat 4': ResultsRat4ToneTaskMAZE3_TEST.sum(axis = 1)});
scores = scores[scores  > 0];
scores = scores/totalTrials * 100

averageScores = scores.mean(1)



#%% plot results
scores.plot(colormap = 'winter')
plt.title('Learning curve 2', fontsize=14);
plt.xlabel('training days');
plt.ylabel('% correct');
plt.ylim(0,100)
savefig('LearningCurveMAZE3.png')



#%% add extra training day (extra row in data frame)
ResultsRat1ToneTaskMAZE3.loc[6,:] = np.nan;
ResultsRat2ToneTaskMAZE3.loc[6,:] = np.nan;
ResultsRat3ToneTaskMAZE3.loc[6,:] = np.nan;
ResultsRat4ToneTaskMAZE3.loc[6,:] = np.nan;


scores.to_csv('scoresMAZE3.csv', index = False);