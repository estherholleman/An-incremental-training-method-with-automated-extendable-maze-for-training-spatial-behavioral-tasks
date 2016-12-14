# -*- coding: utf-8 -*-
"""
Created on Thu May 12 11:15:14 2016

@author: esther
"""

import pandas as pd


trials = ['blk1t1','blk1t2', 'blk1t3','blk1t4','blk1t5','blk1t6','blk1t7','blk1t8','blk1t9','blk1t10','blk1t11','blk1t12','blk1t13','blk1t14','blk1t15','blk1t16','blk1t17','blk1t18','blk1t19','blk1t20','blk1t21','blk1t22','blk1t23','blk1t24','blk1t25','blk2t1','blk2t2', 'blk2t3','blk2t4','blk2t5','blk2t6','blk2t7','blk2t8','blk2t9','blk2t10','blk2t11','blk2t12','blk2t13','blk2t14','blk2t15','blk2t16','blk2t17','blk2t18','blk2t19','blk2t20','blk2t21','blk2t22','blk2t23','blk2t24','blk2t25','blk3t1','blk3t2', 'blk3t3','blk3t4','blk3t5','blk3t6','blk3t7','blk3t8','blk3t9','blk3t10','blk3t11','blk3t12','blk3t13','blk3t14','blk3t15','blk3t16','blk3t17','blk3t18','blk3t19','blk3t20','blk3t21','blk3t22','blk3t23','blk3t24','blk3t25','blk4t1','blk4t2', 'blk4t3','blk4t4','blk4t5','blk4t6','blk4t7','blk4t8','blk4t9','blk4t10','blk4t11','blk4t12','blk4t13','blk4t14','blk4t15','blk4t16','blk4t17','blk4t18','blk4t19','blk4t20','blk4t21','blk4t22','blk4t23','blk4t24','blk4t25'];

days = ['1','2','3','4'];


#%% make results dataframe
ResultsRat1ToneTaskMAZE3 = pd.DataFrame(index = days, columns = trials);
ResultsRat2ToneTaskMAZE3 = pd.DataFrame(index = days, columns = trials);
ResultsRat3ToneTaskMAZE3 = pd.DataFrame(index = days, columns = trials);
ResultsRat4ToneTaskMAZE3 = pd.DataFrame(index = days, columns = trials);

#%% save results
ResultsRat1ToneTaskMAZE3.to_csv('ResultsRat1ToneTaskMAZE3_3days.csv', index = False);
ResultsRat2ToneTaskMAZE3.to_csv('ResultsRat2ToneTaskMAZE3_3days.csv', index = False);
ResultsRat3ToneTaskMAZE3.to_csv('ResultsRat3ToneTaskMAZE3_3days.csv', index = False);
ResultsRat4ToneTaskMAZE3.to_csv('ResultsRat4ToneTaskMAZE3_3days.csv', index = False);


#%% calculate percentage correct

totalTrials = pd.DataFrame({'Rat 1': ResultsRat1ToneTaskMAZE3.count(axis = 1) ,'Rat 2': ResultsRat2ToneTaskMAZE3.count(axis = 1), 'Rat 3': ResultsRat3ToneTaskMAZE3.count(axis = 1), 'Rat 4':ResultsRat4ToneTaskMAZE3.count(axis = 1)});

scores = pd.DataFrame({'Rat 1': ResultsRat1ToneTaskMAZE3.sum(axis = 1) ,'Rat 2': ResultsRat2ToneTaskMAZE3.sum(axis = 1), 'Rat 3': ResultsRat3ToneTaskMAZE3.sum(axis = 1), 'Rat 4': ResultsRat4ToneTaskMAZE3.sum(axis = 1)});
scores = scores[scores  > 0];
scores = scores/totalTrials * 100

averageScores = scores.mean(1)


# load the results for all rats
ResultsRat1ToneTask = pd.read_csv('ResultsRat1ToneTaskMAZE3_3days.csv');
ResultsRat2ToneTask = pd.read_csv('ResultsRat2ToneTaskMAZE3_3days.csv');
ResultsRat3ToneTask = pd.read_csv('ResultsRat3ToneTaskMAZE3_3days.csv');
ResultsRat4ToneTask = pd.read_csv('ResultsRat4ToneTaskMAZE3_3days.csv');