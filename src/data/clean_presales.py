# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 08:41:29 2018

@author: andyj
"""
import pandas as pd
import numpy as np
import os


# import data
data_dir = '../../data/raw/extra/presale_counts/'
upload_dir = '../../data/interim/presale_counts/'

# iterate over all files in dir and run
for filename in os.listdir(data_dir):
    print(filename)
    data_file = filename
    df = pd.read_csv(data_dir + data_file, skiprows = 5, encoding = "ISO-8859-1")
    
    try:
        df = df.drop(['On Sale', 'Wrap'], axis = 1)
    except (KeyError, ValueError):
        pass
    
    if 'ten' in filename:
        df = df.drop(df.iloc[:, 3:5], axis=1)
    
    df = df.drop(df.iloc[:, 8:], axis=1)
    
    #rename cols
    df = df.rename(columns={'% Sold': 'Percent Sold'})
    
    # set types
    col_names = ['Sellable', 'Percent Sold', 'Open','Total Sold', 'Days Out']
    
    for col_name in col_names:
        try:
            df[col_name] = df[col_name].str.replace(',', '').str.replace('$', '').str.replace('%', '')
        except (AttributeError, KeyError):
            pass
        try:
            df[col_name] = pd.to_numeric(df[col_name])
        except (AttributeError, KeyError):
            pass
    
    #write out
    df.to_csv(upload_dir + filename, encoding = "utf-8", index = False)