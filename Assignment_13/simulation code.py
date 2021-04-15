import numpy as np
import matplotlib.pyplot as plt

#let X be the random variable following Beta(a,b)
#We have to find P(X<0.5)
num_samples= 10000
counter=0
a=2
b=1
x_arr = np.random.beta(a,b, num_samples)  #generating random samples from Beta(2,1)
pdf_arr = 2*x_arr                         #finding the pdf of each sample  

for i in range(0, num_samples):
   
    if x_arr[i]<0.5:              #checking whether each sample is less than 0.5 or not
        counter += 1              #adding counter by 1 if the sample is found less than 0.5
        
p= counter/num_samples            #finding the probability
print("P(X<0.5) = ", p)           #printing the probability value of P(X<0.5)
print("Simulation matches Theoritical result")

#plotting the pdf of the samples
plt.scatter(x_arr, pdf_arr, marker= '.', color ='r')
plt.title("Beta Distribution")
plt.xlabel("x")
plt.ylabel("PDF")
plt.show()
