import numpy as np
import math
import matplotlib.pyplot as plt
a=float(input("Enter a value="))
b=float(input("Enter b value="))
def u(n):
    if(n>=0):
        return 1
    else:
        return 0
t=np.linspace(0,10,1000)

y=((np.exp(-a*t)*np.sin(math.sqrt((b-(a**2/4))*t))*u(t)))/(math.sqrt(b-(a**2/4)))
plt.plot(t,y)
plt.show()
