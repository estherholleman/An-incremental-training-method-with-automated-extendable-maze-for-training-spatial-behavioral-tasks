# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 12:17:11 2016

@author: esther
"""

from pylab import rcParams
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot') #makes plots look pretty
from pylab import savefig # may need to change this back to *

#%% calculate percentage correct

totalTrialsMAZE = pd.DataFrame({'Rat 1': ResultsRat1ToneTaskMAZE.count(axis = 1) ,'Rat 2': ResultsRat2ToneTaskMAZE.count(axis = 1), 'Rat 3': ResultsRat3ToneTaskMAZE.count(axis = 1), 'Rat 4':ResultsRat4ToneTaskMAZE.count(axis = 1)});

scoresMAZE = pd.DataFrame({'Rat 1': ResultsRat1ToneTaskMAZE.sum(axis = 1) ,'Rat 2': ResultsRat2ToneTaskMAZE.sum(axis = 1), 'Rat 3': ResultsRat3ToneTaskMAZE.sum(axis = 1), 'Rat 4': ResultsRat4ToneTaskMAZE.sum(axis = 1)});
scoresMAZE = scoresMAZE[scoresMAZE  > 0];
scoresMAZE = scoresMAZE/totalTrialsMAZE * 100

averageScores = scoresMAZE.mean(1)

averagedEveryThirdDay = scoresMAZE.groupby(scoresMAZE.index/3).mean();
averagedEveryFifthDay = scoresMAZE.groupby(scoresMAZE.index/5).mean();


#%% plot scores
plt.figure(figsize=(11.69,8.27))
scores.plot(colormap = 'winter')
plt.title('Learning Curve Group 2', fontsize=14);
plt.ylim(0,100);
plt.xlabel('training days');
plt.ylabel('% correct');
plt.xticks(np.arange(1,len(scores)+1,1.0))
plt.yticks(np.arange(0,101,5))


rcParams['figure.figsize'] = 30, 20

savefig('LearningCurveGroup2Huge.png')

averageScores = scores.mean(1)


plt.figure(figsize=(11.69,8.27))
averageScores.plot(colormap = 'winter')
plt.title('Learning Curve Group 2', fontsize=24);
plt.ylim(0,100);
plt.xlabel('training days');
plt.ylabel('% correct');
plt.xticks(np.arange(0,len(scores),1))
plt.yticks(np.arange(0,101,5))



averagedEveryThirdDay = scores.groupby(scores.index/3).mean();
averagedEveryFifthDay = scores.groupby(scores.index/5).mean();
