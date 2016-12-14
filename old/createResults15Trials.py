# -*- coding: utf-8 -*-
"""
Created on Thu May 12 11:15:14 2016

@author: esther
"""

import pandas as pd


trials = ['blk1t1','blk1t2', 'blk1t3','blk1t4','blk1t5','blk1t6','blk1t7','blk1t8','blk1t9','blk1t10','blk1t11','blk1t12','blk1t13','blk1t14','blk1t15','blk2t1','blk2t2', 'blk2t3','blk2t4','blk2t5','blk2t6','blk2t7','blk2t8','blk2t9','blk2t10','blk2t11','blk2t12','blk2t13','blk2t14','blk2t15','blk3t1','blk3t2', 'blk3t3','blk3t4','blk3t5','blk3t6','blk3t7','blk3t8','blk3t9','blk3t10','blk3t11','blk3t12','blk3t13','blk3t14','blk3t15','blk4t1','blk4t2', 'blk4t3','blk4t4','blk4t5','blk4t6','blk4t7','blk4t8','blk4t9','blk4t10','blk4t11','blk4t12','blk4t13','blk4t14','blk4t15'];

days = ['1','2','3','4','5','6','7'];

#results = [0,1,1,0,0,1,1,1,1,0,0,1,1,0,1,0,1]

#%% make results dataframe
ResultsRat1ToneTaskMAZE = pd.DataFrame(index = days, columns = trials);
ResultsRat2ToneTaskMAZE = pd.DataFrame(index = days, columns = trials);
ResultsRat3ToneTaskMAZE = pd.DataFrame(index = days, columns = trials);
ResultsRat4ToneTaskMAZE = pd.DataFrame(index = days, columns = trials);

#%% save results
ResultsRat1ToneTaskMAZE.to_csv('ResultsRat1ToneTaskMAZE.csv', index = False);
ResultsRat2ToneTaskMAZE.to_csv('ResultsRat2ToneTaskMAZE.csv', index = False);
ResultsRat3ToneTaskMAZE.to_csv('ResultsRat3ToneTaskMAZE.csv', index = False);
ResultsRat4ToneTaskMAZE.to_csv('ResultsRat4ToneTaskMAZE.csv', index = False);