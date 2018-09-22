# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 13:04:58 2018

@author: andyj
"""

import pandas as pd
import numpy as np
from generate_sales_features import add_region, add_day_of_week, states

# import data
data_dir = '../../data/processed/design/'
file_name = 'design_1.0.csv'

df = pd.read_csv(data_dir + file_name)


''' minor cleanup '''
df['num_print_colors'] = np.where(df['num_print_colors']=='na', 0, df['num_print_colors'])
df = df[df['name'] != 'day_total']

''' Generate Feature calls'''
# MONTH
df = df.rename(columns={'date': 'Date'})
df['month'] = df['Date'] # CUT OFF AFTER '/'
df['month'] = df['month'].str[0:2]
df['month'] = pd.to_numeric(df['month'])
    
# STATE & City
df['State'] = df['location']
df['city'] = df['location']

df['tmp'] = df['State'].str.find(',')

for i, row in df.iterrows():
    df.at[i, 'State'] = df.at[i, 'State'][df['tmp'][i] + 2: df['tmp'][i] + 4]
    df.at[i, 'city'] = df.at[i, 'city'][:df['tmp'][i]]
df = df.drop(['tmp'], axis = 1)
    
# REGION
add_region(df, states)

#DAY OF WEEK
add_day_of_week(df, clip_front = False)


''' Other Edits '''
# Drop unusable in prediciton
def setup_pred(df):
    pred_df = df.drop(['Unnamed: 0', 'Date', 'location', 'merch_id', 'tour_id'], axis = 1)
    
    pred_df = pred_df.rename(columns={'value': 'RESULT_VALUE'})
    
    return pred_df


''' Get Analytical FORMAT '''
pred_df = setup_pred(df)

# ORganize Cols
pred_df = pred_df[['name', 'tour_name', 'tour_type', 'venue', 'State', 'city', 'region',
                   'year', 'month', 'day_of_week', 'season', 't_color', 'num_print_colors',
                   'print_colors', 'logo', 'tour', 'elite' ,'evil' ,'lyrics', 'minimal', 'RESULT_VALUE']]


''' WRITE OUT TO CSV's '''
upload_dir = '../../data/processed/design/'

df.index.name = 'id'
pred_df.index.name = 'id'

df.to_csv(upload_dir + 'design_2.0' + '.csv')
pred_df.to_csv(upload_dir + 'design_3.0' + '.csv')