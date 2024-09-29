import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#input all
#Income= input('Enter your income:')
Expenses= input('Enter your expenses:')
Groceries= input('Enter your groceries:')
House_rent= input('Enter your house rent:')
Entertainment= input('Enter your entertainment:')

#int convert
x=int(Expenses)
y=int(Groceries)
z=int(House_rent)
w=int(Entertainment)
Total_expense=(x+y+z+w)
print("Total expenses= ")
print(Total_expense)

#pandas data collect
data={'Income':[12000,15000,20000,22000,22000],
      'Total_expense':[3000,4000,8658,21450,20000]}
df=pd.DataFrame(data)


#loop for 4 time input your income and total expense
for i in range(5,8):
    Income= input('Enter your previous/present month income:')
    Total_expense= input('Enter your previous/present month total expences:')
    df.loc[i]=[Income, Total_expense]
    
print(df)    



#csv file
#df.to_csv("Personal_details.csv")

#last matplotlip graph
plt.plot(df['Income'], df['Total_expense'])
plt.title("Income and Total expenses")
plt.xlabel('Income')
plt.ylabel('Total expenses')
 
plt.show()


