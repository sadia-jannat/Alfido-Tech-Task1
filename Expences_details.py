import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#pandas data collect by csv
data = pd.read_csv('Personal_count.csv')


plt.scatter(data['Expenses'],data['Groceries'], data['House_rent'] ,data['Entertainment'])

# Adding title to the plot
plt.title("Expences Details")

# Setting the X and Y labels
plt.xlabel('Expenses')
plt.ylabel('Groceries')

plt.colorbar()


#plt.plot(df['Income'], df['Total_expense'], color='blue', linewidth=3, marker='o',  markersize=15, linestyle='--')
plt.show()