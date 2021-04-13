import numpy as np
import matplotlib.pyplot as plt

#given is exponential distribution with mean = 1 i.e scale parameter = 1
#let X be the random variable following Exp(1)
#We have to find P(X>1)
num_samples= 10000
counter=0
x_arr=[]
pdf_arr=[]

for i in range(0, num_samples):
    x = np.random.exponential(1)  #generating one random sample from exp(1)
    x_arr.append(x)               #creating a list to store the samples
    pdf= np.exp(-x)               #calculating the pdf of each random sample x
    pdf_arr.append(pdf)           #creating a list to store the pdf values of all the samples
    
    if x>1:                       #checking whether the sample is greater than 1
        counter += 1              #adding counter by 1 if the sample is found greater than 1
        
p= counter/num_samples            #finding the probability
print("P(X>1) = ", p)             #printing the probability value of P(X>1)

#plotting the curve of the samples from exponential distribution
plt.scatter(x_arr, pdf_arr, marker= '.', color ='r')
plt.title("Exponential Distribution")
plt.xlabel("x")
plt.ylabel("PDF")
plt.show()