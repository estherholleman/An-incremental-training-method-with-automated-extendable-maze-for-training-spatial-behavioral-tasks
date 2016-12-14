# -*- coding: utf-8 -*-
"""
Created on Thu May 12 12:31:07 2016

@author: esther
"""

#%% import pandas library to use data frames
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot') #makes plots look pretty
from pylab import savefig # may need to change this back to *


# load the results for all rats
ResultsRat1ToneTask2 = pd.read_csv('ResultsRat1ToneTask2.csv');
ResultsRat2ToneTask2 = pd.read_csv('ResultsRat2ToneTask2.csv');
ResultsRat3ToneTask2 = pd.read_csv('ResultsRat3ToneTask2.csv');
ResultsRat4ToneTask2 = pd.read_csv('ResultsRat4ToneTask2.csv');

#resultspath = os.path.join('C:\Users\admin\Desktop\Feeders_setup_v4\experiments\Results')

#%% add date of training session to index
ResultsRat1ToneTask2.index = range(1,42);
ResultsRat2ToneTask2.index = range(1,42);
ResultsRat3ToneTask2.index = range(1,42);
ResultsRat4ToneTask2.index = range(1,42);


#%% add extra training day (extra row in data frame)
ResultsRat1ToneTask2.loc['30/06/2016',:] = 0;
ResultsRat2ToneTask2.loc['30/06/2016',:] = 0;
ResultsRat3ToneTask2.loc['30/06/2016',:] = 0;
ResultsRat4ToneTask2.loc['30/06/2016',:] = 0;

## at this point manually fill in the results

#%% save results
ResultsRat1ToneTask2.to_csv('ResultsRat1ToneTask2.csv', index = False);
ResultsRat2ToneTask2.to_csv('ResultsRat2ToneTask2.csv', index = False);
ResultsRat3ToneTask2.to_csv('ResultsRat3ToneTask2.csv', index = False);
ResultsRat4ToneTask2.to_csv('ResultsRat4ToneTask2.csv', index = False);

#%% calculate percentage correct
totalTrials = ResultsRat1ToneTask2.count(axis = 1)
totalTrials = pd.DataFrame({'Rat 1': ResultsRat1ToneTask2.count(axis = 1) ,'Rat 2': ResultsRat2ToneTask2.count(axis = 1), 'Rat 3': ResultsRat3ToneTask2.count(axis = 1), 'Rat 4':ResultsRat4ToneTask2.count(axis = 1)});

scores = pd.DataFrame({'Rat 1': ResultsRat1ToneTask2.sum(axis = 1) ,'Rat 2': ResultsRat2ToneTask2.sum(axis = 1), 'Rat 3': ResultsRat3ToneTask2.sum(axis = 1), 'Rat 4': ResultsRat4ToneTask2.sum(axis = 1)});
scores = scores[scores  > 0];
scores = scores/totalTrials * 100


#%% plot results
scores.plot(colormap = 'winter')
plt.title('Learning curve 2', fontsize=14);
plt.xlabel('training days');
plt.ylabel('% correct');
plt.ylim(0,100)
savefig('LearningCurve2.png')








