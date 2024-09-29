import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 


progress_data={'Save_money':[1000,2000,2000,5000,3000],
      'Progress_rate':[3,6,6,7,4]}
df=pd.DataFrame(progress_data)

for i in range(5,6):
  Save_money= input('Enter your save money:')
  Progress_rate= input('Enter progress rate:')
  df.loc[i]=[Save_money, Progress_rate]

print(df)

#csv file
#df.to_csv("Progress.csv")


#data from csv file 
data = pd.read_csv('Progress.csv')

#bar chart create
x=data['Save_money']
y=['Save_money_1','Save_money_2','Save_money_3','Save_money_4', 'Save_money_5','Save_money_6']
positions=range(len(x))
plt.bar(positions,x)
plt.xticks(positions,y)
# Adding title to the plot
plt.title("Saving Dataset")

# Adding label on the y-axis
plt.ylabel('Total Bill')
# Adding label on the x-axis
plt.xlabel('Day')
plt.show()



# histogram of Progress_rate
plt.hist(data['Progress_rate'])
plt.title("Progress_rate")
plt.show()






