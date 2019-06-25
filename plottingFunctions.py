# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 13:10:15 2016

@author: esther
"""

from __future__ import division

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patch
import matplotlib.ticker as ticker



def plotScoresClean(ScoresPerDay):
    
    PhaseLengths = [];
    phases = range(1,7)
    phase = 1
    
    for phase in phases:  
        PhaseLengths.append(len(ScoresPerDay.iloc[ScoresPerDay.index.get_level_values('Phase') == phase]))
    
    DaysInPhase = np.cumsum(PhaseLengths)
  
    ScoresPerDay['avg'] = ScoresPerDay.mean(axis = 1)
    
    ax = ScoresPerDay.plot(colormap = 'magma', title = "LEARNING CURVES - SCORING MANUAL REWARDS",figsize = (11.69,8.27))

    patches,labels = ax.get_legend_handles_labels()
    ax.set_ylabel("% Correct")
    ax.set_xlabel("")
    # make average thicker and black
    ax.lines[-1].set_linewidth(5)
    ax.lines[-1].set_color('black')  
    
    # clean up plot
    ax.spines["top"].set_visible(False)    
    ax.spines["bottom"].set_visible(False)    
    ax.spines["right"].set_color('#b1b3b6')
    ax.spines["right"].set_linestyle('--')
    ax.spines["left"].set_visible(True)  
    
    ax.get_xaxis().tick_bottom()    
    ax.get_yaxis().tick_left() 
    
    plt.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="off", left="off", right="off", labelleft="on")   

    ax.axvline(0, color='#b1b3b6', linestyle='--', lw = 1)
 
    for p in DaysInPhase:
        ax.axvline(p, color='#b1b3b6', linestyle='--', lw = 1)

    ax.legend(patches,labels,loc='center left', framealpha = 0.4, title = "Rats: ", frameon = False, bbox_to_anchor=(1,0.2))
    
    plt.savefig("ScoresPerDayManualRewards.eps",format = "eps")
    plt.savefig("ScoresPerDayManualRewards.png",format = "png")




def plotScoresPatches(ScoresPerDay):
    
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


def plotIt(Scores, title = None, ylabel = None, Phase = False, Norm = False, ylim = []):
    
    if Phase:
        Scores = Scores.groupby(level ="Phase").mean()
    
    PhaseLengths = [];
    phases = range(1,7)
    phase = 1
    
    for phase in phases:  
        PhaseLengths.append(len(Scores.iloc[Scores.index.get_level_values('Phase') == phase]))
    #print PhaseLengths
    DaysInPhase = np.cumsum(PhaseLengths)
    DaysInPhase = np.append(DaysInPhase,69)
    Scores["Avg"] = Scores.mean(axis = 1)
    
    ax = Scores.plot(colormap = 'magma', title = title ,figsize = (11.69,8.27))
    
    ax.xaxis.set_major_locator(ticker.FixedLocator([i for i in DaysInPhase]))
    ax.set_xticklabels(DaysInPhase + 1)
    patches,labels = ax.get_legend_handles_labels()
    
    ax.set_ylabel(ylabel)
    if len(ylim) > 0:
        ax.set_ylim(ylim)
    ax.set_xlabel('Training Days')
    # make average thicker and black
    ax.lines[-1].set_linewidth(5)
    ax.lines[-1].set_color('black')  
    
    # clean up plot
    ax.spines["top"].set_visible(False)    
    ax.spines["bottom"].set_visible(True)    
    ax.spines["right"].set_color('#b1b3b6')
    ax.spines["right"].set_linestyle('--')
    ax.spines["left"].set_visible(True)  
    ax.get_xaxis().tick_bottom()      
    ax.get_yaxis().tick_left() 
    
    ax.legend(patches,labels,loc='center left', title = "Animals:", framealpha = 0.4, frameon = False, bbox_to_anchor=(1,0.2))
    
    if Norm:
        ax.axhline(y =1,xmin = 0, xmax=1, linewidth = 2, color = 'grey', ls ="--")
#    else:
#        ax.set_ylim([0,100])
        
    for p in DaysInPhase:
        ax.axvline(p, color='#b1b3b6', linestyle='--', lw = 1)
    
    plt.savefig(title + ".png",format = "png")
    plt.savefig(title + ".eps",format = "eps")

## Freeze this one for now, the reaction times of the strategies don't say much

#winStayRT = rtFiltered[strategyAppliedWinStay]
#winStayRTStats = winStayRT.groupby(level = ["Phase","Day"]).aggregate([np.median,np.mean, np.std])
#winStayRTStats = winStayRTStats.interpolate()
#
#winShiftRT = rtFiltered[strategyAppliedWinShift]
#winShiftRTStats = winShiftRT.groupby(level = ["Phase","Day"]).aggregate([np.median,np.mean, np.std])
#winShiftRTStats = winShiftRTStats.interpolate()
#
#altRT = rtFiltered[strategyAppliedAlt]
#altRTStats = altRT.groupby(level = ["Phase","Day"]).aggregate([np.median,np.mean, np.std])
#altRTStats = altRTStats.interpolate()



#def plotStrategyStats(strategies):
#    #strategies should be: [WinStayRTStats,WinShiftRTStats,altRTStats]
#
#    #    medianWinStayRT = winStayRTStats.xs("median", level = 1, axis = 1)
##    meanWinStayRT = winStayRTStats.xs("mean", level = 1, axis = 1)
##    
##    medianWinShiftRT = winShiftRTStats.xs("median", level = 1, axis = 1)
##    meanWinShiftRT = winShiftRTStats.xs("mean", level = 1, axis = 1)
##    
##    medianAltRT = altRTStats.xs("median", level = 1, axis = 1)
##    meanAltRT = altRTStats.xs("mean", level = 1, axis = 1)
#
#
#    strategies = ["winStay","winShift","alt"]
#    stats = ["mean", "median"]
#    
#    for s, strategy in strategies:
#        
#        RtT = rtFiltered[strategyAppliedWinShift]
#        
#        for st, stat in stats:
#            
#            f, axarr = plt.subplots(3,2);
#            axarr[s,st].plot(strategy+RTStats.xs("mean", level = 1, axis = 1));
#            axarr[s,st].set_title(stat);
#        

def plotNormScoresScatter(stratScoreAnimal,stratScoreRand, strategyName, mean = False):
    # strategyName should be a string, e.g: "Alternation"
    
    animals = ["1","2","3","4"]
    
    f, axs = plt.subplots(4,1,figsize = (8,20))
    
    ax = axs.ravel()
    
    for animal in animals:
    
        # indexing 
        #rat = stratScoreAnimal[animal]
#        rand = stratScoreRand[animal]

        phases = range(1,8)

        #fig, ax = plt.subplots()
        
        for phase in phases:
            
            if mean:
                ax[int(animal)-1].plot(stratScoreRand.loc[phase,animal].mean(),stratScoreAnimal.loc[phase,animal].mean(), marker='o', linestyle='', ms=6, label= "Phase " + str(phase), )
            else:    
                ax[int(animal)-1].plot(stratScoreRand.loc[phase,animal],stratScoreAnimal.loc[phase,animal], marker='o', linestyle='', ms=6, label= "Phase " + str(phase), )
           
            ax[int(animal)-1].legend(numpoints = 1)
            ax[int(animal)-1].set(xlim=(0,100), ylim=(0,100))
            ax[int(animal)-1].set_xlabel("% of trials where strategy was present in randomization")
            ax[int(animal)-1].set_ylabel("% of trials where the rats choice == the strategy")
            ax[int(animal)-1].set_title(strategyName + " Rat " + animal)
            ax[int(animal)-1].set(adjustable='box-forced', aspect='equal')
            # plot unity line
            ax[int(animal)-1].plot(ax[int(animal)-1].get_xlim(), ax[int(animal)-1].get_ylim(), ls="--", c=".3") 
    if mean:
        plt.savefig(strategyName + "ScatterAverages.png",format = "png")
        plt.savefig(strategyName + "ScatterAverages.eps",format = "eps")            
    else:
        plt.savefig(strategyName + "Scatter.png",format = "png")
        plt.savefig(strategyName + "Scatter.eps",format = "eps")  
        
        
        
def plotStrategyNorms(stratScoreAnimal,stratScoreRand, strategyName):
    # plot the difference between the points in the scatter plot and the unity line
    
    stratDiff = abs(stratScoreAnimal - stratScoreRand)
    
    plotIt(stratDiff, title = 'Variance From Optimal Use of ' + strategyName + ' Strategy', ylabel = "animal score (% correct) - rand score (% correct)", Phase = False, Norm = False)

#    stratAvgs = stratDiff.groupby(level = "Phase").mean()
#    stratAvgs["Avg"] = stratAvgs.mean(axis =1)


def plotCorrectAgainstIncorrectScatter(correct,incorrect, mean = False):
    
    animals = ["1","2","3","4"]
    
    f, axs = plt.subplots(4,1,figsize = (8,20))
    
    ax = axs.ravel()
    
    for animal in animals:
    
        # indexing 
        #rat = stratScoreAnimal[animal]
#        rand = stratScoreRand[animal]

        phases = range(1,8)

        #fig, ax = plt.subplots()
        
        for phase in phases:
            
            if mean:
                ax[int(animal)-1].plot(incorrect.loc[phase,animal].mean(),correct.loc[phase,animal].mean(), marker='o', linestyle='', ms=6, label= "Phase " + str(phase))
            else:    
                ax[int(animal)-1].plot(incorrect.loc[phase,animal],correct.loc[phase,animal], marker='o', linestyle='', ms=6, label= "Phase " + str(phase))
           
            ax[int(animal)-1].legend(numpoints = 1)
            ax[int(animal)-1].set(xlim=(0,100), ylim=(0,100))
            ax[int(animal)-1].set_xlabel("% of incorrect trials")
            ax[int(animal)-1].set_ylabel("% of correct trials")
            ax[int(animal)-1].set_title("Correct vs. Incorrect Rat " + animal)
                
                
                
#                
#def plotCorrectAgainstIncorrectDays(correct,incorrect, mean = False):
#    
#    animals = ["1","2","3","4"]
#    
##    f, axs = plt.subplots(4,1,figsize = (8,20))
##    
##    ax = axs.ravel()
#    
#    for animal in animals:
#
#        phases = range(1,8)
#        
#        f, axs = plt.subplots(len(phases),4)
#        ax = axs.ravel()
#        
#        for phase in phases:
#            
#            group = correct.loc[phase,animal]
#            days = group.index.get_level_values('Day')
#
#            for day in days:
#                
#                if mean:
#                    ax[phase + int(animal)-1].plot(incorrect.loc[phase,animal,day].mean(),correct.loc[phase,animal,day].mean(), marker='o', linestyle='', ms=6, label= "Day " + str(day), subplots = True)
#                else:    
#                    ax[phase + int(animal)-1].plot(incorrect.loc[phase,animal,day],correct.loc[phase,animal,day], marker='o', linestyle='', ms=6, label= "Day" + str(day),subplots = True)
#               
#                ax[phase + int(animal)-1].legend(numpoints = 1)
#                ax[phase + int(animal)-1].set(xlim=(0,100), ylim=(0,100))
#                ax[phase + int(animal)-1].set_xlabel("% of incorrect trials")
#                ax[phase + int(animal)-1].set_ylabel("% of correct trials")
#                ax[phase + int(animal)-1].set_title("Correct vs. Incorrect Rat " + animal)

def compareScoringMethodsScatter(method1,method2, method1name = "RewardScores", method2name = "ManualScores", phases = range(5,8)):    

    f, ax = plt.subplots()    
    #ax = axs.ravel()
    
    for phase in phases:
        

        ax.plot(method1.loc[phase].mean(),method2.loc[phase].mean(), marker='o', linestyle='', ms=6, label= "Phase " + str(phase))
 
       
        ax.legend(numpoints = 1, loc = 4, fontsize = 9)
        ax.set(xlim=(0,100), ylim=(0,100))
        ax.set_xlabel("% of correct trials " + method1name)
        ax.set_ylabel("% of correct trials " + method2name)
        ax.set(adjustable='box-forced', aspect='equal')
        
        title = method1name + " Plotted Against " + method2name
        ax.set_title(title)
        
        ax.plot(ax.get_xlim(), ax.get_ylim(), ls="--", c=".3")

    plt.savefig(title + ".png",format = "png")
    plt.savefig(title + ".eps",format = "eps")
    
    
    
    
    
    
    