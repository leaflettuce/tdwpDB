# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 13:28:46 2018

@author: andyj
"""
import pandas as pd

# import data
data_dir = '../../data/processed/sales/'

df = pd.read_csv(data_dir + 'ps_sales_3.0.csv')
df = df.drop(['Unnamed: 0'], axis =1)

