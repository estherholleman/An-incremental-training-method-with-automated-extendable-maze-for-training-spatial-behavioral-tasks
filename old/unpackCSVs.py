# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 14:51:28 2015

@author: esther
"""

def unpackCSVs():
        
    #import necessary libraries/packages
    import os
    import glob
    import pandas as pd

    ## read in all data
    frame = pd.DataFrame()
    allBlocks = []
    
    #cd to trial data folder
    os.chdir('Results/')    
    
    # list all folders (&files) in directory
    phases = os.listdir(os.curdir)    
    # sort phases
    phases.sort()    
    
    for phase in phases:
        
        #cd to trial data folder
        os.chdir(phase)
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
            
            for block in blocks:
                #open folder of training day
                os.chdir(block)
                scores = glob.glob("*.csv")
                for score in scores:
                    
                    df = pd.read_csv(score,index_col=None, header=0)
                    df['Animal'] = score[7]
                    df['Phase'] = phase[2:]
                    df['Day'] = day[4:]
                    df['Block'] = block[6]
                    
                    allBlocks.append(df)
                
                frame = pd.concat(allBlocks)
                
                os.chdir('..') # exit block folder
                     
            os.chdir('..') # exit day folder
            
        os.chdir('..') # exit trial data folder
        os.chdir('..') # exit phase folder
           
    return frame
    
    
    
