#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 13:44:02 2025

@author: bhupatejassingh
"""

#import pandas as pd
import numpy as np
import seaborn as sns


x=sns.load_dataset('iris')
x.drop(columns='species', inplace=True)

df=x.head(11)
df=df.copy()

df['aloo']=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

['anrog', np.nan, 'ejgwn', 'aegnrib', 'ged', 'bsafi', 'tj' ,'a', 'aafs', 'rsrb', 'reaf']

df.aggregate(['max', 'min', 'count', 'std', 'var'], axis=0)

df.sort_values(by='sepal_length')

df.groupby('sepal_length').max()


print(df.aggregate(['max', 'min', 'count', 'std', 'var'], axis=0))

df1 = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])
df2 = df.reindex([5, 8, 1, 9, 0, 2, 3, 6, 4, 7, 10])

df3 = df.reindex(columns = ['d', 'j', 'w', 'y'])
df4 = df.reindex(columns = ['sepal_width', 'petal_width', 'sepal_length', 'aloo'])

y = df.rename(columns={'sepal_length':0})
#df.rename(columns={'sepal_length':0}, inplace=True)

#df.set_index('columns')

z = df.rename(index={0:'something_aloo'})
#df.rename(index={0:'something_aloo'}, inplace=True)





