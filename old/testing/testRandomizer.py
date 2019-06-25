#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 15:48:46 2017

@author: esther
"""

from random import randint
import numpy as np

choices = [0, 1]
nTrials = 20

in_row = 1
p_x= randint(0, len(choices)-1)
choices_list = [p_x]
counter = 0

#%%
while len(choices_list) < nTrials:
    
    x = randint(0, len(choices)-1)
    if p_x == x:
        if in_row <3:
            in_row +=1
            choices_list.append(x)
            p_x = x
            counter = counter + 1
        else:
            continue
    else:
        choices_list.append(x)
        p_x = x
        in_row = 1
        counter = counter + 1
 
 
    if counter > nTrials - 1:
        d = np.diff(choices_list)
        flavChange = np.nonzero(d)
        nflavChange = len(flavChange[0])
        
        if nflavChange > 9:
            in_row = 1
            p_x= randint(0, len(choices)-1)
            choices_list = [p_x]