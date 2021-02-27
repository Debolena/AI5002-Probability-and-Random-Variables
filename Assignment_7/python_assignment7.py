import numpy as np
from scipy.stats import bernoulli

sample_size=100000

#defining probabilities
prob_A= 13/52
prob_A_compli = 39/52
prob_B_A= (12*11)/(51*50)
prob_B_A_compli = (13*12)/(51*50)

#Simulations using Bernoulli R.V.
sample_A= bernoulli.rvs(size= sample_size, p = prob_A)
sample_A_compli= bernoulli.rvs(size= sample_size, p = prob_A_compli)
sample_B_A= bernoulli.rvs(size= sample_size, p = prob_B_A)
sample_B_A_compli= bernoulli.rvs(size= sample_size, p = prob_B_A_compli)

#Calculating the number of favourable outcomes
n_A = np.nonzero(sample_A == 1)
n_A_compli = np.nonzero(sample_A_compli == 1)
n_B_A = np.nonzero(sample_B_A == 1)
n_B_A_compli = np.nonzero(sample_B_A_compli == 1)

#calculating the probability using Bayes Theorem
prob= (np.size(n_B_A)*np.size(n_A))/((np.size(n_B_A)*np.size(n_A))+(np.size(n_B_A_compli)*np.size(n_A_compli)))

print("Probability that the lost card is diamond = P(A|B) = ", prob)


