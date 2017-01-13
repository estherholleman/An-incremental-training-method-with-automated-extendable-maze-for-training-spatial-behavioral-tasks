# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 15:13:47 2016

@author: esther
"""
import pandas as pd
import numpy as np

# read in manual scores
ManualScores = pd.read_csv("ManualScoresNewIndx.csv")

# list which columns will be indexes
indexes = ["Phase","Day","Block","Trial"]
ManualScores = ManualScores.set_index(indexes,drop = True)


# load sensor recorded reaction times
ReactionTimes = pd.read_csv("ReactionTimes.csv")

# list which columns will be indexes
indexes = ["Phase","Day","Block","trial_nr"]
ReactionTimes = ReactionTimes.set_index(indexes,drop = True)

# get the indexes 
IndxReactionTimes = ReactionTimes.index
IndxManualScores = ManualScores.index


# Find the indexes in ManualScores that are missing in ReactionTimes
MissingIndexes = IndxManualScores.difference(IndxReactionTimes)


# Make a new data frame in order to examine indexes by eye
LookAtIndexes = pd.DataFrame(np.zeros(len(MissingIndexes)))
LookAtIndexes = LookAtIndexes.set_index(MissingIndexes)


# just dropping the last 15 missing indexes to test if it works
test = MissingIndexes[-15:]
ManualScores = ManualScores.drop(test)

# checked all the missing indexes (they were all nans in the other matrix) and removed them all at once:
ManualScores = ManualScores.drop(MissingIndexes)



# Reverse the processes to find those indexes that are in ReactionTimes but not in Manual Scores
MissingIndexesRev = IndxReactionTimes.difference(IndxManualScores)
# Make a new data frame in order to examine indexes by eye
LookAtIndexesRev = pd.DataFrame(np.zeros(len(MissingIndexesRev)))
LookAtIndexesRev = LookAtIndexesRev.set_index(MissingIndexesRev)

IndexesToDrop = ReactionTimes.ix[(1,1,1,1):(1,1,3,10)]
IndexesToDrop = IndexesToDrop.index
ReactionTimesRemovePhase1Day1 = ReactionTimes.drop(IndexesToDrop)


IndexesToDrop = ReactionTimes.ix[(1,8,2,1):(1,8,2,5)]
IndexesToDrop = IndexesToDrop.index
ReactionTimesRemovePhase1Day1 = ReactionTimesRemovePhase1Day1.drop(IndexesToDrop)

IndexesToDrop = ReactionTimes.ix[(1,8,3,1):(1,8,3,5)]
IndexesToDrop = IndexesToDrop.index
ReactionTimesRemovePhase1Day1 = ReactionTimesRemovePhase1Day1.drop(IndexesToDrop)


