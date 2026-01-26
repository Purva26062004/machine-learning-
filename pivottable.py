# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 20:49:22 2026

@author: Admin
"""
import pandas as pd
import numpy as np
df = pd.read_csv(r"C:\Users\Admin\anaconda3\Lib\site-packages\pandas\io\Employee_Details.csv")
print(df)
pivot = pd.pivot_table(df,index="EMP_DEPARTMENT", values="EMP_SALARY", aggfunc=['count','sum','mean'])
print(pivot)
print("\nMinimum paying department:")
print(pivot.idxmin())
