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


# month numeric
df['month'] = df['Date'] # CUT OFF AFTER '/'
ps['month'] = ps['Date'] # CUT OFF AFTER '/'

# regions
df['region'] = ''
ps['region'] = ''

region_dict = {
        'W' : [],
        'S' : [],
        'NW' : [],
        'NE' : []
        }

for row in len(df):
    for key, value in region_dict.values():
        for state in value:
            if state == row.iloc[3]:
                row.iloc[22] == key
                
# day of week
        ''' DO THIS '''
        

''' PRESALE FEATURES '''
# Precent day of
ps['percent_total_presale'] = (ps['Total Sold']/ps['Attend'])*100
                