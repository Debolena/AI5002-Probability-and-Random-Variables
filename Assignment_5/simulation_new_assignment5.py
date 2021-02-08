import numpy as np
import random
from matplotlib import pyplot as plt
from scipy.stats import uniform

# X is random variable which has 3 outcomes
#Let X=0,1 and 2 denote the event for insured scooter driver, car driver and truck drivers.
p=[1.0/6, 1.0/3, 1.0/2] #given distribution P(X=0)=1/6 ,P(X=1)=1/3 ,P(X=2)=1/2
num_trials = 12000

cdfp=[0.0,0.0,0,0]
cdfp=np.cumsum(p)  # Cummulative distribution of pmf given
#print(cdfp)

def randomsamples(num_trials,p):
 Samples=[x for x in range(num_trials)] # creating string array for storage of samples
 alpha=["0","1","2"]
 for i in range(num_trials):
      U=np.random.rand() #random number between 0 and 1
      if (U<=cdfp[0]):
         Samples[i]=alpha[0]
      elif (U>cdfp[0]) and (U<cdfp[1]):
         Samples[i]=alpha[1]
      elif (U>cdfp[1]):
         Samples[i]=alpha[2]
      
 Samples=str(Samples)
 return(Samples)

y=randomsamples(num_trials,p)

#print("Generated samples according to the probability distribution is \n")
#print(y)

count0=y.count("0")
count1=y.count("1")
count2=y.count("2")

print("generated no. of insured scooter drivers= ", count0)
print("generated no. of insured car drivers= ", count1)
print("generated no. of insured truck drivers= ", count2)

print("\nActual probabilities are",p)
print("\nSimulation probabilities are given by: \n")

p_simul=[count0/num_trials,count1/num_trials,count2/num_trials]

print("Probability for X=0 i.e insured scooter drivers is ",count0/num_trials)
print("Probability for X=1 i.e insured car drivers is ",count1/num_trials)
print("Probability for X=2 i.e insured truck drivers is ",count2/num_trials)

print("the total no.of insured scooter drivers, car drivers and truck drivers from simulation is = ", count0+ count1+ count2) 
print("adding the simulated probabilities = ", np.sum(p_simul) )

plt.plot(p,p_simul,marker="o",color="red")
plt.xlabel("Actual probability")
plt.ylabel("probability after simulation of random variables")
plt.title("simulation versus actual probabilities")
plt.show()
