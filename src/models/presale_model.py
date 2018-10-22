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

# drop all categorical but tour_type -> considered in sales model
df = df.drop(['State', 'year', 'month', 'season', 'region', 'day_of_week', 
              'RESULT_PER_HEAD', 'RESULT_ATTEND', 'Open'], axis = 1)

df = df.drop([4])

df['Total Sold'] = (df['Percent Sold']/100)*df['Capacity']