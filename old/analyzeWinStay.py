# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 17:05:31 2016

@author: esther
"""
import pandas as pd
import numpy as np

# compare animals choices with win-stay strategy 

# load in automatically scored data
Adat = pd.read_csv("AutoData.csv",header=[0,1],index_col = [0,1,2,3], tupleize_cols=False )

# load in manually scored data (to identify trials manually cancelled/marked as nan)
Mdat = pd.read_csv("ManualScores.csv",index_col = ["Phase","Day","Block","Trial"])
Mdat.columns = [u'1', u'2', u'3', u'4']

# extract actual randomization
sides =  Adat.xs('side',level = 1, axis = 1) 

sidesIndx = sides.copy()
sidesIndx['choice/side'] = 'side'
sidesIndx.set_index('choice/side', append = True, inplace = True)
sidesIndx = sidesIndx.reorder_levels(['choice/side', 'Phase', 'Day','Block','Trial'])
sidesIndx = sidesIndx.unstack(level=0).reorder_levels([1,0], axis=1)



# extract animal choices
choiceRaw = Adat.xs('animal_answer',level = 1, axis = 1) 
# replace the timed out trials (animal answer = 2) 
choicesNo2 = choiceRaw.copy()
choicesNo2[choiceRaw == 2] = np.nan

# now also do not count the manually skipped trials (set as nan)
choices = choicesNo2.copy()
mask = pd.isnull(Mdat)
choices[mask] = np.nan



choicesIndx = choices.copy()
choicesIndx['choice/side'] = 'choice'
choicesIndx.set_index('choice/side', append = True, inplace = True)
choicesIndx = choicesIndx.reorder_levels(['choice/side', 'Phase', 'Day','Block','Trial'])
choicesIndx = choicesIndx.unstack(level=0).reorder_levels([1,0], axis=1)


sideChoices = sidesIndx.join(choicesIndx)

# loop per block (groups of [phase, day, block])
# for each row in that group (starting from the 2nd row) check if the 
# animal choice in the prev. trial was correct and if so, if he returned to the same side the next trial (win-stay = +1),
# or if he chose the opposite side (win-shift = +1), and whether or not this was the correct choice (rewarded)
# (if they were applying the strategy in correct cases, it's not necessarily a strategic response but an actual response to the tone (the desired response) )  

# try applying a function to each group instead of looping over it along the lines of 
#df.groupby(level =  ["Phase","Day","Block"]).agg(lamda x: if x+1 == x: y = 1)

# or make a function such as:
#def get_stats(group):
#    return {'min': group.min(), 'max': group.max(), 'count': group.count(), 'mean': group.mean()}





def simulate_winstay(df):  
   #correct = df['side'] == df['choice']
   winStay = pd.DataFrame()
   
   # append row of nans as first row to winStay
#
   for i, row in df.iterrows():
        
        currentChoice = row['choice']
        incorrect = currentChoice[currentChoice != row['side']]
        
        # predict what the rat would do in the next trial if using win-stay strategy
        # by default choose the same side next
        winStayNxt = row['choice']
        # except if the current trial was incorrect, then switch sides
        winStayNxt[incorrect.index] = [1-t for t in incorrect]
        winStay = winStay.append(winStayNxt)
        
        
        # predict what the rat would do in the next trial if using win-shift strategy
        #winShiftNxt = 
        
        
#        print correct
#
#   print test
   # winStay = winStay[-1] ??
   
   return winStay


WinStay = sideChoices.groupby(level =  ["Phase","Day","Block"]).apply(simulate_winstay)

# the first row needs to be nan's (no prev choices to base next choice on, and all the rows
# should be shifted down one (the prediction was for the next choice, based on the current trial)
# in this process the last row should be/is deleted
WinStay = WinStay.shift(1)

# to get the win shift strategy reverse the win-stay answers
WinShift = 1 - WinStay


# identify trials with hints
rewards = Adat.xs('reward_size',level = 1, axis = 1) 
add_reward = Adat.xs('additional_reward',level = 1, axis = 1) 


hints = (rewards < 1) & (add_reward  > 0)







scoreWinStayHintsInc = WinStay == choices

# compare win-stay with actual answers of rat
scoreWinStayBool = WinStay[~hints] == choices[~hints]
scoreWinStay = scoreWinStayBool * 1



#get avg
#ScoresWinStayAvg = scoreWinStay.sum() / len(WinStay) * 100


WinStaySummed = scoreWinStay.sum(axis = 0,level = ["Phase","Day"])
countGroups = scoreWinStay.groupby(level = ["Phase","Day"])

ScoresPerDayWinStay = WinStaySummed/countGroups.count(axis=0) * 100

ax = ScoresPerDayWinStay.plot(title ="Win Stay Strategy Scores")
ax.set(ylabel="% trials strategy was applied")



# Scores Win-Shift
scoreWinShift = WinShift[~hints] == choices[~hints]
scoreWinShift = scoreWinShift * 1

#ScoresWinShiftAvg = scoreWinShift.sum() / len(WinShift) * 100

WinShiftSummed = scoreWinShift.sum(axis = 0,level = ["Phase","Day"])
countGroups = scoreWinShift.groupby(level = ["Phase","Day"])

ScoresPerDayWinShift = WinShiftSummed/countGroups.count(axis=0) * 100

ax = ScoresPerDayWinShift.plot(title ="Win Shift Strategy Scores")
ax.set(ylabel="% trials strategy was applied")
















#
#def check_answers(sidegroup,choicegroup):
#    for i, row in choicegroup.iterrows():
#        currentChoice = choicegroup.ix[i]
#        correct = currentChoice[currentChoice == sidegroup.ix[i]]

# then apply it to the groups

#df['postTestScore'].groupby(df['categories']).apply(get_stats).unstack()




#
#
#animals = ["1","2","3","4"]
#
#sidegroups = sides.groupby(level =  ["Phase","Day","Block"])
#choicegroups = choices.groupby(level =  ["Phase","Day","Block"])
#
#
#for side,choice in zip(sidegroups,choicegroups):
#    print side
#    print choice
# 

