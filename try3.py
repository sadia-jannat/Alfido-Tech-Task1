import requests
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt


#income= input('Enter your income:')
#expenses= input('Enter your expenses:')
#groceries= input('Enter your groceries:')
#rent= input('Enter your house rent:')
#entertainment= input('Enter your entertainment:')
#df=pd.DataFrame(columns=thlist)
data={'Income':[5,8,9],
      'House_rent':[3,4,5]}
df=pd.DataFrame(data)
print(df)    #SEE data

expenses=[6,8,9]   #new colum add
df['expenses']=expenses
print(df)


###df.add({'Income':6, 'House_rent':45, 'expenses':56 }) not work
df.loc[5]=[64,86,90] #new row add
print(df)

incomedic=[1,7]
#incomedic.append(int(income))
