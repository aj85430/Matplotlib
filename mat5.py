import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,2.0*np.pi,101)
y=np.sin(x)

xnumbers=np.linspace(0,7,15)
ynumbers=np.linspace(-1,1,11)

plt.plot(x,y,color='r',label='sin')
plt.xlabel('angle in radians')
plt.ylabel('magnitude')
plt.title('trigonometric function')
plt.grid()
plt.xticks(xnumbers)
plt.yticks(ynumbers)

plt.legend()
plt.axis([0,6.5,-1.1,1.1])
plt.show()
