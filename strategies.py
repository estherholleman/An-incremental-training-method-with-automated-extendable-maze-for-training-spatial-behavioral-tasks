# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 16:39:03 2016

@author: esther
"""

import pandas as pd
from myFunctions import generate_flavors



sides = pd.read_csv("Randomization.csv")

randIndx = ["Phase","Day","Block", "trial_nr"]
Rnd = sides.set_index(randIndx,drop = True)

nTrials = len(Rnd)

# always alternates
alt0 = [0,1] * (nTrials/2) + [0]
alt1 = [1,0] * (nTrials/2) + [1]

# always chooses the same side
pref0 = [0] * nTrials
pref1 = [1] * nTrials

# several different possible patterns
alt2x0 = [0,0,1] * (nTrials/3) + [0]
alt2x1 = [1,1,0] * (nTrials/3) + [1]

alt3x0 = [0,0,0,1] * (nTrials/4) + [0]
alt3x1 = [1,1,1,0] * (nTrials/4) + [1]

alt3x02x1 = [0,0,0,1,1] * (nTrials/5)
alt3x12x1 = [1,1,1,0,0] * (nTrials/5)

# using own randomization
ownRand = generate_flavors()

#%% calculate scores for each type of strategy
AltScores0 = Rnd == alt0
AltScores1 = Rnd == alt1

PrefScores0 = Rnd == pref0
PrefScores1 = Rnd == pref1

AltScores2x0 = Rnd == alt2x0
AltScores2x1 = Rnd == alt2x1

AltScores3x0 = Rnd == alt3x0
AltScores3x1 = Rnd == alt3x1

AltScores3x02x1 = Rnd == alt3x02x1
AltScores3x12x1 = Rnd == alt3x12x1

OwnRandScores = Rnd == ownRand

# compare randomizations for each rat against those for all other rats
Rat1RandScores = Rnd.fillna(0) == [Rnd["Rat1"].fillna(0)]
Rat2RandScores = Rnd.fillna(0) == [Rnd["Rat2"].fillna(0)]
Rat3RandScores = Rnd.fillna(0) == [Rnd["Rat3"].fillna(0)]
Rat4RandScores = Rnd.fillna(0) == [Rnd["Rat4"].fillna(0)]

#%% sum scores per day
AltScores0Summed = AltScores0.sum(axis = 0,level = ["Phase","Day"])
AltScores1Summed = AltScores1.sum(axis = 0,level = ["Phase","Day"])

PrefScores0Summed = PrefScores0.sum(axis = 0,level = ["Phase","Day"])
PrefScores1Summed = PrefScores1.sum(axis = 0,level = ["Phase","Day"])

AltScores2x0Summed = AltScores2x0.sum(axis = 0,level = ["Phase","Day"])
AltScores2x1Summed = AltScores2x1.sum(axis = 0,level = ["Phase","Day"])

AltScores3x0Summed = AltScores3x0.sum(axis = 0,level = ["Phase","Day"])
AltScores3x1Summed = AltScores3x1.sum(axis = 0,level = ["Phase","Day"])

AltScores3x02x1Summed = AltScores3x02x1.sum(axis = 0,level = ["Phase","Day"])
AltScores3x12x1Summed = AltScores3x12x1.sum(axis = 0,level = ["Phase","Day"])

OwnRandScoresSummed = OwnRandScores.sum(axis = 0,level = ["Phase","Day"])

Rat1RandScoresSummed = Rat1RandScores.sum(axis = 0,level = ["Phase","Day"])
Rat2RandScoresSummed = Rat2RandScores.sum(axis = 0,level = ["Phase","Day"])
Rat3RandScoresSummed = Rat3RandScores.sum(axis = 0,level = ["Phase","Day"])
Rat4RandScoresSummed = Rat4RandScores.sum(axis = 0,level = ["Phase","Day"])

# calculate total trials per day
totalTrials = AltScores0.groupby(level = ["Phase","Day"])


#%% calculate percent correct by dividing by totalTrials
AltScores1PerDay = AltScores0Summed/totalTrials.count(axis=0) * 100
AltScores2PerDay = AltScores1Summed/totalTrials.count(axis=0) * 100
PrefScores1PerDay = PrefScores0Summed/totalTrials.count(axis=0) * 100
PrefScores2PerDay = PrefScores1Summed/totalTrials.count(axis=0) * 100
AltScores2x0PerDay = AltScores2x0Summed/totalTrials.count(axis=0) * 100
AltScores2x1PerDay = AltScores2x1Summed/totalTrials.count(axis=0) * 100
AltScores3x0PerDay = AltScores3x0Summed/totalTrials.count(axis=0) * 100
AltScores3x1PerDay = AltScores3x1Summed/totalTrials.count(axis=0) * 100
AltScores3x02x1PerDay = AltScores3x02x1Summed/totalTrials.count(axis=0) * 100
AltScores3x12x0PerDay = AltScores3x12x1Summed/totalTrials.count(axis=0) * 100
OwnRandScoresPerDay = OwnRandScoresSummed/totalTrials.count(axis=0) * 100
Rat1RandScoresPerDay = Rat1RandScoresSummed/totalTrials.count(axis=0) * 100
Rat2RandScoresPerDay = Rat2RandScoresSummed/totalTrials.count(axis=0) * 100
Rat3RandScoresPerDay = Rat3RandScoresSummed/totalTrials.count(axis=0) * 100
Rat4RandScoresPerDay = Rat4RandScoresSummed/totalTrials.count(axis=0) * 100

#%% Plot scores from different strategies

## Alternation
# scores when alternating, starting left
AltScores1PerDay.plot(title='Alternating Starting Left')

# scores when alternating, starting right
AltScores2PerDay.plot(title='Alternating Starting Right')


## Preference for one side only
# scores when only choosing left
PrefScores1PerDay.plot(title='Only Left')

# scores when alternating, starting right
PrefScores2PerDay.plot(title='Only Right')


## Various Alternation Patterns
# scores when alternating, twice left, once right (repetitively)
AltScores2x0PerDay.plot(title='Pattern 2x Left, 1x Right')

# scores when alternating, twice right, once left
AltScores2x1PerDay.plot(title='Pattern 2x Right, 1x Left')

# scores when alternating, twice left, once right (repetitively)
AltScores3x0PerDay.plot(title='Pattern 3x Left, 1x Right')

# scores when alternating, twice right, once left
AltScores3x1PerDay.plot(title='Pattern 3x Right, 1x Left')

# scores when alternating, twice left, once right (repetitively)
AltScores3x02x1PerDay.plot(title='Pattern 3x Left, 1x Right')

# scores when alternating, twice right, once left
AltScores3x12x0PerDay.plot(title='Pattern 3x Right, 1x Left')


## Scores of one instance of own randomization against another generated by the same code
OwnRandScoresPerDay.plot(title='Randomization Against Itself')

## Randomization of 1 rat applied to the randomization of the others (including itself (= 100% correct))
# This is a double check as these randomizations were created together at the start of each day of training. 
Rat1RandScoresPerDay.plot(title='Randomization Of Rat 1 Against Rand. of Other Rats')
Rat2RandScoresPerDay.plot(title='Randomization Of Rat 2 Against Rand. of Other Rats')
Rat3RandScoresPerDay.plot(title='Randomization Of Rat 3 Against Rand. of Other Rats')
Rat4RandScoresPerDay.plot(title='Randomization Of Rat 4 Against Rand. of Other Rats')
