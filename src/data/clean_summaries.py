# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 08:41:29 2018

@author: andyj
"""
import pandas as pd
import numpy as np
import os


# import data
data_dir = '../../data/raw/tour_summaries/'

# iterate over all files in dir and run
for filename in os.listdir(data_dir):
    data_file = filename
    df = pd.read_csv(data_dir + data_file, skiprows = 4)
     
    
    '''
    # FORMATING AND REMOVAL
    '''
    #remove unneccesary columnns and last 2 aggregate rows
    df = df.drop(['Exch. Rate', 'Venue Actual %', 'Bootleg Exp', 
                  'Payment Fees', 'Venue Fee', 'Vend Fee', 'Ext Exp'], axis = 1)
    df = df[:-2]
    
    
    #Set types
    col_names = ['Capacity', 'Attend', 'Per Head', 'Gross', 'Tax', 
                 'Venue Adjust.', 'Selling Exp', 'Net Receipts']
    
    for col_name in col_names:
        try:
            df[col_name] = df[col_name].str.replace(',', '').str.replace('$', '')
        except AttributeError:
            pass
        try:
            df[col_name] = pd.to_numeric(df[col_name])
        except AttributeError:
            pass
    
    '''
    # INPUT MISSING VALUES
    '''
    #replace 0's in capacity and attendance
    attend_mean = np.ceil(np.mean(df['Attend']))
    df['Capacity'] = df['Capacity'].replace(0, np.ceil(np.mean(df['Capacity'])))
    df['Attend'] = df['Attend'].replace(0, np.ceil(np.mean(df['Attend'])))
    
    for i in range(len(df)):               # Check for over cap.
        if df.iloc[i, 6] > df.iloc[i, 5]:
            df.iloc[i, 6] = df.iloc[i, 5]
        if df.iloc[i, 6] == attend_mean:   # weighted estimate for input values
            df.iloc[i, 6] = np.ceil(((attend_mean*5) + df.iloc[i, 5]) / 6)
        if df.iloc[i, 9] == 0:
            df.iloc[i, 6] = 0 
            
    #input missing per head `xvalues
    df['Per Head'] = (df['Gross'] / df['Attend']).round(2)
    
    
    '''
    # WRITE TO FILE
    '''
    upload_dir = '../../data/interim/summaries/'
    
    #Get storage name for file
    loc_start = data_file.find('_', data_file.find('_') + 1) + 1
    loc_end = data_file.find('-', loc_start + 1)
    upload_file = data_file[loc_start : loc_end]
    
    #write
    df.to_csv(upload_dir + upload_file + '.csv')