# -*- coding: utf-8 -*-
"""
Created on Thu May 12 11:15:14 2016

@author: esther
"""

import pandas as pd


trials = ['blk1t1','blk1t2', 'blk1t3','blk1t4','blk1t5','blk1t6','blk1t7','blk1t8','blk1t9','blk1t10','blk2t1','blk2t2', 'blk2t3','blk2t4','blk2t5','blk2t6','blk2t7','blk2t8','blk2t9','blk2t10','blk3t1','blk3t2', 'blk3t3','blk3t4','blk3t5','blk3t6','blk3t7','blk3t8','blk3t9','blk3t10'];

days = ['1','2','3','4','5','6','7'];


#%% make results dataframe
ToneTask1Rat1 = pd.DataFrame(index = days, columns = trials);
ToneTask1Rat2 = pd.DataFrame(index = days, columns = trials);
ToneTask1Rat3 = pd.DataFrame(index = days, columns = trials);
ToneTask1Rat4 = pd.DataFrame(index = days, columns = trials);

#%% save results
ToneTask1Rat1.to_csv('ToneTask1Rat1.csv', index = False);
ToneTask1Rat2.to_csv('ToneTask1Rat2.csv', index = False);
ToneTask1Rat3.to_csv('ToneTask1Rat3.csv', index = False);
ToneTask1Rat4.to_csv('ToneTask1Rat4.csv', index = False);