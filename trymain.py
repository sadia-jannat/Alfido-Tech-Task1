import requests
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt



data={'Income':[1200,4200,7895,3456,2387],
      'House_rent':[300,400,7865,2345,1234]}
df=pd.DataFrame(data)

income= input('Enter your income:')
rent= input('Enter your house rent:')

#loop for 1
for i in range(2,4):
    df.loc[i]=[income,rent]
print(df)

#loop for 2 (int create after)
intincome=int(income)
intrent=int(rent)

for i in range(2,4):
    df.loc[i]=[intincome,intrent]
print(df)

#df.loc[3]=[income,rent]
#print(df) 

#div_x=[df.loc[1]]
y=df.values
print("it is=",y)

#div_y=[df.loc[2]]
#plt.plot(div_x, div_y)
#plt.show()
#print(div_x)
x=df.loc[3]
x.values
print(x)

#plt.bar(df['Income'], df['House_rent'])
#plt.scatter(df['Income'], df['House_rent'])
plt.scatter(df['Income'], df['House_rent'])
 
plt.title("scatter Chart")

plt.xlabel('Income')
plt.ylabel('House_rent')
 
plt.show()