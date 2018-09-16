# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 08:16:44 2018

@author: andyj
"""

import pandas as pd
import numpy as np
import os


# import data
data_dir = '../../data/interim/summaries/'
ex_data_dir = '../../data/raw/extra/'
presale_data_dir = '../../data/interim/presale_counts/'

#import extraneous data files
tour_df = pd.read_csv(ex_data_dir + 'tour_details.csv')

beginning_test = 1
presale_beginning_test = 1

# iterate over all files in dir and run
for filename in os.listdir(data_dir):
    print(filename)
    data_file = filename
    df = pd.read_csv(data_dir + data_file)
    
    '''
    #REMOVE THESE TWO 
    filename = 'NSNM.csv'
    ps_filename = 'NSNM.csv'
    df = pd.read_csv(data_dir + 'NSNM.csv')
    presale_df = pd.read_csv(presale_data_dir + 'NSNM.csv')
    #REMOVE AT IMPLEMENTATION
    '''

    ''' ADD TOUR DETAILS'''
    # position in line up
    search_name = filename[:filename.find('.')]
    df['tour_name'] = search_name
    df['tour_type'] = tour_df[tour_df['name'] == search_name]['position'].iloc[0]
    # year
    df['year'] = tour_df[tour_df['name'] == search_name]['year'].iloc[0]
    # season
    df['season'] = tour_df[tour_df['name'] == search_name]['season'].iloc[0]
    df['tour_id'] = tour_df[tour_df['name'] == search_name]['id'].iloc[0]
    
    ''' toss in presale'''
    #iterate over presale and pull in if avail
    for ps_filename in os.listdir(presale_data_dir):
        if ps_filename == filename:
            presale_df = pd.read_csv(presale_data_dir + ps_filename)
            presale_df['city'] = 'void'
    
        if ps_filename == filename:
            print(filename)
            # set city column
            for i in range(len(presale_df)):
                presale_df['city'].iloc[i] = presale_df['City/State'].iloc[i][:presale_df['City/State'].iloc[i].find(',')]
            
            # drop unnecessary
            presale_df = presale_df.drop(['City/State', 'Date', 'Venue'], axis = 1)
            # merge two df's
            new_presale_df = pd.merge(df, presale_df,  how='left', left_on=['City'], right_on = ['city'], 
                              right_index = False)
            new_presale_df = new_presale_df.drop(['city'], axis = 1)
            new_presale_df = new_presale_df.drop(['Unnamed: 0'], axis = 1)
    
            new_presale_df = new_presale_df.fillna(np.ceil(new_presale_df.mean()))
            
            if presale_beginning_test == 1:
                final_presale_df = new_presale_df
                presale_beginning_test = 0
            else:
                final_presale_df = pd.concat([final_presale_df, new_presale_df], ignore_index=True)
                
                final_presale_df = final_presale_df.drop(['Wrap', 'Cap.', 'Unsold', 'Sellable'], axis = 1)
                final_presale_df['Days Out'] = final_presale_df['Days Out'].fillna(1)
                final_presale_df['Open'] = final_presale_df['Open'].fillna(final_presale_df['Capacity'] - final_presale_df['Total Sold'])
        
    new_df = df
    new_df = new_df.drop(['Unnamed: 0'], axis = 1)
    
    
    ''' fill na's '''
    new_df = new_df.fillna(np.ceil(new_df.mean()))
    
    if beginning_test == 1:
        final_df = new_df
        beginning_test = 0
    else:
        final_df = pd.concat([final_df, new_df], ignore_index=True)

final_df = final_df[final_df['Date'] != 'TOTAL']

# WRITE OUT
upload_dir = '../../data/processed/sales/'
upload_file = 'sales_1.0'
upload_ps_file = 'ps_sales_1.0'
    
#write
final_df.to_csv(upload_dir + upload_file + '.csv')
final_presale_df.to_csv(upload_dir + upload_ps_file + '.csv')