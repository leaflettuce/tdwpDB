# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 10:32:19 2018

@author: andyj
"""

import pandas as pd
import numpy as np

from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from collections import defaultdict

# import data
data_dir = '../../data/processed/sales/'

df = pd.read_csv(data_dir + 'sales_3.0.csv')
df = df.drop(['id'], axis =1)


######################################
# CLEAN AND ORGANIZE VARIABLES #######
######################################
 
# Make dummies
df_cont = df.loc[:,df.columns.isin(['year','month','day_of_week'])]
df = df.drop(['year', 'month', 'day_of_week'], axis = 1)

# pull out tour name for a minute
df_tour = df['tour_name']
df = df.drop(['tour_name'], axis = 1)

# encode categorical w/ label sparse matrix
d = defaultdict(LabelEncoder)
df.iloc[:,:5] = df.apply(lambda x: d[x.name].fit_transform(x))

# add numeric back in then one hot
df = pd.concat([df_cont, df], axis=1, sort=False)

# one hot encode categorical
oh_enc = OneHotEncoder()
oh_enc.fit(df.iloc[:,:8])
df_encoded = oh_enc.transform(df.iloc[:,:8]).toarray()

#resort df
df = df.iloc[:,8:]
df = df[['Capacity', 'RESULT_PER_HEAD', 'RESULT_ATTEND', 'RESULT_GROSS']]

# PCA
pca = PCA(n_components = 5)
pca.fit(df_encoded)
df_pca = pca.transform(df_encoded)
df_pca = pd.DataFrame(df_pca, index=df_pca[:,0])

#standardize continuous data
scaler = StandardScaler()
scaler.fit(df.iloc[:,:2])
df.iloc[:,:2] = scaler.transform(df.iloc[:,:2])

#drop unneeded
df = df.drop(['RESULT_PER_HEAD'], axis = 1)

# glue back together
df_pca = df_pca.reset_index(drop=True)
df = pd.concat([df_pca, df], axis = 1, sort = False)
df['tour_name'] = df_tour


'''
# Label Encoder Notes

# Inverse the encoded
fit.apply(lambda x: d[x.name].inverse_transform(x))

# Using the dictionary to label future data
df.apply(lambda x: d[x.name].transform(x))
'''


##################################
### SET UP TEST AND TRAIN ########
##################################

# Validation set is PArkway and first two weeks WRAABB
validation = df.loc[df['tour_name'].isin(['parkway', 'wraabb'])]
df = df.loc[~df['tour_name'].isin(['parkway', 'wraabb'])]

# test set is last week WRAABB
test = validation.iloc[-7:,:]
validation = validation.iloc[:-7,:]

df = df.drop(['tour_name'], axis =1)
validation = validation.drop(['tour_name'], axis =1)
test = test.drop(['tour_name'], axis =1)


###############################################
# split indepenent/dependent vars in all sets #
###############################################

#train
X_train = df.iloc[:,0:6]
Y_attend_train = df['RESULT_ATTEND']
Y_gross_train = df['RESULT_GROSS']

#validation
X_val = validation.iloc[:,0:6]
Y_attend_val = validation['RESULT_ATTEND']
Y_gross_val = validation['RESULT_GROSS']

#test
X_test = test.iloc[:,0:6]
Y_attend_test = test['RESULT_ATTEND']
Y_gross_test = test['RESULT_GROSS']



#########################################
######### MODEL TESTING #################
########################################




#################################################
## NOTES FOR NEW DATA PIPELINE
#################################################

'''
PIPELINE

-pull out year, month, day & tour
        #set into new_cont & drop from new_df
-label encode new_df[:,:5] 
        # df.apply(lambda x: d[x.name].transform(x))
-add new_cont back into df       <- check order
        #new_df = concat(new_cont, new_df)
-one hot encode new_df[:,:8]
        #oh_enc.transform(nww_df[:,:8])
-PCA on encoded df
        # pca.transform(encoded data)
-scaler on [capacity, result_per_head]
        #scaler.transform(new_df[cap, per_head])  ,_create perhead if needed
-drop unneeded
        #drop per_head
-concat pca & new_df
        # THIS IS X to predict
        
-run chosen model on this X to get Y
'''