# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
 
 
# reading the database
data = pd.read_csv("Personal_count.csv")
 
# using only data attribute
sns.lineplot(data=data.drop(['Entertainment'], axis=1))
plt.show()


#using income, house rent, groceries
sns.barplot(x='House_rent',y='Income', data=data, 
            hue='Groceries')
 
plt.show()


#using income and total expences
data2 = pd.read_csv("Personal_details.csv")
sns.histplot(x='Total_expense', data=data2, kde=True, hue='Income')
 
plt.show()


##  need  pip install seaborn