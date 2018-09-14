# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 16:03:37 2018

@author: andyj
"""

import pandas as pd
import xlrd
import os


# Create empty dataframe with cols we want
columns = ['date', 'venue', 'location', 'nsnm black tee', 'steelers tee',
           'plagues tee', 'long sleeve', 'snake hoodie', 'sound and fury tee', 'nsnm windbreaker',
           'lovers ladies muscle tank', 'enamel pin', 'script logo hat camo', 
           'script logo hat black', 'chicago tee', 'texas tee', 'california tee', 'day_total']
df = pd.DataFrame(columns=columns)


data_dir = '../../data/raw/daily/nsnm/'

# iterate over all files in dir and run
i = 0
for filename in os.listdir(data_dir):
    data_file = data_dir + filename
    # Grab sheet in excel file
    workbook = xlrd.open_workbook(data_file)
    sheet = workbook.sheet_by_index(0)
    i += 1
    
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
    
     # Iterate over for data and get info
    for row in range(sheet.nrows):
        cols = sheet.row_values(row)
        if row == 1:
            date = cols[0]
        if row == 2:
            venue = cols[0]
        if row == 3:
            location = cols[0]
            
        if row in range(28, 33):
            if type(cols[3]) == float:
                nsnm_black += cols[2] + cols[3] - cols[6]
            else:
                try:
                    nsnm_black += cols[2] - cols[6]
                except TypeError:
                    pass
        
        if row in range(37,  42):
            if type(cols[3]) == float:
                steelers += cols[2] + cols[3] - cols[6]
            else:
                try:
                    steelers += cols[2] - cols[6]
                except TypeError:
                    pass
        
        if row in range(46, 51):
            if type(cols[3]) == float:
                plagues += cols[2] + cols[3] - cols[6]
            else:
                try:
                    plagues += cols[2] - cols[6]
                except TypeError:
                    pass
            
        if row in range(55, 60):
            if type(cols[3]) == float:
                long_sleeve += cols[2] + cols[3] - cols[6]
            else:
                try:
                    long_sleeve += cols[2] - cols[6]
                except TypeError:
                    pass
            
        if row in range(64, 69):
            if type(cols[3]) == float:
                snake_hoodie += cols[2] + cols[3] - cols[6]
            else:
                try:
                    snake_hoodie += cols[2] - cols[6]
                except TypeError:
                    pass
        
        if row in range(73, 78):
            if type(cols[3]) == float:
                sound_and_fury += cols[2] + cols[3] - cols[6]
            else:
                try:
                    sound_and_fury += cols[2] - cols[6]
                except TypeError:
                    pass
            
        if row in range(82, 87):
            if type(cols[3]) == float:
                windbreaker += cols[2] + cols[3] - cols[6]
            else:
                try:
                    windbreaker += cols[2] - cols[6]
                except TypeError:
                    pass
        
        if row in range(91, 95):
            if type(cols[3]) == float:
                lovers += cols[2] + cols[3] - cols[6]
            else:
                try:
                    lovers += cols[2] - cols[6]
                except TypeError:
                    pass
            
        if row in range(99, 100):
            if type(cols[3]) == float:
                pin += cols[2] + cols[3] - cols[6]
            else:
                try:
                    pin += cols[2] - cols[6]
                except TypeError:
                    pass
          
        if row in range(104, 105):
            if type(cols[3]) == float:
                script_camo += cols[2] + cols[3] - cols[6]
            else:
                try:
                    script_camo += cols[2] - cols[6]
                except TypeError:
                    pass
        
        if row in range(109, 110):
            if type(cols[3]) == float:
                script_black += cols[2] + cols[3] - cols[6]
            else:
                try:
                    script_black += cols[2] - cols[6]
                except TypeError:
                    pass
        
        if row in range(114, 119):
            if type(cols[3]) == float:
                chicago += cols[2] + cols[3] - cols[6]
            else:
                try:
                    chicago += cols[2] - cols[6]
                except TypeError:
                    pass
            
        if row in range(123, 128):
            if type(cols[3]) == float:
                texas += cols[2] + cols[3] - cols[6]
            else:
                try:
                    texas += cols[2] - cols[6]
                except TypeError:
                    pass
            
        if row in range(132, 137):
            if type(cols[3]) == float:
                cali += cols[2] + cols[3] - cols[6]
            else:
                try:
                    cali += cols[2] - cols[6]
                except TypeError:
                    pass
                
    total = (nsnm_black + steelers +plagues + long_sleeve + snake_hoodie + 
             sound_and_fury + windbreaker + lovers + pin + script_camo + 
             script_black + chicago + texas + cali)
    
    '''WRITE ROW TO DF'''
    df.loc[i] = [date, venue, location, nsnm_black, steelers, plagues, long_sleeve, 
               snake_hoodie, sound_and_fury, windbreaker, lovers, pin, script_camo, 
             script_black, chicago, texas, cali, total]
    
'''WRITE DF TO CSV'''  
upload_dir = '../../data/interim/daily/'
upload_file = 'NSNM-daily'
df.to_csv(upload_dir + upload_file + '.csv')