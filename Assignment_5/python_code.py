import numpy as np
from scipy.stats import bernoulli

sample_size=1000000

prob_B1=1.0/6  #insured scooter drivers
prob_B2=1.0/3  #insured car drivers
prob_B3=1.0/2  #insured truck drivers

prob_A_B1 = 0.01  #accident|scooter driver
prob_A_B2 = 0.03  #accident|car driver
prob_A_B3 = 0.15  #accident|truck driver


#Simulations using Bernoulli r.v.
sample_B1= bernoulli.rvs(size= sample_size, p = prob_B1)
sample_B2= bernoulli.rvs(size= sample_size, p = prob_B2)
sample_B3= bernoulli.rvs(size= sample_size, p = prob_B3)
sample_A_B1= bernoulli.rvs(size= sample_size, p = prob_A_B1)
sample_A_B2= bernoulli.rvs(size= sample_size, p = prob_A_B2)
sample_A_B3= bernoulli.rvs(size= sample_size, p = prob_A_B3)

#Calculating the number of favourable outcomes

n_B1 = np.nonzero(sample_B1 == 1)
n_B2 = np.nonzero(sample_B2 == 1)
n_B3 = np.nonzero(sample_B3 == 1)
n_A_B1 = np.nonzero(sample_A_B1 == 1)
n_A_B2 = np.nonzero(sample_A_B2 == 1)
n_A_B3 = np.nonzero(sample_A_B3 == 1)

#calculating the probability using Bayes Theorem
prob= (np.size(n_A_B1)*np.size(n_B1))/((np.size(n_A_B1)*np.size(n_B1))+(np.size(n_A_B2)*np.size(n_B2))+ (np.size(n_A_B3)*np.size(n_B3)))

print("P(scooter driver given an insured person meets with an accident) ", prob)