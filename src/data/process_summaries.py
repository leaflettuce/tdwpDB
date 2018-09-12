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

'''
# iterate over all files in dir and run
for filename in os.listdir(data_dir):
    data_file = filename
    df = pd.read_csv(data_dir + data_file)
    
    #iterate over presale and pull in if avail
    for ps_filename in os.listdir(presale_data_dir):
        if ps_filename == filename:
            presale_df = pd.read_csv(presale_data_dir + ps_filename)
'''
#REMOVE THESE TWO 
df = pd.read_csv(data_dir + 'nsnm.csv')
presale_df = pd.read_csv(presale_data_dir + 'nsnm.csv')
#REMOVE AT IMPLEMENTATION


