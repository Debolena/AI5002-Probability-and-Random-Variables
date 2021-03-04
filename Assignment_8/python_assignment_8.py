import numpy as np
import random
from matplotlib import pyplot as plt

p=[0.1, 0.15, 0.30, 0.30, 0.15] #according to given pmf
num_trials = 100000

cdfp=[0.0,0.0,0.0,0.0,0.0,0.0]
cdfp=np.cumsum(p)  # Cummulative distribution of pmf given
print("the cdf (theoritical) is:\n", cdfp)

samples= np.zeros(num_trials)
count0 = count1 = count2 = count3 = count4 = 0

for i in range(num_trials):
      U=np.random.rand() #random number between 0 and 1
      if (U<=cdfp[0]):
         samples[i]=0
         count0 +=1
      elif (U>cdfp[0]) and (U<cdfp[1]):
         samples[i]=1
         count1 +=1
      elif (U>cdfp[1]) and (U<cdfp[2]):
         samples[i]=2
         count2 +=1
      elif (U>cdfp[2]) and (U< cdfp[3]):
          samples[i]=3
          count3 +=1
      else:
          samples[i]=4
          count4 +=1

print("the generated sample according to the pmf is:\n", samples)

p_simulated=[count0/num_trials, count1/num_trials, count2/num_trials, count3/num_trials, count4/num_trials]

print("the simulated probabilities of studying 0 hour, 1 hour, 2 hours, 3 hours and 4 hours are: \n", p_simulated, "respectively")
print("sum of the original probabilities = ", sum(p) )
print("sum of the simulated probabilities = ", sum(p_simulated) )
print("favourable outcomes generated for studying 0,1,2,3,4 hours are: ", count0, count1, count2, count3, count4, "respectively")
print("sum of these counts= ", count0+count1+count2+count3+count4, "= total number of trials")

plt.plot(p,p_simulated,marker="o",color="red")
plt.xlabel("Actual probability")
plt.ylabel("probability after simulation of random variables")
plt.title("simulation versus actual probabilities")
plt.show()

#plotting pmf for theory
x=[0,1,2,3,4]
plt.title("plot of PMF (theoritical)")
plt.xlabel('x')
plt.ylabel('P(X=x)')
plt.bar(x, p)
plt.show()

#plotting pmf for simulation
plt.title("plot of PMF (simulation)")
plt.xlabel('x')
plt.ylabel('P(X=x)')
plt.bar(x, p_simulated)
plt.show()

#for plotting the cdf theoritical
plt.bar(x, cdfp)
plt.title('cdf plot (theoritical)')
plt.xlabel('x')
plt.ylabel('cdf')
plt.show()

#for plotting the cdf in simulation
cdf_p_simulated =np.cumsum(p_simulated)
print("the cdf (simulated):\n ", cdf_p_simulated)
plt.bar(x, cdf_p_simulated)
plt.title('cdf plot (simulation)')
plt.xlabel('x')
plt.ylabel('cdf')
plt.show()
