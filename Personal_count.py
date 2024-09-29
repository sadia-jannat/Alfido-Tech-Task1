import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data={'Income':[12000,15000,20000,22000,22000], 'Expenses':[1000,11000,4000,2000,500], 'Groceries':[423,87,234,500,34], 'House_rent':[1500,1500,1200,1300,1500], 
      'Entertainment':[3000,4000,865,450,200]}
df=pd.DataFrame(data)


for i in range(5,6):
    #input all
    Income1= input('Enter your income:')
    Income=int(Income1)
    Expenses= input('Enter your expenses:')
    Groceries= input('Enter your groceries:')
    House_rent= input('Enter your house rent:')
    Entertainment= input('Enter your entertainment:')

    df.loc[i]=[Income, Expenses, Groceries, House_rent, Entertainment]


print(df)

#csv file
#df.to_csv("Personal_count.csv")

# initializing the data
#x = data['total_bill']
#plt.plot(df['Income'], df['Total_expense'])

# plotting the data
plt.hist(df['Income'], bins=25, color='green', edgecolor='blue',
         linestyle='--', alpha=0.5)

# Adding title to the plot
plt.title("Income Details")

# Adding label on the y-axis
plt.ylabel('Frequency')

# Adding label on the x-axis
plt.xlabel('Total Income')

plt.show()