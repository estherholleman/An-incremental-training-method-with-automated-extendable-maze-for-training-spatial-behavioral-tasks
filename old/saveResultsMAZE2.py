# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 09:27:33 2016

@author: esther
"""

import pandas as pd

ResultsRat1ToneTaskMAZE2 = pd.read_csv('ResultsRat1ToneTaskMAZE2_7days.csv');
ResultsRat2ToneTaskMAZE2 = pd.read_csv('ResultsRat2ToneTaskMAZE2_7days.csv');
ResultsRat3ToneTaskMAZE2 = pd.read_csv('ResultsRat3ToneTaskMAZE2_7days.csv');
ResultsRat4ToneTaskMAZE2 = pd.read_csv('ResultsRat4ToneTaskMAZE2_7days.csv');


#%% add date of training session to index
ResultsRat1ToneTaskMAZE2.index = range(1,10);
ResultsRat2ToneTaskMAZE2.index = range(1,10);
ResultsRat3ToneTaskMAZE2.index = range(1,10);
ResultsRat4ToneTaskMAZE2.index = range(1,10);


#%% save results
ResultsRat1ToneTaskMAZE2.to_csv('ResultsRat1ToneTaskMAZE2_9days.csv', index = False);
ResultsRat2ToneTaskMAZE2.to_csv('ResultsRat2ToneTaskMAZE2_9days.csv', index = False);
ResultsRat3ToneTaskMAZE2.to_csv('ResultsRat3ToneTaskMAZE2_9days.csv', index = False);
ResultsRat4ToneTaskMAZE2.to_csv('ResultsRat4ToneTaskMAZE2_9days.csv', index = False);


scores.to_csv('scoresToneTaskMAZE2_7days.csv', index = False);

# add extra row
ResultsRat1ToneTaskMAZE2.loc['9',:] = 0;
ResultsRat2ToneTaskMAZE2.loc['9',:] = 0;
ResultsRat3ToneTaskMAZE2.loc['9',:] = 0;
ResultsRat4ToneTaskMAZE2.loc['9',:] = 0;