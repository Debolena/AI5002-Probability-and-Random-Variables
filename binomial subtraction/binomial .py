import numpy as np

num_simulations= 1000000
n1= 10
n2= 15
p= 0.5

#let X1 ~ Bin(n1, p) and X2 ~ Bin(n2, p). #generating samples of X1 and X2
sample_X1 = np.random.binomial(n1, p, num_simulations)
sample_X2 = np.random.binomial(n2, p, num_simulations)
#print("X1;\n", sample_X1)
#print("X2:\n", sample_X2)

#Y= X1+X2. # adding the samples of X1 and X2
Y=[]
for i in range(num_simulations):
    Y.append(sample_X1[i] + sample_X2[i])    
    
#print("Y:\n", Y)
Y= np.array(Y) #converting list into numpy array
print("Mean of Y= ", np.mean(Y))
print("Variance of Y= ", np.var(Y))
print("Max of Y = ", np.amax(Y))
print("Min of Y = ", np.amin(Y))
print("Range of Y = ", np.amax(Y)- np.amin(Y))


#Y= X1+X2 ~ Bin(n1+n2, p). ##generating samples of Y from this distribution
Y_simulated = np.random.binomial(n1+n2, p, num_simulations)
#print("Y simulated:\n", Y_simulated)
print("\nMean of Y simulated= ", np.mean(Y_simulated))
print("Variance of Y simulated= ", np.var(Y_simulated))
print("Max of Y simulated = ", np.amax(Y_simulated))
print("Min of Y simulated= ", np.amin(Y_simulated))
print("Range of Y simulated= ", np.amax(Y_simulated)- np.amin(Y_simulated))

print("\nFrom the values of statistical measures it is clear Y follows the same distribution for both the cases.")

