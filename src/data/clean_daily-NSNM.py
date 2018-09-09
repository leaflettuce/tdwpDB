# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 16:03:37 2018

@author: andyj
"""

import pandas as pd
import xlrd
import os


# Create empty dataframe with cols we want
columns = ['date', 'venue', 'city', 'state', 'country', 'nsnm black tee', 'steelers tee',
           'plagues tee', 'long sleeve', 'snake hoodie', 'sound and fury tee', 'nsnm windbreaker',
           'lovers ladies muscle tank', 'enamel pin', 'script logo hat camo', 
           'script logo hat black', 'chicago tee', 'texas tee', 'california tee']
df = pd.DataFrame(columns=columns)

data_dir = '../../data/raw/daily/nsnm/'
# iterate over all files in dir and run
for filename in os.listdir(data_dir):
    data_file = data_dir + filename
    # Grab sheet in excel file
    workbook = xlrd.open_workbook(data_file)
    sheet = workbook.sheet_by_index(0)
    
    #initialize vars for data storage
    nsnm_black = 0
    steelers = 0
    plagues = 0
    long_sleeve = 0
    snake_hoodie = 0
    sound_and_fury = 0
    windbreaker = 0
    lovers = 0
    pin = 0
    script_camo = 0
    script_black = 0
    chicago = 0
    texas = 0
    cali = 0
    
     # Iterate over for data
    for row in range(sheet.nrows):
        cols = sheet.row_values(row)
        if row == 1:
            date = cols[0]
        if row == 2:
            venue = cols[0]
        if row == 3:
            ''' DO MATH FOR THESE V'''
            city = cols[0]
            state = cols[0]
            country = cols[0]
            ''' DO MATH FOR THOSE ^'''
            
        if row in [28, 29, 30, 31, 32]:
            try:
                nsnm_black += cols[2] - cols[6]
            except TypeError:
                pass
        
        if row in [37, 38, 39, 40, 41]:
            try:
                steelers += cols[2] - cols[6]
            except TypeError:
                pass
        
        if row in [46, 47, 48, 49, 50]:
            try:
                plagues += cols[2] - cols[6]
            except TypeError:
                pass
            
        if row in [55, 56, 57, 58, 59]:
            try:
                long_sleeve += cols[2] - cols[6]
            except TypeError:
                pass
            
        ''' DO REMAINING'''
        
    ''' WRITE ROW TO DF'''
        
'''WRITE DF TO CSV'''  