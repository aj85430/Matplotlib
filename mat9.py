import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
style.use('classic')

mean=100
sd=15
N=1000
binsize=20
IQ=np.random.normal(mean,sd,N)

plt.hist(IQ,binsize,facecolor='chocolate',label='IQs',rwidth=0.8,normed=False)


plt.xlabel('IQ')
plt.ylabel('Count/Fraction')
plt.title('Histogram')
plt.grid(True)
plt.legend()
plt.show()
