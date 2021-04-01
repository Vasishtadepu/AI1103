import numpy as np
from matplotlib import pyplot as plt

#defining a function with mu value as 2
def h(x):
    if x>1:
        return 1/(x**2)
    else:
        return 0    


#defining a pdf taking mu values as 9
def g(x):
    if x>1:
        return 8/(x**9)
    else:
        return 0    


#defining a pdf taking mu values as 5.5
def f(x):
    if x>1:
        return 9/(2*(x**5.5))
    else:
        return 0            


#defining what values will be considerd for x

X = np.linspace(1.5,10,100000)

#finding the corresponding Y values for each pdf formed above 
Y_2 = [h(x) for x in X]
Y_9 = [g(x) for x in X]
Y_5 = [f(x) for x in X]

#plotting the graphs
plt.xlabel('X values')
plt.ylabel('p(x)')
plt.plot(X,Y_2,c = 'green',label = '\u03BC = 2')
plt.plot(X,Y_9,c = 'red',label = '\u03BC = 9')
plt.plot(X,Y_5, c ='blue', label = '\u03BC = 5.5')
plt.legend(loc = 'upper right')
plt.show()