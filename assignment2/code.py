import numpy as np 
from scipy.stats import binom 
import random 
from array import *
from matplotlib import pyplot as plt
import pandas as pd
#defining variance and other arrays
k = []
p = []
mean = []
var_theo = []
var_form = []
exp_squared = []


for i in range(0,10):
    k.append(random.randint(2,11))
    p.append(random.random())
    exp_squared.append(0)
    var_form.append(0)
    
for i in range(0,10):
    mean.append(binom.mean(k[i],p[i]))
    var_theo.append(binom.var(k[i],p[i]))

for i in range(0,10):
    for j in range(0,k[i] + 1):
        exp_squared [i] = exp_squared [i] + (j**2)*binom.pmf(j,k[i],p[i])

for i in range(0,10):
    var_form [i] = exp_squared [i] - mean [i] * mean [i]


dev_x = var_form
dev_y = var_theo
x = [0,2.5]
y = [0,2.5]
plt.xlabel('Variances from formula')
plt.ylabel('Variances from In built function')
plt.title('Verification of the formula')
plt.scatter(dev_x,dev_y, c = 'green')
plt.plot(x,y,label = 'x=y line')
plt.legend(loc = 'upper right')


plt.show()