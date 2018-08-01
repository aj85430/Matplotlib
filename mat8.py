import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
style.use('seaborn')
x=np.linspace(0,2.0*np.pi,101)
y=np.sin(x)
z=np.cos(x)


plt.plot(x,y,'r',label='sin')
plt.plot(x,z,'g',label='cos')
plt.xlabel('angle in radians')
plt.ylabel('magnitude')
plt.title('trigonometric function')
plt.grid(True)

plt.legend()
plt.show()
