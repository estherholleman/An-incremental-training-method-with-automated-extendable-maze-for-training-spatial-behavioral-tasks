# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 13:10:15 2016

@author: esther
"""
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


def plotIt(Scores, title = None, ylabel = None, Phase = False, Norm = False):
    
    if Phase:
        Scores = Scores.groupby(level ="Phase").mean()
    
    PhaseLengths = [];
    phases = range(1,7)
    phase = 1
    
    for phase in phases:  
        PhaseLengths.append(len(Scores.iloc[Scores.index.get_level_values('Phase') == phase]))
    
    DaysInPhase = np.cumsum(PhaseLengths)
    DaysInPhase = np.append(DaysInPhase,69)
    Scores["Avg"] = Scores.mean(axis = 1)
    
    ax = Scores.plot(colormap = 'magma', title = title ,figsize = (11.69,8.27))
    
    ax.xaxis.set_major_locator(ticker.FixedLocator([i for i in DaysInPhase]))
    ax.set_xticklabels(DaysInPhase + 1)
    patches,labels = ax.get_legend_handles_labels()
    
    ax.set_ylabel(ylabel)
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
    
    for p in DaysInPhase:
        ax.axvline(p, color='#b1b3b6', linestyle='--', lw = 1)
    
    plt.savefig(title + ".png",format = "png")
    

