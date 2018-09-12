# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 07:54:01 2018

@author: andyj
"""

import pandas as pd
import xlrd
import os


# Create empty dataframe with cols we want
columns = ['date', 'venue', 'location', 'one_after', 'praise_poison',
           'reptar', 'hoodie', 'hat', 'back_pack', 'day_total']
df = pd.DataFrame(columns=columns)


data_dir = '../../data/raw/daily/pwd/'

# iterate over all files in dir and run
i = 0
for filename in os.listdir(data_dir):
    data_file = data_dir + filename
    # Grab sheet in excel file
    workbook = xlrd.open_workbook(data_file)
    sheet = workbook.sheet_by_index(0)
    i += 1
    
    #initialize vars for data storage
    one_after = 0
    praise = 0
    reptar = 0
    hoodie = 0
    hat = 0
    back_pack = 0
    
    
     # Iterate over for data and get info
    for row in range(sheet.nrows):
        cols = sheet.row_values(row)
        if row == 1:
            date = cols[0]
        if row == 2:
            venue = cols[0]
        if row == 3:
            location = cols[0]
            
        if row in range(8, 13):
            if type(cols[3]) == float:
                one_after += cols[2] + cols[3] - cols[6]
            else:
                try:
                    one_after += cols[2] - cols[6]
                except TypeError:
                    pass
        
        if row in range(17,  22):
            if type(cols[3]) == float:
                praise += cols[2] + cols[3] - cols[6]
            else:
                try:
                    praise += cols[2] - cols[6]
                except TypeError:
                    pass
        
        if row in range(26, 31):
            if type(cols[3]) == float:
                reptar += cols[2] + cols[3] - cols[6]
            else:
                try:
                    reptar += cols[2] - cols[6]
                except TypeError:
                    pass
        
        if row in range(35, 40):
            if type(cols[3]) == float:
                hoodie += cols[2] + cols[3] - cols[6]
            else:
                try:
                    hoodie += cols[2] - cols[6]
                except TypeError:
                    pass
            
        if row in range(44, 45):
            if type(cols[3]) == float:
                hat += cols[2] + cols[3] - cols[6]
            else:
                try:
                    hat += cols[2] - cols[6]
                except TypeError:
                    pass
            
        if row in range(49, 50):
            if type(cols[3]) == float:
                back_pack += cols[2] + cols[3] - cols[6]
            else:
                try:
                    back_pack += cols[2] - cols[6]
                except TypeError:
                    pass
            
            
    total = (one_after + praise + reptar + hoodie + hat + back_pack)
    
    '''WRITE ROW TO DF'''
    df.loc[i] = [date, venue, location, one_after, praise, reptar, hoodie, hat,
          back_pack, total]
    
'''WRITE DF TO CSV'''  
upload_dir = '../../data/interim/daily/'
upload_file = 'pwd-daily'
df.to_csv(upload_dir + upload_file + '.csv')