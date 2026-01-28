# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 19:22:13 2026

@author: Admin
"""

import pandas as pd
data = {"State":["Uttar Pradesh", "Maharashtra", "Bihar", "West Bengal", "Tamil Nadu", "Karnataka", "Gujarat", "Rajasthan", "Madhya Pradesh", "Kerala"], "Votes_Lakh":[912, 590, 480, 510, 430, 390, 410, 360, 370, 280]}
df = pd.DataFrame(data)
print(df)

#Creating line plot
import matplotlib.pyplot as plt
plt.xlabel("State")
plt.ylabel("Votes(in Lakhs)")
plt.plot(["Uttar Pradesh", "Maharashtra", "Bihar", "West Bengal", "Tamil Nadu", "Karnataka", "Gujarat", "Rajasthan", "Madhya Pradesh", "Kerala"], [912, 590, 480, 510, 430, 390, 410, 360, 370, 280])

#Creating pie plot
plt.title("Vote Distribution by State")
plt.pie(df.Votes_Lakh, labels=df.State, autopct='%1.1f%%')

#Creating bar plot
plt.title("Votes(in Lakhs) by State")
plt.bar(df.State, df.Votes_Lakh)

#Creating box plot
import seaborn as sns
sns.boxplot(x=["Uttar Pradesh", "Maharashtra", "Bihar", "West Bengal", "Tamil Nadu", "Karnataka", "Gujarat", "Rajasthan", "Madhya Pradesh", "Kerala"],y=[912, 590, 480, 510, 430, 390, 410, 360, 370, 280])
