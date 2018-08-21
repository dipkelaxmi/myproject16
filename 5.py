import pandas as pd
ds=pd.read_csv('Game_medal.csv',encoding="ISO-8859-1")
ds.head()
ds.tail()
ds.describe()
ds.shape
ds.shift
ds.info
ds.NOC
ds.plot()
import matplotlib.pyplot as plt
plt.plot(ds.Edition)
plt.plot(ds.Edition,label="Year of event")
plt.legeng(loc="upperleft")
pltplot(ds.Edition,color="blue",lable="year of event")
pltplot(ds.Edition,linewidth=2.5,color="red",lable="year of event")
fig=plt.gcf()
ds.plot()
fig.savefig('my_figure.png')