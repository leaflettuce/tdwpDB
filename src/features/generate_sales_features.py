# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 13:43:34 2018

@author: andyj
"""

import pandas as pd
import numpy as np


# import data
data_dir = '../../data/processed/sales/'
file_name = 'sales_1.0.csv'
presale_file_name = 'ps_saleS_1.0.csv'

df = pd.read_csv(data_dir + file_name)
ps = pd.read_csv(data_dir + presale_file_name)