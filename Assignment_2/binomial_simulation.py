import numpy as np
p= 0.1 #probability of success i.e.probability of getting a defective bulb
num_simulations = 100000
n= 5
sample = np.random.binomial(n, p, num_simulations)
print("the binomial simulations are: ", sample)

#favourable outcomes:
#counting the number of simulations which gave that none of the bulbs were defective out of a sample of 5 bulbs
# i.e we have to check how many "x = 0"
count=0
for i in sample:
    if i==0:
        count += 1
        
prob = count/num_simulations  #calculating the prob that none of the 5 bulbs are defective

print("probability that none are defective out of a sample of 5 bulbs = ", prob)        