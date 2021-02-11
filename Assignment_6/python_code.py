import numpy as np
from scipy.stats import bernoulli

sample_size= 100000

#given
prob_A = 0.2
prob_B_alone= 0.15
prob_AB = 0.15

#Simulations using Bernoulli r.v.
sample_A= bernoulli.rvs(size= sample_size, p = prob_A)
sample_B_alone= bernoulli.rvs(size= sample_size, p = prob_B_alone)

#Calculating the number of favourable outcomes

A_nonzero = np.nonzero(sample_A == 1)
B_alone_ = np.nonzero(sample_B_alone == 1)
n_A= np.size(A_nonzero)
n_B_alone= np.size(B_alone_)

#calculating A union B
prob_AorB = (n_A +n_B_alone)/sample_size
print("P(A U B) = ", prob_AorB)

#calculating prob of B
prob_B= prob_AorB - prob_A + prob_AB
print("P(B fails) = ", prob_B ) 

#answers
print("P(A fails | B has failed) = ", prob_AB/prob_B)
print("P(A fails alone) = ", prob_A - prob_AB)