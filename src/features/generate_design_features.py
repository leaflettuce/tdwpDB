# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 13:04:58 2018

@author: andyj
"""

import pandas as pd
import numpy as np
from generate_sales_features import add_month, add_region, add_day_of_week, states

# import data
data_dir = '../../data/processed/sales/'
file_name = 'sales_1.0.csv'
presale_file_name = 'ps_saleS_1.0.csv'

df = pd.read_csv(data_dir + file_name)
ps = pd.read_csv(data_dir + presale_file_name)

''' Generate Feature calls'''




''' Other Edits '''

# CLip Some Shit
def clipper(df):
    df['Per Head'] = np.where(df['Per Head'] < 12, df['Per Head'], 12)
    
    
# Drop unusable in prediciton
def setup_pred(df):
    pred_df = df.drop(['Zip', 'Date', 'Venue', 'Currency', 'Tax', 'Venue Adjust.',
                       'Selling Exp', 'Net Receipts', 'tour_name', 'tour_id'], axis = 1)
    
    pred_df = pred_df.rename(columns={'Attend': 'RESULT_ATTEND', 'Per Head': 'RESULT_PER_HEAD',
                                      'Gross' : 'RESULT_GROSS'})
    
    return pred_df
  

   
''' MAIN CALL '''
# Main df
add_month(df)
add_region(df, states)
add_day_of_week(df)

pred_df = setup_pred(df)


''' Organize cols '''
pred_df = pred_df[['City', 'State', 'tour_type', 'year', 'month', 'season', 'region', 
                   'day_of_week', 'Capacity', 'RESULT_ATTEND', 'RESULT_PER_HEAD', 'RESULT_GROSS']]



''' WRITE OUT TO CSV's '''
upload_dir = '../../data/processed/design/'

df.to_csv(upload_dir + 'design_2.0' + '.csv')
pred_df.to_csv(upload_dir + 'sales_3.0' + '.csv')