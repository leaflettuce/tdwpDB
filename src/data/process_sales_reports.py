# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 08:53:47 2018

@author: andyj
"""

import pandas as pd
import numpy as np
import os


# import data
data_dir = '../../data/interim/sales_reports/'
ex_data_dir = '../../data/raw/extra/'

#import extraneous data files
tour_df = pd.read_csv(ex_data_dir + 'tour_details.csv')
merch_df = pd.read_csv(ex_data_dir + 'merch_details.csv', encoding = "ISO-8859-1")
beginning_test = 1

#function to find merch data
def find_merch_info():
    for term in df['search_terms'][row]:            # loop over search terms
        for merch_row in range(len(merch_df)):      # loop over rows in merch df
            if term in merch_df['name'][merch_row]: # store data if terms match
                # ADD MERCH DATA
                df['t_color'][row] = merch_df['color'][merch_row]
                df['num_print_colors'][row] = merch_df['num_print_colors'][merch_row]
                df['print_colors'][row] = merch_df['print_colors'][merch_row]
                df['lyrics'][row] = merch_df['lyrics'][merch_row]
                df['tour'][row] = merch_df['tour'][merch_row]
                df['evil'][row] = merch_df['evil'][merch_row]
                df['elite'][row] = merch_df['elite'][merch_row]
                df['logo'][row] = merch_df['logo'][merch_row]
                df['minimal'][row] = merch_df['minimal'][merch_row]
                return

# iterate over all files in dir and run
for filename in os.listdir(data_dir):
    if filename != 'the.csv':
        data_file = filename
        df = pd.read_csv(data_dir + data_file)
        
        #init merch vars
        df['t_color'] = 'na'
        df['num_print_colors'] = 'na'
        df['print_colors'] = 'na'
        df['lyrics'] = 0
        df['tour'] = 0
        df['evil'] = 0
        df['elite'] = 0
        df['logo'] = 0
        df['minimal'] = 0
        
        
        ''' ADD TOUR DETAILS'''
        # position in line up
        search_name = filename[:filename.find('.')]
        df['tour_name'] = search_name
        df['tour_type'] = tour_df[tour_df['name'] == search_name]['position'].iloc[0]
        # year
        df['year'] = tour_df[tour_df['name'] == search_name]['year'].iloc[0]
        # season
        df['season'] = tour_df[tour_df['name'] == search_name]['season'].iloc[0]
        
        df = df.drop(['Unnamed: 0'], axis = 1)
        
        
        '''ADD MERCH DETAILS'''
        df['search_terms'] = ''
        for row in range(len(df)):
            df['search_terms'][row] = df['Name'][row].lower().split(' ')[0:2]
            find_merch_info()
        
        vb
        ''' CONCAT TO FINAL DF '''        
        if beginning_test == 1:
            final_df = df
            beginning_test = 0
        else:
            final_df = pd.concat([final_df, df], ignore_index=True)
            
        final_df = final_df.drop(['search_terms'], axis =1)
        

''' WRITE OUT TO CSV '''
upload_dir = '../../data/processed/stock/'
upload_file = 'stock_1.0'
    
#write
final_df.to_csv(upload_dir + upload_file + '.csv')