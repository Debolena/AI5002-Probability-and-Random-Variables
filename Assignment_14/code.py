import numpy as np
import matplotlib.pyplot as plt

num_samples= 10000

a=-1
b=4
x_arr = np.random.uniform(a,b, num_samples)  #generating random samples from Uniform(a,b)
pdf=[]

#constructing the pdf array
for i in range(0, num_samples):
    if x_arr[i]<= 1:              
        pdf.append(0.2)             
    if x_arr[i]<=4 and x_arr[i]>1:
        pdf.append(0.1)
   

#plotting the pdf of the samples
plt.scatter(x_arr, pdf, marker= '.', color ='r')
plt.title("plot of f(x)")
plt.xlabel("x")
plt.ylabel("PDF: f(x)")
plt.show()
