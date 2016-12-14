# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 16:48:46 2016

@author: esther
"""

#%% save results
ToneTask1Rat1.to_csv('ToneTask1Rat1.csv', index = False);
ToneTask1Rat2.to_csv('ToneTask1Rat2.csv', index = False);
ToneTask1Rat3.to_csv('ToneTask1Rat3.csv', index = False);
ToneTask1Rat4.to_csv('ToneTask1Rat4.csv', index = False);

#%%Read in for testing
ToneTask1RAT1Test = pd.read_csv("ToneTask1Rat1.csv")
ToneTask1RAT2Test = pd.read_csv("ToneTask1Rat2.csv")
ToneTask1RAT3Test = pd.read_csv("ToneTask1Rat3.csv")
ToneTask1RAT4Test = pd.read_csv("ToneTask1Rat4.csv")