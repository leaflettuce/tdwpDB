# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 16:10:08 2018

@author: andyj
"""
import pandas as pd

# - IMPORT SALES and PRESALES prediction csv's
presales = pd.read_csv('../../data/predictions/leg2_presale.csv')
sales = pd.read_csv('../../data/predictions/leg2_sale.csv')

# - Average out together w/ past predictions per show
df = pd.concat([presales, sales], axis = 1, sort = False)
df.columns = ['presales', 'sales']

df['average'] = (df['presales'] + df['sales']) / 2

# - Report back final predicted
df['average'].to_csv('../../data/predictions/leg2_final_predictions.csv')