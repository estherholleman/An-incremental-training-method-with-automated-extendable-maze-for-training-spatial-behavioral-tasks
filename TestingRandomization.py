# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 12:05:58 2016

@author: esther
"""

import matplotlib.pyplot as plt
# testing the different results from randomization
from randFunctions import testRand

#%% for 10 trials
RandTest10 = testRand(nTests = 10000, nTrials = 10)

# Left Trials
plt.hist(RandTest10['left'])
plt.title("Left Side: Block of 10 Trials")
plt.xlabel("number of left trials")
plt.ylabel("number of occurances")

plt.savefig("Left10Trials.eps", format = "eps")
plt.savefig("Left10Trials.png", format = "png")


# Right Trials
plt.hist(RandTest10['right'])
plt.title("Right Side: Block of 10 Trials")
plt.xlabel("number of right trials")
plt.ylabel("number of occurances")

plt.savefig("Right10Trials.eps", format = "eps")
plt.savefig("Right10Trials.png", format = "png")


# Same Side Trials
plt.hist(RandTest10['nochange'])
plt.title("Same Side Transition: Block of 10 Trials")
plt.xlabel("number of same side transitions")
plt.ylabel("number of occurances")

plt.savefig("SameSide10Trials.eps", format = "eps")
plt.savefig("SameSide10Trials.png", format = "png")


# Alternation
plt.hist(RandTest10['alternations'])
plt.title("Alternations for Blocks of 10 Trials")
plt.xlabel("number of alternating transitions between trials")
plt.ylabel("number of occurances")

plt.savefig("Alternations10Trials.eps", format = "eps")
plt.savefig("Alternations10Trials.png", format = "png")

# Left to Right Transitions
plt.hist(RandTest10['leftToright'])
plt.title("Left to Right Transitions: Block of 10 Trials")
plt.xlabel("number of left to right transitions")
plt.ylabel("number of occurances")

plt.savefig("LeftRight10Trials.eps", format = "eps")
plt.savefig("LeftRight10Trials.png", format = "png")


# Right to Left Transitions
plt.hist(RandTest10['rightToleft'])
plt.title("Right to Left Transitions: Block of 10 Trials")
plt.xlabel("number of right to left transitions")
plt.ylabel("number of occurances")

plt.savefig("RightLeft10Trials.eps", format = "eps")
plt.savefig("RightLeftt10Trials.png", format = "png")



#%% for 15 trials
RandTest15 = testRand(nTests = 10000, nTrials = 15)


# Left Trials
plt.hist(RandTest15['left'])
plt.title("Left Side: Block of 15 Trials")
plt.xlabel("number of left trials")
plt.ylabel("number of occurances")

plt.savefig("Left15Trials.eps", format = "eps")
plt.savefig("Left15Trials.png", format = "png")


# Right Trials
plt.hist(RandTest15['right'])
plt.title("Right Side: Block of 15 Trials")
plt.xlabel("number of right trials")
plt.ylabel("number of occurances")

plt.savefig("Right15Trials.eps", format = "eps")
plt.savefig("Right15Trials.png", format = "png")


# Same Side Trials
plt.hist(RandTest15['nochange'])
plt.title("Same Side Transition: Block of 15 Trials")
plt.xlabel("number of same side transitions")
plt.ylabel("number of occurances")

plt.savefig("SameSide15Trials.eps", format = "eps")
plt.savefig("SameSide15Trials.png", format = "png")


# Alternation
plt.hist(RandTest15['alternations'])
plt.title("Alternations for Blocks of 15 Trials")
plt.xlabel("number of alternating transitions between trials")
plt.ylabel("number of occurances")

plt.savefig("Alternations15Trials.eps", format = "eps")
plt.savefig("Alternations15Trials.png", format = "png")

# Left to Right Transitions
plt.hist(RandTest15['leftToright'])
plt.title("Left to Right Transitions: Block of 15 Trials")
plt.xlabel("number of left to right transitions")
plt.ylabel("number of occurances")

plt.savefig("LeftRight15Trials.eps", format = "eps")
plt.savefig("LeftRight15Trials.png", format = "png")


# Right to Left Transitions
plt.hist(RandTest15['rightToleft'])
plt.title("Right to Left Transitions: Block of 15 Trials")
plt.xlabel("number of right to left transitions")
plt.ylabel("number of occurances")

plt.savefig("RightLeft15Trials.eps", format = "eps")
plt.savefig("RightLeftt15Trials.png", format = "png")




# for 20 trials
RandTest20 = testRand(nTests = 10000, nTrials = 20)


# Left Trials
plt.hist(RandTest20['left'])
plt.title("Left Side: Block of 20 Trials")
plt.xlabel("number of left trials")
plt.ylabel("number of occurances")
plt.xticks(range(0,21))
#plt.savefig("Left20Trials.eps", format = "eps")
plt.savefig("Left20Trials.png", format = "png")
plt.savefig("Left20Trials.eps", format = "eps")

# Right Trials
plt.hist(RandTest20['right'])
plt.title("Right Side: Block of 20 Trials")
plt.xlabel("number of right trials")
plt.ylabel("number of occurances")
plt.xticks(range(0,21))
#plt.savefig("Right20Trials.eps", format = "eps")
plt.savefig("Right20Trials.png", format = "png")
plt.savefig("Right20Trials.eps", format = "eps")

# Same Side Trials
plt.hist(RandTest20['nochange'])
plt.title("Same Side Transition: Block of 20 Trials")
plt.xlabel("number of same side transitions")
plt.ylabel("number of occurances")
plt.xticks(range(0,21))
plt.savefig("SameSide20Trials.eps", format = "eps")
plt.savefig("SameSide20Trials.png", format = "png")


# Alternation
plt.hist(RandTest20['alternations'])
plt.title("Alternations for Blocks of 20 Trials")
plt.xlabel("number of alternating transitions between trials")
plt.ylabel("number of occurances")
plt.xticks(range(0,11))
plt.savefig("Alternations20Trials.eps", format = "eps")
plt.savefig("Alternations20Trials.png", format = "png")

# Left to Right Transitions
plt.hist(RandTest20['leftToright'])
plt.title("Left to Right Transitions: Block of 20 Trials")
plt.xlabel("number of left to right transitions")
plt.ylabel("number of occurances")
plt.xticks(range(0,11))
plt.savefig("LeftRight20Trials.eps", format = "eps")
plt.savefig("LeftRight20Trials.png", format = "png")


# Right to Left Transitions
plt.hist(RandTest20['rightToleft'])
plt.title("Right to Left Transitions: Block of 20 Trials")
plt.xlabel("number of right to left transitions")
plt.ylabel("number of occurances")
plt.xticks(range(0,11))
plt.savefig("RightLeft20Trials.eps", format = "eps")
plt.savefig("RightLeftt20Trials.png", format = "png")






# for 25 trials
RandTest25 = testRand(nTests = 10000, nTrials = 25)

plt.hist(RandTest25['alternations'])
plt.title("Alternations for Blocks of 25 Trials")
plt.xlabel("number of alternating transitions between trials")
plt.ylabel("number of occurances")

#plt.savefig("Alternations25Trials.eps", format = "eps")
plt.savefig("Alternations25Trials.png", format = "png")


