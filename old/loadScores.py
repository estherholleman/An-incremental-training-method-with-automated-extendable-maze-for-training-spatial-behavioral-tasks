# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 14:05:23 2016

@author: esther
"""
import pandas as pd


#load scores
scoresToneTask1 = pd.read_csv('scoresToneTask1.csv')

scoresToneTask = pd.read_csv('scoresToneTask2.csv')

scoresMAZE1 = pd.read_csv('scoresMAZE.csv')
scoresMAZE2 = pd.read_csv('scoresMAZE2.csv')
scoresMAZE3 = pd.read_csv('scoresMAZE3.csv')



AllScores = pd.concat([scoresToneTask,scoresMAZE1,scoresMAZE2,scoresMAZE3],axis = 0)


AllScores.plot(colormap = 'winter')
plt.title('Learning Curve Group 2', fontsize=14);
plt.ylim(0,100);
plt.xlabel('training days');
plt.ylabel('% correct');
plt.xticks(np.arange(1,len(scores)+1,1.0))
plt.yticks(np.arange(0,101,5))



AllScores.to_csv('AllScoresToneTaskBackUp.csv', index = False);


averageScoresAllScores = AllScores.mean(1)


# testing adding columns to dataframe and moving it to the front
AllScores["Phase"] = ""
cols = AllScores.columns.tolist()
cols = cols[-1:] + cols[:-1]
AllScoresWithPhase = AllScores[cols]

AllScoresWithPhase["Trial"] = ""
cols = AllScoresWithPhase.columns.tolist()
cols = cols[-1:] + cols[:-1]
AllScoresWithPhase = AllScoresWithPhase[cols]


# extract index from AllScores
indxScores = AllScores.index.tolist()


phase1 = [1] *41
phase2 = [2] * 6
phase3 = [3] * 9
phase4 = [4] * 6

phases = phase1 + phase2 + phase3 + phase4

indx1 = range(1,42)
indx2 = range(1,7)
indx3 = range(1,10)
indx4 = range(1,7)

indxes = indx1 + indx2 + indx3 + indx4


arrays = [phases,indxes]

tuples = list(zip(*arrays))

index = pd.MultiIndex.from_tuples(tuples, names=['Phase', 'Trial'])

AllScoresWithIndx = AllScores.set_index(index)


averagedEveryThirdDay = averageScoresAllScores.groupby(averageScoresAllScores.index/3).mean();
averagedEveryFifthDay = averageScoresAllScores.groupby(averageScoresAllScores.index/5).mean();
