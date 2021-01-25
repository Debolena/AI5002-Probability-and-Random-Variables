import numpy as np
from scipy.stats import bernoulli

sample_size=100000

prob_B1=0.5
prob_B2=0.5
prob_A_B1= 0.28
prob_A_B2 = 0.30

#Simulations using Bernoulli r.v.
sample_B1= bernoulli.rvs(size= sample_size, p = prob_B1)
sample_B2= bernoulli.rvs(size= sample_size, p = prob_B2)
sample_A_B1= bernoulli.rvs(size= sample_size, p = prob_A_B1)
sample_A_B2= bernoulli.rvs(size= sample_size, p = prob_A_B2)

#Calculating the number of favourable outcomes

n_B1 = np.nonzero(sample_B1 == 1)
n_B2 = np.nonzero(sample_B2 == 1)
n_A_B1 = np.nonzero(sample_A_B1 == 1)
n_A_B2 = np.nonzero(sample_A_B2 == 1)

#calculating the probability using Bayes Theorem
prob= (np.size(n_A_B1)*np.size(n_B1))/((np.size(n_A_B1)*np.size(n_B1))+(np.size(n_A_B2)*np.size(n_B2)))

print("Given the patient has heart attack, the probability that the patient followed the course of yoga and meditation is: ", prob)