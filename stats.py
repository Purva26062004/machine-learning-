# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 20:10:01 2026

@author: Admin
"""

import pandas as pd
data = pd.read_csv("C:\\Users\\Admin\\anaconda3\\Lib\\site-packages\\pandas\\io\\t20_matches.csv")
print(data)

#Calculate variance
print("Variance:\n", data.var(numeric_only=True))

#Calcuate Standard Deviation
print("\n Standard Deviation:\n", data.std(numeric_only=True))

#Calculate Chi-Square
import scipy.stats as stats
for col in data.select_dtypes(include='number'): chi, p = stats.chisquare(data[col].value_counts())
print(col, chi, p)

#Calculate t-test
from scipy.stats import ttest_ind
num_cols = data.select_dtypes(include='number').columns
t_stat, p_value = ttest_ind(data[num_cols[0]].dropna(),data[num_cols[1]].dropna())
print("t-statistic:", t_stat)
print("p-value:", p_value)

#Calculate z-test
import numpy as np
c = data.select_dtypes(include='number').columns
x, y = data[c[0]], data[c[1]].dropna()
z = (x.mean() - y.mean()) / np.sqrt(x.var()/len(x) + y.var()/len(y))
p = 2 * (1 - stats.norm.cdf(abs(z)))
print(z, p)

#Calculate anova
c = data.select_dtypes(include='number').columns
g = [data[col].dropna() for col in np.random.choice(c, 3, replace=False)]
print(*stats.f_oneway(*g))

#Calculate F-test
c = data.select_dtypes(include='number').columns
x, y = data[c[0]].dropna(), data[c[1]].dropna()
f = x.var(ddof=1) / y.var(ddof=1)
p = 2 * min(stats.f.cdf(f, len(x)-1, len(y)-1), 1 - stats.f.cdf(f, len(x)-1, len(y)-1))
print(f, p)
