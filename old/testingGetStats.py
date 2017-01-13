# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 12:34:20 2016

@author: esther
"""

import numpy as np
from myFunctions import computeDensity


def getStats(df):
           
     
    # make x-axis
    xs = np.linspace(0,8000,100)
               
    density = computeDensity(df)

    pdf = density.pdf(xs);    
    
    return {'mode': xs[pdf == max(pdf)], 'median':  np.median(pdf), 'mean': np.mean(pdf)}
    



def getStatsRT(group):
     
    return pd.DataFrame({'median':  np.median(group), 'mean': np.mean(group)})