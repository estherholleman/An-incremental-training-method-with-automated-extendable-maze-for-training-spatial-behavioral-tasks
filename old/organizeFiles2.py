# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 14:51:28 2015

@author: esther
"""

#import necessary libraries/packages
from __future__ import division
import os
import glob
import pandas as pd
import matplotlib.pyplot as plt

# function definition to chunck data together   
def chunker(seq, size):
    return (seq[pos:pos + size] for pos in xrange(0, len(seq), size))


## read in all data
frame = pd.DataFrame()
allBlocks = []

#cd to trial data folder
os.chdir('trial_data/')

# list all folders (&files) in directory
days = os.listdir(os.curdir)
# arrange folders in order of days
days.sort()

#loop over all training day folders
for day in days:
    #open folder of training day
    os.chdir(day)
    # list all folders (&files) in directory
    blocks = os.listdir(os.curdir)
    blocks.sort()
    
    for b in blocks:
        #open folder of training day
        os.chdir(b)
        scores = glob.glob("*.csv")
        for score in scores:
            
            df = pd.read_csv(score,index_col=None, header=0)
            df['Animal'] = score[7]
            df['Day'] = day[4:]
            df['Block'] = b[6]
            
            allBlocks.append(df)
        
        frame = pd.concat(allBlocks)
        
        os.chdir('..')
        
        
    os.chdir('..')
   
   
   
# calculate percent correct for each block
scoreList = []
percentCorrect = []    
    
for block in allBlocks:
    #scores = allBlocks[block].flavour == allBlocks[block].animal_answer
    #scores =  block.flavour == block.animal_answer
    sensScore = block.flavour == block.animal_answer
    addReward = block.additional_reward > 1
    scores = sensScore | addReward
    ncorrect = sum(scores)
    scoreList.append(ncorrect)
    ntrials = len(block)
    percentCorrect.append(ncorrect/ntrials * 100)
    
# a list to track total scores per day (blocks per day averaged)   
scoreDay = [] 
 
for group in chunker(percentCorrect, 3):
    scoreDay.append(sum(group)/len(group))
    
plt.plot(scoreDay)



