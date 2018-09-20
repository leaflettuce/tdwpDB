# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 13:43:34 2018

@author: andyj
"""

import pandas as pd
import numpy as np

# import data
data_dir = '../../data/processed/sales/'
file_name = 'sales_1.0.csv'
presale_file_name = 'ps_saleS_1.0.csv'

df = pd.read_csv(data_dir + file_name)
ps = pd.read_csv(data_dir + presale_file_name)


''' INITIALIZE VARS '''
# SET REGIONS - N - NE, W - West, S - South, M - Midwest, O - other
states = {
        'AK': 'O',
        'AL': 'S',
        'AR': 'S',
        'AS': 'O',
        'AZ': 'W',
        'CA': 'W',
        'CO': 'W',
        'CT': 'N',
        'DC': 'N',
        'DE': 'N',
        'FL': 'S',
        'GA': 'S',
        'GU': 'O',
        'HI': 'O',
        'IA': 'M',
        'ID': 'W',
        'IL': 'M',
        'IN': 'M',
        'KS': 'M',
        'KY': 'S',
        'LA': 'S',
        'MA': 'N',
        'MD': 'N',
        'ME': 'N',
        'MI': 'W',
        'MN': 'M',
        'MO': 'M',
        'MP': 'O',
        'MS': 'S',
        'MT': 'W',
        'NA': 'O',
        'NC': 'S',
        'ND': 'M',
        'NE': 'W',
        'NH': 'N',
        'NJ': 'N',
        'NM': 'W',
        'NV': 'W',
        'NY': 'N',
        'OH': 'M',
        'OK': 'S',
        'OR': 'W',
        'PA': 'N',
        'PR': 'O',
        'RI': 'N',
        'SC': 'S',
        'SD': 'M',
        'TN': 'S',
        'TX': 'S',
        'UT': 'W',
        'VA': 'S',
        'VI': 'O',
        'VT': 'N',
        'WA': 'W',
        'WI': 'M',
        'WV': 'S',
        'WY': 'W'
}

df = df.drop(['Unnamed: 0'], axis = 1)
ps = ps.drop(['Unnamed: 0'], axis = 1)

''' Functions For Generation '''
def add_month(df):
    ''' Add month numeric to df '''
    df['month'] = df['Date'] # CUT OFF AFTER '/'
    df['month'] = df['month'].str[2:4]
    df['month'] = pd.to_numeric(df['month'])


def add_region(df, states):
    ''' Add region variables '''
    df['region'] = ''
    
    for i, row in df.iterrows():
            for state in states:
                if row['State'] == state:
                    region = states[state]
                    df.set_value(i, 'region', region)
                    break
                else:
                    region = "C"
                    df.set_value(i, 'region', region)
                  
# day of week
def add_day_of_week(df, clip_front = True) :
    ''' Set datetime and add day of week var '''
    # 0 = monday, 6 = sunday
    if clip_front == True:
        df['Date'] = df['Date'].str[2:]
    df['Date'] = pd.to_datetime(df['Date'], format="%m/%d/%Y")
    
    df['day_of_week'] = df['Date'].dt.dayofweek


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
  
    
# PRESALE FEATURES
def presale_gen(df):
    df['days_ps_cross'] = df['Days Out'] * df['Percent Sold']
    
    
''' MAIN CALL '''
# Main df
add_month(df)
add_region(df, states)
add_day_of_week(df)
clipper(df)

pred_df = setup_pred(df)

# Presale df
add_month(ps)
add_region(ps, states)
add_day_of_week(ps)    
clipper(ps)

pred_ps = setup_pred(ps)
presale_gen(pred_ps)

pred_ps = pred_ps.drop(['City'], axis = 1)


''' Organize cols '''
pred_df = pred_df[['City', 'State', 'tour_type', 'year', 'month', 'season', 'region', 
                   'day_of_week', 'Capacity', 'RESULT_ATTEND', 'RESULT_PER_HEAD', 'RESULT_GROSS']]

pred_ps = pred_ps[['State', 'tour_type', 'year', 'month', 'season', 'region', 
                   'day_of_week', 'Capacity', 'Days Out', 'Total Sold', 'Open', 
                   'Percent Sold', 'days_ps_cross', 'RESULT_ATTEND', 'RESULT_PER_HEAD', 'RESULT_GROSS']]




''' WRITE OUT TO CSV's '''
upload_dir = '../../data/processed/sales/'

df.to_csv(upload_dir + 'sales_2.0' + '.csv')
ps.to_csv(upload_dir + 'ps_sales_2.0' + '.csv')

pred_df.to_csv(upload_dir + 'sales_3.0' + '.csv')
pred_ps.to_csv(upload_dir + 'ps_sales_3.0' + '.csv')



''' Random Stats! '''
# Precent day of
ps['percent_total_presale'] = (ps['Total Sold']/ps['Attend'])*100

# unique day of week counts
unique, counts = np.unique(df['day_of_week'], return_counts=True)
dict(zip(unique, counts))
                