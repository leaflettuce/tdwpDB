# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 10:32:19 2018

@author: andyj
"""

import pandas as pd
import numpy as np

# import data
data_dir = '../../data/processed/sales/'
df = pd.read_csv(data_dir + 'sales_3.0.csv')

df = df.drop(['id'], axis =1)

# set train, test, and validation

X = df.iloc[:,0:8]
Y_attend = df['RESULT_ATTEND']
Y_gross = df['RESULT_GROSS']