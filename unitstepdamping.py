import numpy as np
import math
import matplotlib.pyplot as plt
a=float(input("Enter a value="))
b=float(input("Enter b value="))
Y=np.array([])
def u(n):
    if(n>=0):
        return 1
    else:
        return 0
t=np.linspace(0,10,1000)
for i in t:
    y=((np.exp(-a*i)*np.sin(math.sqrt((b-(a**2/4))*i))*u(i)))/(math.sqrt(b-(a**2/4)))
    Y= np.append(Y,[y])
plt.plot(t,Y)
plt.show()
