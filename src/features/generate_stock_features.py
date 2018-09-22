# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 13:51:12 2018

@author: andyj
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 13:04:58 2018

@author: andyj
"""

import pandas as pd

# import data
data_dir = '../../data/processed/stock/'
file_name = 'stock_1.0.csv'

df = pd.read_csv(data_dir + file_name)


''' Generate Feature calls'''
df = df.rename(columns = {'$ % of Total' : 'Percent_Design', 'Precent of Total': 'Percent Tour'})

''' Other Edits '''

# Drop unusable in prediciton
def setup_pred(df):
    pred_df = df.drop(['Unnamed: 0', 'Unit % of Total', 'tour_id' , 'merch_id'], axis = 1)
    
    return pred_df


''' Get Analytical FORMAT '''
pred_df = setup_pred(df)

# ORganize Cols
pred_df = pred_df[['Name', 'Type', 'Sex', 'Size', 't_color', 'num_print_colors', 
                   'print_colors', 'logo', 'tour', 'elite' ,'evil' ,'lyrics', 'minimal',
                   'tour_name', 'tour_type', 'year', 'season','Avg. Price', 'Comp', 
                    'Percent_Design', 'Percent Tour', 'Sold', 'Gross Rev']]


''' WRITE OUT TO CSV's '''
upload_dir = '../../data/processed/stock/'

df.index.name = 'id'
pred_df.index.name = 'id'

df.to_csv(upload_dir + 'stock_2.0' + '.csv')
pred_df.to_csv(upload_dir + 'stock_3.0' + '.csv')