import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
from matplotlib import style

style.use('classic')
fig=plt.figure()
ax1=fig.add_subplot(1,1,1)

def animate(i):
    print("refreshing data...")
    graph_data=open('example.txt','r').read()
    lines=graph_data.split('\n')
    xs=[]
    ys=[]
    for line in lines:
        if len(line)>1:
            x,y=line.split(',')
            xs.append(x)
            ys.append(y)
        ax1.clear()
        ax1.plot(xs,ys)

#plt.grid()
plt.title('Real-Time Traffic Graph')

ani=animation.FuncAnimation(fig,animate,interval=1000)

plt.show()


