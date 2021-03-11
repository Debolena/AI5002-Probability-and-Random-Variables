import numpy as np
from scipy.stats import bernoulli

sample_size=100000

prob_A=0.3
prob_B=0.4

#Simulations using Bernoulli r.v.
sample_A= bernoulli.rvs(size= sample_size, p = prob_A)
sample_B= bernoulli.rvs(size= sample_size, p = prob_B)


#calculating P(A intersection B):
count=0
for i in range(sample_size):
    if sample_A[i] == 1 and sample_B[i] == 1:
        count +=1
        
#finding probability of A intersection B
prob_AB= count/sample_size        
print("P(A intersection B) = ", prob_AB)
print("P(A|B) = ", prob_AB/prob_B, "which is approximately equal to ", prob_A)
print("P(B|A) = ", prob_AB/prob_A, "which is approximately equal to ", prob_B)

        