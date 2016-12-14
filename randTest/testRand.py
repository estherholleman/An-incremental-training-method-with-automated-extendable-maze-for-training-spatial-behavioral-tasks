import numpy
from myFunctions import generate_flavors
    
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
            d = numpy.diff(sides)
            # trials between which the flavor changed
            flavSwaps = numpy.nonzero(d)
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
        
        # use results['alternations'] to bring up alternations, etc.
    
        # plt.hist(results['alternations'])
     