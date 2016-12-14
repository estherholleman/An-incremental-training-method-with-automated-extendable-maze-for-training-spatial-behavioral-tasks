# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 12:46:22 2016

@author: admin
"""
#%% import pandas library to use data frames
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot') #makes plots look pretty
from pylab import savefig # may need to change this back to *

# load the results for all rats
ResultsRat1ToneTask1 = pd.read_csv('ResultsRat1ToneTask1.csv');
ResultsRat2ToneTask1 = pd.read_csv('ResultsRat2ToneTask1.csv');
ResultsRat3ToneTask1 = pd.read_csv('ResultsRat3ToneTask1.csv');
ResultsRat4ToneTask1 = pd.read_csv('ResultsRat4ToneTask1.csv');

#%% save results
ResultsRat1ToneTask1.to_csv('ResultsRat1ToneTask1.csv', index = False);
ResultsRat2ToneTask1.to_csv('ResultsRat2ToneTask1.csv', index = False);
ResultsRat3ToneTask1.to_csv('ResultsRat3ToneTask1.csv', index = False);
ResultsRat4ToneTask1.to_csv('ResultsRat4ToneTask1.csv', index = False);

#%% calculate percentage correct
totalTrials = ResultsRat1ToneTask1.count(axis = 1)
totalTrials = pd.DataFrame({'Rat 1': ResultsRat1ToneTask1.count(axis = 1) ,'Rat 2': ResultsRat2ToneTask1.count(axis = 1), 'Rat 3': ResultsRat3ToneTask1.count(axis = 1), 'Rat 4':ResultsRat4ToneTask1.count(axis = 1)});

scores = pd.DataFrame({'Rat 1': ResultsRat1ToneTask1.sum(axis = 1) ,'Rat 2': ResultsRat2ToneTask1.sum(axis = 1), 'Rat 3': ResultsRat3ToneTask1.sum(axis = 1), 'Rat 4': ResultsRat4ToneTask1.sum(axis = 1)});
scores = scores[scores  > 0];
scores = scores/totalTrials * 100

averageScores = scores.mean(1)

averagedEveryThirdDay = scores.groupby(scores.index/3).mean();

#%% plot results
scores.plot(colormap = 'winter')
plt.title('Learning curve 2', fontsize=14);
plt.xlabel('training days');
plt.ylabel('% correct');
plt.ylim(0,100)
savefig('LearningCurve1.png')


plt.figure(figsize=(11.69,8.27))
scores.plot(colormap = 'winter')
plt.title('Learning Curve Group 2', fontsize=24);
plt.ylim(0,100);
plt.xlabel('training days');
plt.ylabel('% correct');
plt.xticks(np.arange(0,len(scores),1))
plt.yticks(np.arange(0,101,5))


rcParams['figure.figsize'] = 11.69,8.27

savefig('LearningCurve1Large.png')



plt.figure(figsize=(11.69,8.27))
averageScores.plot(colormap = 'winter')
plt.title('Learning Curve Group 2', fontsize=24);
plt.ylim(0,100);
plt.xlabel('training days');
plt.ylabel('% correct');
plt.xticks(np.arange(0,len(scores),1))
plt.yticks(np.arange(0,101,5))

savefig('LearningCurve1Average.png')


# plot every 3rd score averaged
plt.figure(figsize=(11.69,8.27))
averagedEveryThirdDay.plot(colormap = 'winter')
plt.title('Learning Curve Group 1', fontsize=14);
plt.ylim(0,100);
plt.xlabel('training days');
plt.ylabel('% correct');
plt.xticks(np.arange(1,len(averagedEveryThirdDay),1),('1',  '4',  '7',));
plt.yticks(np.arange(0,101,5))


savefig('LearningCurveGroup1Smoothed.png')


averageSmoothed = averagedEveryThirdDay.mean(1);

# plot every 3rd score averaged
plt.figure(figsize=(11.69,8.27))
averageSmoothed.plot(colormap = 'winter')
plt.title('Learning Curve Group 1 Average', fontsize=14);
plt.ylim(0,100);
plt.xlabel('training days');
plt.ylabel('% correct');
plt.xticks(np.arange(1,len(averagedEveryThirdDay),1),('1',  '4',  '7', '10','13', '16', '19', '22', '25', '28', '31', '34', '37', '40'));
plt.yticks(np.arange(0,101,5))


savefig('LearningCurveGroup2AverageSmoothed.png')