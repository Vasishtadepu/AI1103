import numpy as np 
from matplotlib import pyplot as plt 


def F(x):
    if (x<1):
        return 0
    elif (1<=x<2):
        return 0.5
    elif (2<=x<3):
        return 5/6
    else:
        return 1           


X0 = np.linspace(0,1,10000)
X1 = np.linspace(1,2,10000)
X2 = np.linspace(2,3,10000)
X3 = np.linspace(3,4,10000)

Y0 = [F(x) for x in X0]
Y1 = [F(x) for x in X1]
Y2 = [F(x) for x in X2]
Y3 = [F(x) for x in X3]


plt.plot(X0,Y0,c = 'yellow')
plt.plot(X1,Y1,c = 'blue')
plt.plot(X2,Y2, c = 'green')
plt.plot(X3,Y3, c = 'red')
plt.xlabel('x values')
plt.ylabel('F(x) c.d.f')

plt.show()