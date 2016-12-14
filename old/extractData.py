# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 12:33:20 2016

@author: esther
"""
# provide a string as argument specifying what to extract,  option are:
# - "reaction_time"
# - "side" (for the randomization)
# - 
import pandas as pd

def extractData(df, toExtract = "reaction_time"):

    Rat1RT = df[toExtract].iloc[df.index.get_level_values('Animal') == 1]
    Rat2RT = df[toExtract].iloc[df.index.get_level_values('Animal') == 2]
    Rat3RT = df[toExtract].iloc[df.index.get_level_values('Animal') == 3]
    Rat4RT = df[toExtract].iloc[df.index.get_level_values('Animal') == 4]
    
    rt1 = pd.DataFrame(Rat1RT)
    rt1.index = rt1.index.droplevel()
    
    rt2 = pd.DataFrame(Rat2RT)
    rt2.index = rt2.index.droplevel()
    
    rt3 = pd.DataFrame(Rat3RT)
    rt3.index = rt3.index.droplevel()
    
    rt4 = pd.DataFrame(Rat4RT)
    rt4.index = rt4.index.droplevel()
    
    data = pd.concat([rt1,rt2,rt3,rt4], join = "outer", axis = 1)
    data.columns = ["Rat1","Rat2","Rat3","Rat4"]
    return data
    
    