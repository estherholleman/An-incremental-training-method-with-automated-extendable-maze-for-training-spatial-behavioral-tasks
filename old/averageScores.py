# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 11:59:20 2016

@author: esther
"""

averagedEveryThirdDay = averageScoresAllScores.groupby(averageScoresAllScores.index/3).mean();
averagedEveryFifthDay = averageScoresAllScores.groupby(averageScoresAllScores.index/5).mean();