# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 16:56:23 2016

@author: esther
"""
import pandas as pd
from random import randint
import numpy as np
from scipy.stats import gaussian_kde
import matplotlib.pyplot as plt
import matplotlib.patches as patch
#matplotlib.style.use('ggplot') 
from scipy.stats import gaussian_kde



def generate_flavors(choices = [0, 1], nTrials = 20):
    in_row = 1
    p_x= randint(0, len(choices)-1)
    choices_list = [p_x]
    counter = 0
    
    while len(choices_list) < nTrials:
        counter = counter + 1
        x = randint(0, len(choices)-1)
        if p_x == x:
            if in_row <3:
                in_row +=1
                choices_list.append(x)
                p_x = x
            else:
                continue
        else:
            choices_list.append(x)
            p_x = x
            in_row = 1
     
     
        if counter > 19:
            d = np.diff(choices_list[counter-19 : counter])
            flavChange = np.nonzero(d)
            nflavChange = len(flavChange[0])
            
            if nflavChange > 10:
                in_row = 1
                p_x= randint(0, len(choices)-1)
                choices_list[counter-19 : counter] = [p_x]
                     
        #check for number of alternations in a row
#        if len(choices_list) > 19:
#            d = np.diff(choices_list)
#            flavChange = np.nonzero(d)
#            nflavChange = len(flavChange[0])
#            
#            if nflavChange > 10:
#                in_row = 1
#                p_x= randint(0, len(choices)-1)
#                choices_list = [p_x]
##                    

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


#%% Loop over all csv files of computer scored trials and import
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
    

#%% calculate the factors for a particular input number  
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))    

def loadData():
    
    # load in automatically scored data
    Adat = pd.read_csv("AutoData.csv",header=[0,1],index_col = [0,1,2,3], tupleize_cols=False )
    
    # load in manually scored data (to identify trials manually cancelled/marked as nan)
    Mdat = pd.read_csv("ManualScores.csv",index_col = ["Phase","Day","Block","Trial"])
    Mdat.columns = [u'1', u'2', u'3', u'4']
    
    return Adat, Mdat


def removeCancelledTrials(df, Mdat): 
    # convert manually cancelled trials (nans in Mdat) to nans in choices
    # df input should be choices
    mask = pd.isnull(Mdat)
    df[mask] = np.nan
    
    return df



def preProcessChoices(Adat, Mdat):
    
    # extract choices and sides
    sides =  Adat.xs('side',level = 1, axis = 1) 
    choiceRaw = Adat.xs('animal_answer',level = 1, axis = 1)  

    # replace the timed out trials (animal answer = 2) 
    choices = choiceRaw.copy()
    choices[choiceRaw == 2] = np.nan   
    
    choices = removeCancelledTrials(choices,Mdat)

    return choices, sides
    
    

def scoreChoices(Adat, choices, sides):
    
    rewards = Adat.xs('reward_size',level = 1, axis = 1) 
    add_reward = Adat.xs('additional_reward',level = 1, axis = 1)    

    # find hints
    hints = (rewards < 1) & (add_reward  == 1)
    
    validTrials = ~np.isnan(choices[~hints])

    #%% calculate correct and incorrect
    correct = choices[~hints] == sides[~hints]
    incorrect = choices[~hints] != sides[~hints] 
    
    countGroups = choices[~hints].groupby(level = ["Phase","Day"])
    nTotalTrials = countGroups.count(axis=0)
    
    return validTrials, correct, incorrect, nTotalTrials
    

def scoreChoicesManualReward(Adat, choices):
    
    rewards = Adat.xs('reward_size',level = 1, axis = 1) 
    add_reward = Adat.xs('additional_reward',level = 1, axis = 1)    


    #%% calculate correct and incorrect
    correct = (rewards + add_reward) > 1 
    correct = correct[~np.isnan(choices)]

    countGroups = correct.groupby(level = ["Phase","Day"])
    nTotalTrials = countGroups.count(axis=0)
    
    return correct, nTotalTrials


def calcScoresPerDay(correct, nTotalTrials):
    
    correctSummed = correct.sum(axis = 0,level = ["Phase","Day"] )
    
    ScoresPerDay = correctSummed/nTotalTrials * 100
    
    ScoresPerDay[nTotalTrials < 7] = np.nan
    
    ScoresPerDay = ScoresPerDay.interpolate()
    
    return ScoresPerDay

    
def calcScoresPerPhase(correct, nTotalTrials):
    
    correctSummed = correct.sum(axis = 0,level = ["Phase"] )
    
    ScoresPerPhase = correctSummed/nTotalTrials.sum(level = ["Phase"]) * 100
    
    return ScoresPerPhase

        


def plotScores(ScoresPerDay):
    
    PhaseLengths = [];
    phases = range(1,7)
    phase = 1
    
    for phase in phases:  
        PhaseLengths.append(len(ScoresPerDay.iloc[ScoresPerDay.index.get_level_values('Phase') == phase]))
    
    DaysInPhase = np.cumsum(PhaseLengths)
    
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)
    for p in [
        patch.Rectangle(
            (0.1, 0.1), PhaseLengths[0], 99.9,
            alpha=0.7,
            facecolor = "#003b46"
        ),
      
        patch.Rectangle(
            (DaysInPhase[0], 0.1), PhaseLengths[1], 99.9,
            alpha=0.4,
            facecolor = "#07575b"
        ),
    
        patch.Rectangle(
            (DaysInPhase[1], 0.1), PhaseLengths[2], 99.9,
            alpha=0.5,
            facecolor = "#003b46"
       ),
        patch.Rectangle(
            (DaysInPhase[2], 0.1), PhaseLengths[3], 99.9,
            alpha=0.3,
            facecolor = "#07575b"
        ),
        patch.Rectangle(
            (DaysInPhase[3], 0.1), PhaseLengths[4], 99.9,
            alpha=0.4,
            facecolor = "#07575b"
        ),
        patch.Rectangle(
            (DaysInPhase[4], 0.1), PhaseLengths[5], 99.9,
            alpha=0.6,
            facecolor = "#07575b"
        ),
        patch.Rectangle(
            (DaysInPhase[5], 0.1), PhaseLengths[6], 99.9,
            alpha=0.8,
            facecolor = "#07575b"
        )
    ]:
        ax1.add_patch(p)
#          
    
    ScoresPerDay['Average'] = ScoresPerDay.mean(axis = 1)
    
    ax2 = ScoresPerDay.plot(ax = ax1,colormap = 'PuRd', title = "LEARNING CURVES - SCORING MANUAL REWARDS",figsize = (11.69,8.27))

    patches,labels = ax2.get_legend_handles_labels()
    ax2.set_xlabel("(Phase,Trial)")
    ax2.set_ylabel("% Correct")
    ax2.lines[-1].set_linewidth(5)
    ax2.lines[-1].set_color('black')   
    
    ax2.legend(patches,labels,loc=4, framealpha = 0.4, title = "Rats: ")
    
    plt.savefig("ScoresPerDayManualRewards.eps",format = "eps")
    plt.savefig("ScoresPerDayManualRewards.png",format = "png")








# Estimate probability density function through kernel density (gaussian_kde)
def computeDensity(data, covar_factor = .25):
    density = gaussian_kde(data)
    # determine bandwidth (of smoothing)
    density.covariance_factor = lambda : covar_factor
    density._compute_covariance()
    return density


def computeDensityPerPhase(rt, correct, incorrect, figname = "ReactionTimeDensities", mode = True):
    
    cor = ["Correct","Incorrect"]
    animals = ["1","2","3","4"]
    modesCorrect = pd.DataFrame(np.nan, columns = animals, index = range(1,8))
    modesIncorrect = pd.DataFrame(np.nan, columns = animals, index = range(1,8))

    # divide data into groups per phase
    phaseGrouped =rt.groupby(level = "Phase")
    
    f, axarr = plt.subplots(len(phaseGrouped),2, figsize = (15,22))
    
    for corr in cor:    
    
        if corr == 'Correct':
            sensScoreGrouped = correct.groupby(level = "Phase")
            c = 0
        else:
            sensScoreGrouped = incorrect.groupby(level = "Phase")
            c = 1
    
        for p,phase in phaseGrouped:
           
           # select phase
           rtPhase = phaseGrouped.get_group(p)
           sensScorePhase = sensScoreGrouped.get_group(p)
           
     
            # make x-axis
           xs = np.linspace(0,8000,100)
    #        # compute density
           
           
           for animal in animals:
               
               sel = ~np.isnan(rtPhase[animal]) & sensScorePhase[animal]
               rtAnimal = rtPhase[animal][sel]
               nTrials = len(rtAnimal)
               
               if nTrials < 5: continue
                   
               density = computeDensity(rtAnimal)
                  
               title = corr + " Trials Phase " + str(p)
               
               ## plot density
               axarr[p-1,c].plot(xs,density(xs), label = "Rat " + animal + ", n = " + str(nTrials))
               axarr[p-1,c].set_title(title)
               axarr[p-1,c].set_xlabel("Reaction Time (ms)")
               axarr[p-1,c].set_ylabel("Density") 
               axarr[p-1,c].legend()
               
               if mode:
                   pdf = density.pdf(xs);    
                   mostcommon = xs[pdf == max(pdf)]
                   axarr[p-1,c].plot((mostcommon, mostcommon), (0, max(pdf)), 'k--')
                   if corr == 'Correct':
                       modesCorrect.iloc[p-1,int(animal)-1] = mostcommon
                   else:
                       modesIncorrect.iloc[p-1,int(animal)-1] = mostcommon
                                        
          
               plt.subplots_adjust(hspace = 0.7)
               plt.suptitle(figname, fontsize = 18)

    if mode:    
        figname = figname + '_Mode'
       
#    plt.savefig(figname + ".eps",format = "eps")
#    plt.savefig(figname + ".png",format = "png")

    return modesCorrect, modesIncorrect

# Estimate probability density function through kernel density (gaussian_kde)
def computeDensity(data, covar_factor = .25):
    density = gaussian_kde(data)
    # determine bandwidth (of smoothing)
    density.covariance_factor = lambda : covar_factor
    density._compute_covariance()
    return density


def computeDensityPerPhaseCorrIncorr(rt, CorrIncorr, figname = "ReactionTimeDensities", mode = True):
    
    cor = ["Correct","Incorrect"]
    animals = ["1","2","3","4"]
    modesCorrect = pd.DataFrame(np.nan, columns = animals, index = range(1,8))
    modesIncorrect = pd.DataFrame(np.nan, columns = animals, index = range(1,8))

    # divide data into groups per phase
    phaseGrouped =rt.groupby(level = "Phase")
    
    f, axarr = plt.subplots(len(phaseGrouped),2, figsize = (15,22))
    
    CorrValid = CorrIncorr['correct'] & CorrIncorr['valid']
    IncorrValid = CorrIncorr['incorrect'] & CorrIncorr['valid']
    
    
    for corr in cor:    
    
        if corr == 'Correct':
            sensScoreGrouped = CorrValid.groupby(level = "Phase")
            c = 0
        else:
            sensScoreGrouped = IncorrValid.groupby(level = "Phase")
            c = 1
    
        for p,phase in phaseGrouped:
           
           # select phase
           rtPhase = phaseGrouped.get_group(p)
           sensScorePhase = sensScoreGrouped.get_group(p)
           
     
            # make x-axis
           xs = np.linspace(0,8000,100)
    #        # compute density
           
           
           for animal in animals:
               
               sel = ~np.isnan(rtPhase[animal]) & sensScorePhase[animal]
               rtAnimal = rtPhase[animal][sel]
               nTrials = len(rtAnimal)
               
               if nTrials < 5: continue
                   
               density = computeDensity(rtAnimal)
                  
               title = corr + " Trials Phase " + str(p)
               
               ## plot density
               axarr[p-1,c].plot(xs,density(xs), label = "Rat " + animal + ", n = " + str(nTrials))
               axarr[p-1,c].set_title(title)
               axarr[p-1,c].set_xlabel("Reaction Time (ms)")
               axarr[p-1,c].set_ylabel("Density") 
               axarr[p-1,c].legend()
               
               if mode:
                   pdf = density.pdf(xs);    
                   mostcommon = xs[pdf == max(pdf)]
                   axarr[p-1,c].plot((mostcommon, mostcommon), (0, max(pdf)), 'k--')
                   if corr == 'Correct':
                       modesCorrect.iloc[p-1,int(animal)-1] = mostcommon
                   else:
                       modesIncorrect.iloc[p-1,int(animal)-1] = mostcommon
                                        
          
               plt.subplots_adjust(hspace = 0.7)
               plt.suptitle(figname, fontsize = 18)

    if mode:    
        figname = figname + '_Mode'
       
#    plt.savefig(figname + ".eps",format = "eps")
#    plt.savefig(figname + ".png",format = "png")

    return modesCorrect, modesIncorrect    
    
    
    
    
    
def computeDensityPerBlock(Adat, correct, incorrect, animal = "1", mode = True):
    
    cor = ["Correct","Incorrect"]
    rt = Adat.xs('reaction_time',level = 1, axis = 1) 
    #hints = (Adat[animal].reward_size < 1) & (Adat[animal].additional_reward > 0)
    phases = rt.index.get_level_values(0).unique()
        
    # divide data into groups per phase
    blockGrouped =rt.groupby(level = ["Phase","Block"])
    
    f, axarr = plt.subplots(len(phases),2, figsize = (15,22))

    
    for corr in cor:
        if corr == 'Correct':
            sensScoreGrouped = correct.groupby(level = ["Phase","Block"])
            c = 0
        else:
            sensScoreGrouped = incorrect.groupby(level = ["Phase","Block"])
            c = 1
        
        
        for b,block in blockGrouped:
            
            # select reaction times for block
           rtBlock = blockGrouped.get_group(b)
           sensScoreBlock = sensScoreGrouped.get_group(b)
         
           rtAnimal = rtBlock[animal][(rtBlock[animal] > 4) & sensScoreBlock[animal]] 
           nTrials = len(rtAnimal)                       
           
           if nTrials < 2: continue
               
           # compute density
           density = computeDensity(rtAnimal)
           
           phase = rtBlock.index.get_level_values(0).unique()[0]
           
           ## prepare plot
           # make x-axis
           xs = np.linspace(0,8000,100)
           title = corr + " Trials, Phase" + str(phase) + ": Reaction Time Distribution for Rat " +  animal           
           #figname = "ReactionTimeDensities_" + corr + "Trials_Rat" + animal
           ## plot density
           axarr[phase-1,c].plot(xs,density(xs), label = "block " + str(b[1]) + ", n= " + str(nTrials))
           axarr[phase-1,c].set_title(title)
           axarr[phase-1,c].set_xlabel("Reaction Time (ms)")
           axarr[phase-1,c].set_ylabel("Density")  
           axarr[phase-1,c].legend()

           if mode:
               pdf = density.pdf(xs);    
               mostcommon = xs[pdf == max(pdf)]
               axarr[phase-1,c].plot((mostcommon, mostcommon), (0, max(pdf)), 'k--')           

           plt.subplots_adjust(hspace = 0.7)
#   
    figname = "ReactionTimeDensitiesBlocks_Rat" + animal     
           
    if mode:    
        figname = figname + '_Mode'           
           
    plt.savefig(figname + ".eps",format = "eps")
    plt.savefig(figname + ".png",format = "png")



def makeExtraColumnIndex(dataframe, name = 'NameMe'):
    
    df = dataframe.copy()
    df['tempIndx'] = name
    df.set_index('tempIndx', append = True, inplace = True)
    df = df.reorder_levels(['tempIndx', 'Phase', 'Day','Block','Trial'])
    df = df.unstack(level=0).reorder_levels([1,0], axis=1)
    
    return df

def makeSideChoices(sides,choices):
    
    sidesIndx   = makeExtraColumnIndex(sides, name = 'side')
    choicesIndx = makeExtraColumnIndex(choices, name = 'choice')
    
    sideChoices = sidesIndx.join(choicesIndx)
   
    return sideChoices

    
    
def simulate_winstay(df):  
   
   winStay = pd.DataFrame()
   
   for i, row in df.iterrows():
        
        currentChoice = row['choice']
        incorrect = currentChoice[currentChoice != row['side']]
        
        # predict what the rat would do in the next trial if using win-stay strategy
        # by default choose the same side next
        winStayNxt = currentChoice
        # except if the current trial was incorrect, then switch sides
        winStayNxt[incorrect.index] = [1-t for t in incorrect]
        winStay = winStay.append(winStayNxt)
  
   return winStay

    
   
def analyseWinStay(sideChoices):   
  
    WinStay = sideChoices.groupby(level =  ["Phase","Day","Block"]).apply(simulate_winstay)

    # the first row needs to be nan's (no prev choices to base next choice on, and all the rows
    # should be shifted down one (the prediction was for the next choice, based on the current trial)
    # in this process the last row should be/is deleted
    WinStay = WinStay.shift(1)
    
    # to get the win shift strategy reverse the win-stay answers
    WinShift = 1 - WinStay
    
    return WinStay, WinShift
    
