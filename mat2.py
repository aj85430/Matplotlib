import matplotlib.pyplot as plt

population_ages=[22,55,62,45,21,22,24,42,4,99,102,105,121,123,111,110,5,99,3,17,33,44,56]
bins=[0,10,20,30,40,50,60,70,80,90,100,110,120,130]

#plt.hist(population_ages,bins,histtype='bar',rwidth=0.4,color='r')
#x=[1,2,3,4,6,7,8]
#y=[2,3,3,7,9,0,3]
#plt.scatter(x,y,label='skitscat',color='k',marker='*',s=100)
days=[1,2,3,4,5]
sleeping=[7,8,6,11,7]
eating=[2,3,4,3,2]
working=[7,8,7,2,2]
slices=[7,4,3,6]
activities=['sleeping','eating','working','playing']
colors=['k','r','k','k']

plt.pie(slices,labels=activities,colors=colors,startangle=90,shadow=True,explode=(0,0.1,0,0))

#plt.plot([],[],color='m',label='sleeping',linewidth=5)
#plt.plot([],[],color='c',label='working',linewidth=5)
#plt.plot([],[],color='r',label='working',linewidth=5)
#plt.plot([],[],color='k',label='playing',linewidth=5)

#plt.stackplot(days,sleeping,eating,working,playing,colors=['m','c','r','k'])

plt.xlabel('x')
plt.ylabel('y')
plt.title('interesting graph')
#plt.legend()
plt.show()
