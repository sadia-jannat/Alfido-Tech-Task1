import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#pandas data collect
data={'Income':[12000,15000,20000,22000,22000],
      'Total_expense':[3000,4000,8658,21450,20000]}
df=pd.DataFrame(data)

# plotting the data
#plt.bar(df['Income'], df['Total_expense'])
x=[10,20,30,40]
y=['t1','t2','t3','t4']
positions=range(len(x))
plt.bar(positions,x)
plt.xticks(positions,y)


# Adding title to the plot
plt.title("Tips Dataset")

# Adding label on the y-axis
plt.ylabel('Total Bill')

# Adding label on the x-axis
plt.xlabel('Day')

plt.show()