#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 16:24:03 2017

@author: esther
"""


from random import randint
import numpy as np




def generate_flavors(choices = [0, 1], nTrials = 20):
    in_row = 1
    p_x= randint(0, len(choices)-1)
    choices_list = [p_x]
    #counter = 0
    
    #%%
    while len(choices_list) < nTrials:
        
        x = randint(0, len(choices)-1)
        if p_x == x:
            if in_row <3:
                in_row +=1
                choices_list.append(x)
                p_x = x
                #counter = counter + 1
            else:
                continue
        else:
            choices_list.append(x)
            p_x = x
            in_row = 1
            #counter = counter + 1
     
     
        if len(choices_list) > nTrials - 1:
            d = np.diff(choices_list)
            flavChange = np.nonzero(d)
            nflavChange = len(flavChange[0])
            
            if nflavChange > nTrials/2 - randint(1,3):
                in_row = 1
                p_x= randint(0, len(choices)-1)
                choices_list = [p_x]


    return choices_list 

    
    
    
def testRand(nTests, nTrials):
        #set up lists to fill for every randomization generated
        #frequency of alternation between sides occurring per block
        alternations_list = []
        # frequency of right occurring per block
        right_list = [];
        # frequency of left occurring per block 
        left_list = [];
        # number of times flavor did not change per block
        nochange_list = [];
        #number of times flavor changed from left to right in a block
        leftToright_list = [];
        #number of times flavor changed from right to left in a block
        rightToleft_list = [];       
        
        
        while len(alternations_list) < nTests:
            # generate the randomization for one block
            sides = generate_flavors(nTrials = nTrials)
            
            #count total number of occurrences of each flavor per block
            right = sum(sides)
            left = len(sides) - right
            left_list.append(left)
            right_list.append(right)
            
            
            # differences in sides between trials
            d = np.diff(sides)
            # trials between which the flavor changed
            flavSwaps = np.nonzero(d)
            # number of flavor changes between trials
            alternations = len(flavSwaps[0])
            # add number of flavor changes for this block to list
            alternations_list.append(alternations)
            
            # to analyse flavor changes:
            # 0 = flavor did not change
            nochange = sum(d == 0)
            nochange_list.append(nochange)
            # 1 = flavor change from left to right
            leftToright = sum(d == 1)
            leftToright_list.append(leftToright)
            #-1 = flavor change from right to left
            rightToleft = sum(d == -1)
            rightToleft_list.append(rightToleft)
            
        # return results in a dictionary  
        return {'left':left_list, 'right':right_list,'alternations':alternations_list, 'nochange':nochange_list, 'leftToright':leftToright_list, 'rightToleft':rightToleft_list}
            
    