# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 17:39:52 2026

@author: Admin
"""

# Creating monthly sales trend using dataframe
import matplotlib.pyplot as plt
Months = ["Jan", "Feb", "March"]
Sales = [12000, 15000, 17000]
plt.plot(["Jan", "Feb", "March"], [12000, 15000, 17000])
plt.title("Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#Creating lineplot for monthly sales
Months = ["Jan", "Feb", "March"]
Sales = [12000, 15000, 17000]
plt.plot(Months,Sales)
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

#Creating scatter plot
import seaborn as sns
sns.scatterplot(x=[23,30,40],y=[25000,45000,80000])

#Creating boxplot
import seaborn as sns
sns.boxplot(x=['IT', 'IT', 'IT', 'HR', 'HR', 'HR'],y=[30000, 45000, 50000, 28000, 32000, 35000])

#EDA of df
df=sns.load_dataset('tips')
df.head()
df.tail()
df.describe()
df.info()
df.isnull()

Months = ['Jan', 'Feb', 'Mar']
Sales = [12000, 15000, 17000]
plt.figure()
plt.plot(Months,Sales)
plt.title("Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()

#Creating histogram
import seaborn as sns
sns.histplot([25000, 30000, 45000, 60000, 80000])

#Creating heatmap
df=pd.DataFrame({'Age':[28, 30, 40], 'Salary': [25000, 45000, 80000]})
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
