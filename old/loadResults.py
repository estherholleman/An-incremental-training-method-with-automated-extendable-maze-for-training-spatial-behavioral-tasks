# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 10:13:00 2016

@author: esther
"""

#%% load the results for all rats TT1
ResultsRat1ToneTask1 = pd.read_csv('ResultsRat1ToneTask1.csv');
ResultsRat2ToneTask1 = pd.read_csv('ResultsRat2ToneTask1.csv');
ResultsRat3ToneTask1 = pd.read_csv('ResultsRat3ToneTask1.csv');
ResultsRat4ToneTask1 = pd.read_csv('ResultsRat4ToneTask1.csv');


#%% load the results for all rats TT2
ResultsRat1ToneTask2 = pd.read_csv('ResultsRat1ToneTask2.csv');
ResultsRat2ToneTask2 = pd.read_csv('ResultsRat2ToneTask2.csv');
ResultsRat3ToneTask2 = pd.read_csv('ResultsRat3ToneTask2.csv');
ResultsRat4ToneTask2 = pd.read_csv('ResultsRat4ToneTask2.csv');


#%% load the results for all rats MAZE
#ResultsRat1ToneTaskMAZE = pd.read_csv('ResultsRat1ToneTaskMAZE.csv');
#ResultsRat2ToneTaskMAZE = pd.read_csv('ResultsRat2ToneTaskMAZE.csv');
#ResultsRat3ToneTaskMAZE = pd.read_csv('ResultsRat3ToneTaskMAZE.csv');
#ResultsRat4ToneTaskMAZE = pd.read_csv('ResultsRat4ToneTaskMAZE.csv');



#%% save results
ResultsRat1ToneTaskMAZE.to_csv('ResultsRat1ToneTaskMAZE.csv', index = False);
ResultsRat2ToneTaskMAZE.to_csv('ResultsRat2ToneTaskMAZE.csv', index = False);
ResultsRat3ToneTaskMAZE.to_csv('ResultsRat3ToneTaskMAZE.csv', index = False);
ResultsRat4ToneTaskMAZE.to_csv('ResultsRat4ToneTaskMAZE.csv', index = False);

ResultsRat4ToneTaskMAZE_TEST = pd.read_csv('ResultsRat4ToneTaskMAZE.csv');