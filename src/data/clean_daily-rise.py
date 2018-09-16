# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 07:17:34 2018

@author: andyj
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 16:03:37 2018

@author: andyj
"""

import pandas as pd
import xlrd
import os


# Create empty dataframe with cols we want
columns = ['date', 'venue', 'location', 'lost', 'native', 'oni_mask', 'transit_blues', 
          'tattoo', 'cult_long', 'oni_mask_hoodie', 'cafe_racer',  'candle', 'arch_snap', 
          'pennant_flag', 'candle_flag', 'wristband', 'day_total']
df = pd.DataFrame(columns=columns)


data_dir = '../../data/raw/daily/rise/'

# iterate over all files in dir and run
i = 0
for filename in os.listdir(data_dir):
    data_file = data_dir + filename
    # Grab sheet in excel file
    workbook = xlrd.open_workbook(data_file)
    sheet = workbook.sheet_by_index(0)
    i += 1
    
    #initialize vars for data storage
    lost = 0
    native = 0
    oni_mask = 0
    transit_blues = 0
    tattoo = 0
    cult_long = 0
    oni_mask_hoodie = 0
    cafe_racer = 0
    candle = 0
    arch_snap = 0
    pennant_flag = 0
    candle_flag = 0
    wristband = 0
    
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
                lost += cols[2] + cols[3] - cols[6]
            else:
                try:
                    lost += cols[2] - cols[6]
                except TypeError:
                    pass
        
        if row in range(22,  27):
            if type(cols[3]) == float:
                native += cols[2] + cols[3] - cols[6]
            else:
                try:
                    native += cols[2] - cols[6]
                except TypeError:
                    pass
        
        if row in range(31, 36):
            if type(cols[3]) == float:
                oni_mask += cols[2] + cols[3] - cols[6]
            else:
                try:
                    oni_mask += cols[2] - cols[6]
                except TypeError:
                    pass
            
        if row in range(40, 45):
            if type(cols[3]) == float:
                transit_blues += cols[2] + cols[3] - cols[6]
            else:
                try:
                    transit_blues += cols[2] - cols[6]
                except TypeError:
                    pass
            
        if row in range(49, 54):
            if type(cols[3]) == float:
                tattoo += cols[2] + cols[3] - cols[6]
            else:
                try:
                    tattoo += cols[2] - cols[6]
                except TypeError:
                    pass
        
        if row in range(58, 63):
            if type(cols[3]) == float:
                cult_long += cols[2] + cols[3] - cols[6]
            else:
                try:
                    cult_long += cols[2] - cols[6]
                except TypeError:
                    pass
            
        if row in range(67, 72):
            if type(cols[3]) == float:
                oni_mask_hoodie += cols[2] + cols[3] - cols[6]
            else:
                try:
                    oni_mask_hoodie += cols[2] - cols[6]
                except TypeError:
                    pass
        
        if row in range(76, 81):
            if type(cols[3]) == float:
                cafe_racer += cols[2] + cols[3] - cols[6]
            else:
                try:
                    cafe_racer += cols[2] - cols[6]
                except TypeError:
                    pass
            
        if row in range(85, 90):
            if type(cols[3]) == float:
                candle += cols[2] + cols[3] - cols[6]
            else:
                try:
                    candle += cols[2] - cols[6]
                except TypeError:
                    pass
          
        if row in range(94, 95):
            if type(cols[3]) == float:
                arch_snap += cols[2] + cols[3] - cols[6]
            else:
                try:
                    arch_snap += cols[2] - cols[6]
                except TypeError:
                    pass
        
        if row in range(99, 100):
            if type(cols[3]) == float:
                pennant_flag += cols[2] + cols[3] - cols[6]
            else:
                try:
                    pennant_flag += cols[2] - cols[6]
                except TypeError:
                    pass
        
        if row in range(104, 105):
            if type(cols[3]) == float:
                candle_flag += cols[2] + cols[3] - cols[6]
            else:
                try:
                    candle_flag += cols[2] - cols[6]
                except TypeError:
                    pass
            
        if row in range(109, 110):
            if type(cols[3]) == float:
                wristband += cols[2] + cols[3] - cols[6]
            else:
                try:
                    wristband += cols[2] - cols[6]
                except TypeError:
                    pass
            
    total = (lost + native + oni_mask + transit_blues + tattoo + cult_long + 
    oni_mask_hoodie + cafe_racer +  candle + arch_snap + pennant_flag + 
    candle_flag + wristband)
    
    '''WRITE ROW TO DF'''
    df.loc[i] = [date, venue, location, lost, native, oni_mask, transit_blues, 
          tattoo, cult_long, oni_mask_hoodie, cafe_racer,  candle, arch_snap, 
          pennant_flag, candle_flag, wristband, total]
    
'''WRITE DF TO CSV'''  
upload_dir = '../../data/interim/daily/'
upload_file = 'rise-daily'
df.to_csv(upload_dir + upload_file + '.csv')