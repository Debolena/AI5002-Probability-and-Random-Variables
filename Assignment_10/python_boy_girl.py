import numpy as np
from scipy.stats import bernoulli
import matplotlib.pyplot as plt

sample_size=100000

#probability of a girl
prob_X= 25.0/40

#Simulations using Bernoulli r.v.
sample_X= bernoulli.rvs(size= sample_size, p = prob_X)

#calculating the number of 1's i.e the number of favourable outcomes
n_X = np.size(np.nonzero(sample_X == 1))

#calculating simulated probability of a girl
prob_girl = n_X/sample_size

print("probability of getting a girl's name = ", prob_girl)
print("probability of getting a boy's name = ", 1-prob_girl)

#plotting the probabilities of a girl or a boy
gender= ['girl', 'boy']
prob_sim= [prob_girl, 1- prob_girl]
prob_theory = [prob_X, 1- prob_X]
plt.stem(gender, prob_theory, markerfmt='ro', label='theoritical')
plt.stem(gender, prob_sim, markerfmt='y.', label='simulation')
plt.legend()
plt.ylabel('probabilities')
plt.title('plotting probabilities of a boy or girl')
plt.show()
