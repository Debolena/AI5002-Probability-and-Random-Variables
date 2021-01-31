import numpy as np

sample=100000

x = np.random.uniform(low=0, high=9, size=sample) #generating uniform samples along the length of the rectangle, along x-axis
y = np.random.uniform(low=0, high=4.5, size=sample) #generating uniform samples along the breadth of the rectangle, along y-axis

count=0
for (i,j) in zip(x,y): #taking each point (x,y)
    if i>6.0 and j>2.0:  #checking condition whether the point lies in the lake
        count= count+1   #counting the number of points lying in the lake
     
p= count/ sample         #calculating prob= no. of points in the lake/total no.of points in the rectangle
print("probability that the helicopter crashed inside the lake = ", p)        