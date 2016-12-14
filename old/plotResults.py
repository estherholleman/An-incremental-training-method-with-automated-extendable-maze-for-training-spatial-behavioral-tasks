# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 12:46:22 2016

@author: admin
"""

from pylab import rcParams
import numpy as n

#%% calculate percentage correct
totalTrials = ResultsRat1ToneTask2.count(axis = 1)
totalTrials = pd.DataFrame({'Rat 1': ResultsRat1ToneTask2.count(axis = 1) ,'Rat 2': ResultsRat2ToneTask2.count(axis = 1), 'Rat 3': ResultsRat3ToneTask2.count(axis = 1), 'Rat 4':ResultsRat4ToneTask2.count(axis = 1)});

scores = pd.DataFrame({'Rat 1': ResultsRat1ToneTask2.sum(axis = 1) ,'Rat 2': ResultsRat2ToneTask2.sum(axis = 1), 'Rat 3': ResultsRat3ToneTask2.sum(axis = 1), 'Rat 4': ResultsRat4ToneTask2.sum(axis = 1)});
scores = scores[scores  > 0];
scores = scores/totalTrials * 100

averageScores = scores.mean(1)

averagedEveryThirdDay = scores.groupby(scores.index/3).mean();
averagedEveryFifthDay = scores.groupby(scores.index/5).mean();


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


## plot average scores
plt.figure(figsize=(11.69,8.27))
averageScores.plot(colormap = 'winter')
plt.title('Learning Curve Group 2', fontsize=12);
plt.ylim(0,100);
plt.xlabel('training days');
plt.ylabel('% correct');
plt.xticks(np.arange(0,len(scores),1))
plt.yticks(np.arange(0,101,5))

savefig('LearningCurveGroup2Average.png')

# plot every 3rd score averaged
plt.figure(figsize=(11.69,8.27))
averagedEveryThirdDay.plot(colormap = 'winter')
plt.title('Learning Curve Group 2', fontsize=14);
plt.ylim(0,100);
plt.xlabel('training days');
plt.ylabel('% correct');
plt.xticks(np.arange(1,len(averagedEveryThirdDay),1),('1',  '4',  '7', '10','13', '16', '19', '22', '25', '28', '31', '34', '37', '40'));
plt.yticks(np.arange(0,101,5))


savefig('LearningCurveGroup2Smoothed.png')


averageSmoothed = averagedEveryThirdDay.mean(1);



plt.figure(figsize=(11.69,8.27))
averagedEveryFifthDay.plot(colormap = 'winter')
plt.title('Learning Curve Group 2', fontsize=14);
plt.ylim(0,100);
plt.xlabel('training days');
plt.ylabel('% correct');
plt.xticks(np.arange(1,len(averagedEveryFifthDay),1),('1',  '6',  '11', '16','21', '26', '31', '36'));
plt.yticks(np.arange(0,101,5))


savefig('LearningCurveGroup2Smoothed5days.png')




averageSmoothedFiveDays = averagedEveryFifthDay.mean(1);






# plot average of every 3rd score averaged
plt.figure(figsize=(11.69,8.27))
averageSmoothedFiveDays.plot(colormap = 'winter')
plt.title('Learning Curve Group 2', fontsize=14);
plt.ylim(0,100);
plt.xlabel('training days');
plt.ylabel('% correct');
plt.xticks(np.arange(1,len(averagedEveryFifthDay),1),('1',  '6',  '11', '16','21', '26', '31', '36'));
plt.yticks(np.arange(0,101,5))


savefig('LearningCurveGroup2AverageSmoothedFiveDays.png')

