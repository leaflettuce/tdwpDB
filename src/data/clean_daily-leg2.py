# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 07:54:01 2018

@author: andyj
"""

import pandas as pd
import xlrd
import os


# Create empty dataframe with cols we want
columns = ['date', 'venue', 'location', 'chain', 'tour',
           'handshake', 'nurse_jogger', 'skull', 'stampede_windbreaker', 
            'wraabb_zipup', 'wall_flag', 'pullover', 'patagonia', 'back_pack', 'day_total']
df = pd.DataFrame(columns=columns)


data_dir = '../../data/raw/daily/leg2/'

# iterate over all files in dir and run
i = 0
for filename in os.listdir(data_dir):
    data_file = data_dir + filename
    # Grab sheet in excel file
    workbook = xlrd.open_workbook(data_file)
    sheet = workbook.sheet_by_index(0)
    i += 1
    
    #initialize vars for data storage
    chain = 0
    tour = 0
    handshake = 0
    nurse_jogger = 0
    skull = 0
    stampede_windbreaker = 0
    wraabb_zipup = 0
    wall_flag = 0
    pullover = 0
    patagonia = 0
    back_pack = 0
    
    
     # Iterate over for data and get info
    for row in range(sheet.nrows):
        cols = sheet.row_values(row)
        #print(cols)
    #break
        if row == 1:
            date = cols[0]
        if row == 2:
            venue = cols[0]
        if row == 3:
            location = cols[0]
            
        if row in range(8, 13):
            if type(cols[3]) == float:
                chain += cols[2] + cols[3] - cols[6]
            else:
                try:
                    chain += cols[2] - cols[6]
                except TypeError:
                    pass
        
        if row in range(17,  22):
            if type(cols[3]) == float:
                tour += cols[2] + cols[3] - cols[6]
            else:
                try:
                    tour += cols[2] - cols[6]
                except TypeError:
                    pass
        
        if row in range(26, 31):
            if type(cols[3]) == float:
                handshake += cols[2] + cols[3] - cols[6]
            else:
                try:
                    handshake += cols[2] - cols[6]
                except TypeError:
                    pass
        
        if row in range(35, 40):
            if type(cols[3]) == float:
                nurse_jogger += cols[2] + cols[3] - cols[6]
            else:
                try:
                    nurse_jogger += cols[2] - cols[6]
                except TypeError:
                    pass
            
        if row in range(44, 49):
            if type(cols[3]) == float:
                skull += cols[2] + cols[3] - cols[6]
            else:
                try:
                    skull += cols[2] - cols[6]
                except TypeError:
                    pass
            
        if row in range(53, 58):
            if type(cols[3]) == float:
                stampede_windbreaker += cols[2] + cols[3] - cols[6]
            else:
                try:
                    stampede_windbreaker += cols[2] - cols[6]
                except TypeError:
                    pass
                
        if row in range(62, 67):
            if type(cols[3]) == float:
                wraabb_zipup += cols[2] + cols[3] - cols[6]
            else:
                try:
                    wraabb_zipup += cols[2] - cols[6]
                except TypeError:
                    pass
       
        if row in range(71, 72):
            if type(cols[3]) == float:
                wall_flag += cols[2] + cols[3] - cols[6]
            else:
                try:
                    wall_flag += cols[2] - cols[6]
                except TypeError:
                    pass
                
        if row in range(76, 81):
            if type(cols[3]) == float:
                wall_flag += cols[2] + cols[3] - cols[6]
            else:
                try:
                    wall_flag += cols[2] - cols[6]
                except TypeError:
                    pass
        
        if row in range(85, 90):
            if type(cols[3]) == float:
                pullover += cols[2] + cols[3] - cols[6]
            else:
                try:
                    pullover += cols[2] - cols[6]
                except TypeError:
                    pass
                
        if row in range(94, 99):
            if type(cols[3]) == float:
                patagonia += cols[2] + cols[3] - cols[6]
            else:
                try:
                    patagonia += cols[2] - cols[6]
                except TypeError:
                    pass
                
        if row in range(103, 104):
            if type(cols[3]) == float:
                back_pack += cols[2] + cols[3] - cols[6]
            else:
                try:
                    back_pack += cols[2] - cols[6]
                except TypeError:
                    pass
            
    total = (chain + tour + handshake + nurse_jogger + skull + stampede_windbreaker + 
              wraabb_zipup + wall_flag + pullover + patagonia + back_pack)
      
    '''WRITE ROW TO DF'''
    df.loc[i] = [date, venue, location, chain, tour, handshake, 
                  nurse_jogger, skull, stampede_windbreaker, 
             wraabb_zipup, wall_flag, pullover, patagonia, back_pack, total]
    
'''WRITE DF TO CSV'''  
upload_dir = '../../data/interim/daily/'
upload_file = 'leg2-daily'
df.to_csv(upload_dir + upload_file + '.csv', encoding='utf8')