# -*- coding: utf-8 -*-
"""
Created on Fri May 13 14:48:03 2016

@author: ana
"""

import pandas as pd

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