from random import randint
import numpy as np

def generate_flavors(randLength = 4405, choices = [0,1]):
    in_row = 1
    p_x= randint(0, len(choices)-1)
    choices_list = [p_x]
    counter = 0
    
    while len(choices_list) < randLength:
        counter = counter + 1
        x = randint(0, len(choices)-1)
        if p_x == x:
            if in_row <3:
                in_row +=1
                choices_list.append(x)
                p_x = x
            else:
                continue
        else:
            choices_list.append(x)
            p_x = x
            in_row = 1
     
     
        if counter > 19:
            d = np.diff(choices_list[counter-19 : counter])
            flavChange = np.nonzero(d)
            nflavChange = len(flavChange[0])
            
            if nflavChange > 10:
                in_row = 1
                p_x= randint(0, len(choices)-1)
                choices_list[counter-19 : counter] = [p_x]

    return choices_list 