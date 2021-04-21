import numpy as np
import matplotlib.pyplot as plt

num_samples= 10000

a=-1
b=4
x_arr = np.random.uniform(a,b, num_samples)  #generating random samples from Uniform(a,b)
#pdf_arr=[]
cdf_arr=[]

#constructing the pdf and cdf array
for i in range(0, num_samples):
    if x_arr[i]<= 1:              
        #pdf_arr.append(0.2)
        cdf = 0.2*(x_arr[i]+1)
        cdf_arr.append(cdf)             
    if x_arr[i]<=4 and x_arr[i]>1:
        #pdf_arr.append(0.1)
        cdf= 0.4 + 0.1*(x_arr[i]-1)
        cdf_arr.append(cdf)
   

#creating the part of cdf where F(x)=1, for x>4
x1=np.arange(4, 5, 0.01)               #creating the x values for plotting
new_x1 = np.concatenate((x_arr, x1))   #concatenating with original x samples
for i in range(len(x1)):
    cdf_arr.append(1)                  #extending the cdf array with 1s

#creating the part of cdf where F(x)=0, for x<-1
cdf_start=[]
x2=np.arange(-2,-1,0.01)               #creating the x values for plotting
new_x2= np.concatenate((x2, new_x1))   #concatenating with the previous array
for i in range(len(x2)):
    cdf_start.append(0)                #extending the cdf array with 0s in the beginning

cdf_final= cdf_start + cdf_arr         #forming the complete cdf array for plotting


#plotting cdf
plt.scatter(new_x2, cdf_final, s=0.1)
plt.title("CDF plot F(x)")
plt.xlabel("x")
plt.ylabel('CDF: F(x)')
plt.show()
