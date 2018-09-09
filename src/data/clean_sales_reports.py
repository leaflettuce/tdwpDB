# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 14:26:43 2018

@author: andyj
"""

import pandas as pd
import numpy as np
import os


# import data
data_dir = '../../data/raw/sales_reports/'

# iterate over all files in dir and run

for filename in os.listdir(data_dir):
    data_file = filename

    df = pd.read_csv(data_dir + data_file, skiprows = 1)
    
    
    '''
    # FORMATING AND REMOVAL
    '''
    df_tees = df[(df['SKU'] == '        ""')]
    df_other = df[(df['SKU'] == '    ""')] 
    df = pd.concat([df_tees, df_other])
    df = df.drop(['SKU'], axis = 1)
    
    '''
    # MISSING VALUES
    '''
    df['Sex'] = df['Sex'].fillna('U')
    df['Size'] = df['Size'].fillna('One-Size')
    
    
    '''
    # SET TYPES
    '''
    col_names = ['Sold', 'Unit % of Total', 'Comp', 'Avg. Price', 'Gross Rev', 
                     '$ % of Total']
        
    for col_name in col_names:
       try:
           df[col_name] = df[col_name].str.replace(',', '').str.replace('$', '').str.replace('%', '')
       except AttributeError:
           pass
       try:
           df[col_name] = pd.to_numeric(df[col_name])
       except AttributeError:
           pass
       
    
    # RENAME STUPID NAMED COLS
    df = df.rename({'Unit % of Total':'Percent by Type', 'Avg. Price':'Avg Price', '$ % of Total':'Percent of Total'}, axis=1)
    
    #percent of total
    df['Precent of Total'] = ((df['Gross Rev'] / df['Gross Rev'].sum()) *100).round(2)
    
    
    '''
    # WRITE TO FILE
    '''
    upload_dir = '../../data/interim/sales_reports/'
    
    #Get storage name for file
    loc_start = data_file.find('_', data_file.find('_') + 1) + 1
    loc_end = data_file.find('-', loc_start + 1)
    upload_file = data_file[loc_start : loc_end]
    
    #write
    df.to_csv(upload_dir + upload_file + '.csv')