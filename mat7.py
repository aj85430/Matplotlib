import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,2.0*np.pi,101)
y=np.sin(x)
z=np.sinh(x)

xnumbers=np.linspace(0,7,15)
ynumbers1=np.linspace(-1,1,11)
ynumbers2=np.linspace(0,300,7)

fig, ax1=plt.subplots()
ax2=ax1.twinx()

curve1, =ax1.plot(x,y,label='sin',color='r')
curve2, =ax2.plot(x,z,label='sinh',color='b')

plt.title("plot of sin and hyperbolic sin")
plt.show()


