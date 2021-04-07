import numpy as np
import random

# let 0 represent a black ball
# and 1 represents a red ball

count=0                                      #setting a counter to count the number of red balls after 2nd draw
for i in range(0, 10000):                    #repeating the experiment 10,000 times
    urn=np.array([1,0,1,0,1,0,0,0,1,1])      #initializing urn with red and black balls randomly
    np.random.shuffle(urn)                   #shuffling the elements of the urn randomly
    draw1_index= random.randint(0,9)         #picking a ball for the first draw by selecting a random index
    urn = np.delete(urn, draw1_index)        #removing the selected ball from the urn
    draw2_index= random.randint(0,8)         #drawing a random integer for selecting a random index
    draw2= urn[draw2_index]                  #drawing another ball by using the random index
    
    if draw2 == 1:                           #checking whether the ball is red or not
        count += 1                           #count increases if the selected ball is red 
        
        
pr= count/10000                              #finding the probability of getting red ball in the 2nd draw
print("Probability of getting a red ball in the 2nd draw = ", pr)
print("CONCLUSION: Theory matches Simulation.")        