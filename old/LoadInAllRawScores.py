# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 13:44:05 2016

@author: esther
"""


import pandas as pd

## RAT1
ToneTask1Rat1 = pd.read_csv("ToneTask1Rat1.csv")
ToneTask2Rat1 = pd.read_csv("ToneTask2Rat1.csv")
ToneTaskMazeRat1 = pd.read_csv("ToneTaskMazeRat1New.csv")
ToneTaskMaze2Rat1 = pd.read_csv("ToneTaskMaze2Rat1.csv")
ToneTaskMaze3Rat1 = pd.read_csv("ResultsRat1ToneTaskMAZE3_6days.csv")

TT1Rat1 = ToneTask1Rat1.T
TT1Rat1all = TT1Rat1.unstack(level=-1)

TT2Rat1 = ToneTask2Rat1.T
TT2Rat1all = TT2Rat1.unstack(level=-1)

TT3Rat1 = ToneTaskMazeRat1.T
TT3Rat1all = TT3Rat1.unstack(level=-1)

TT4Rat1 = ToneTaskMaze2Rat1.T
TT4Rat1all = TT4Rat1.unstack(level=-1)

TT5Rat1 = ToneTaskMaze3Rat1.T
TT5Rat1all = TT5Rat1.unstack(level=-1)

Rat1 = [TT1Rat1all, TT2Rat1all,TT3Rat1all,TT4Rat1all,TT5Rat1all]
Rat1 = pd.concat(Rat1)

## RAT2
ToneTask1Rat2 = pd.read_csv("ToneTask1Rat2.csv")
ToneTask2Rat2 = pd.read_csv("ResultsRat2ToneTask2.csv")
ToneTaskMazeRat2 = pd.read_csv("ToneTaskMazeRat2New.csv")
ToneTaskMaze2Rat2 = pd.read_csv("ToneTaskMaze2Rat2.csv")
ToneTaskMaze3Rat2 = pd.read_csv("ResultsRat2ToneTaskMAZE3_6days.csv")

TT1Rat2 = ToneTask1Rat2.T
TT1Rat2all = TT1Rat2.unstack(level=-1)

TT2Rat2 = ToneTask2Rat2.T
TT2Rat2all = TT2Rat2.unstack(level=-1)

TT3Rat2 = ToneTaskMazeRat2.T
TT3Rat2all = TT3Rat2.unstack(level=-1)

TT4Rat2 = ToneTaskMaze2Rat2.T
TT4Rat2all = TT4Rat2.unstack(level=-1)

TT5Rat2 = ToneTaskMaze3Rat2.T
TT5Rat2all = TT5Rat2.unstack(level=-1)

Rat2 = [TT1Rat2all,TT2Rat2all,TT3Rat2all,TT4Rat2all,TT5Rat2all]
Rat2 = pd.concat(Rat2)

##RAT3
ToneTask1Rat3 = pd.read_csv("ToneTask1Rat3.csv")
ToneTask2Rat3 = pd.read_csv("ResultsRat3ToneTask2.csv")
ToneTaskMazeRat3 = pd.read_csv("ToneTaskMazeRat3New.csv")
ToneTaskMaze2Rat3 = pd.read_csv("ResultsRat3ToneTaskMAZE2_9days.csv")
ToneTaskMaze3Rat3 = pd.read_csv("ResultsRat3ToneTaskMAZE3_6days.csv")

TT1Rat3 = ToneTask1Rat3.T
TT1Rat3all = TT1Rat3.unstack(level=-1)

TT2Rat3 = ToneTask2Rat3.T
TT2Rat3all = TT2Rat3.unstack(level=-1)

TT3Rat3 = ToneTaskMazeRat3.T
TT3Rat3all = TT3Rat3.unstack(level=-1)

TT4Rat3 = ToneTaskMaze2Rat3.T
TT4Rat3all = TT4Rat3.unstack(level=-1)

TT5Rat3 = ToneTaskMaze3Rat3.T
TT5Rat3all = TT5Rat3.unstack(level=-1)

Rat3 = [TT1Rat3all,TT2Rat3all,TT3Rat3all,TT4Rat3all,TT5Rat3all]
Rat3 = pd.concat(Rat3)

#RAT4
ToneTask1Rat4 = pd.read_csv("ToneTask1Rat4.csv")
ToneTask2Rat4 = pd.read_csv("ResultsRat4ToneTask2.csv")
ToneTaskMazeRat4 = pd.read_csv("ResultsRat4ToneTaskMAZE.csv")
ToneTaskMaze2Rat4 = pd.read_csv("ResultsRat4ToneTaskMAZE2_9days.csv")
ToneTaskMaze3Rat4 = pd.read_csv("ResultsRat4ToneTaskMAZE3_6days.csv")

TT1Rat4 = ToneTask1Rat4.T
TT1Rat4all = TT1Rat4.unstack(level=-1)

TT2Rat4 = ToneTask2Rat4.T
TT2Rat4all = TT2Rat4.unstack(level=-1)

TT3Rat4 = ToneTaskMazeRat4.T
TT3Rat4all = TT3Rat4.unstack(level=-1)

TT4Rat4 = ToneTaskMaze2Rat4.T
TT4Rat4all = TT4Rat4.unstack(level=-1)

TT5Rat4 = ToneTaskMaze3Rat4.T
TT5Rat4all = TT5Rat4.unstack(level=-1)

Rat4 = [TT1Rat4all,TT2Rat4all,TT3Rat4all,TT4Rat4all,TT5Rat4all]
Rat4 = pd.concat(Rat4)


AllRaw = [Rat1,Rat2,Rat3,Rat4]
AllScoresAllTasks = pd.concat(AllRaw,axis =1)
AllScoresAllTasks.columns = ['Rat1','Rat2','Rat3','Rat4']

#AllScoresAllTasks.to_csv("AllScoresAllTasksChecked.csv", index = False)