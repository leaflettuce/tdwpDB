# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 10:32:19 2018

@author: andyj
"""

import pandas as pd
import numpy as np
import math

from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from collections import defaultdict

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_validate
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.svm import SVR

import matplotlib.pyplot as plt
import seaborn as sns

# import data
data_dir = '../../data/processed/sales/'

df = pd.read_csv(data_dir + 'sales_3.0.csv')
df = df.drop(['id'], axis =1)

# tweak 
df = df.drop(['City', 'State', 'season'], axis =1)
pca_comps = 5
cont_drops = ['month', 'day_of_week']

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
df.iloc[:,:-4] = df.apply(lambda x: d[x.name].fit_transform(x))

# add numeric back in then one hot
df_cont = df_cont.drop(cont_drops, axis = 1)
df = pd.concat([df_cont, df], axis=1, sort=False)

# one hot encode categorical
oh_enc = OneHotEncoder()
oh_enc.fit(df.iloc[:,:-4])
df_encoded = oh_enc.transform(df.iloc[:,:-4]).toarray()

#resort df
df = df.iloc[:,-4:]
df = df[['Capacity', 'RESULT_PER_HEAD', 'RESULT_ATTEND', 'RESULT_GROSS']]

# PCA
pca = PCA(n_components = pca_comps)
pca.fit(df_encoded)
df_pca = pca.transform(df_encoded)

df_pca = pd.DataFrame(df_pca, index=df_pca[:,0])
df_encoded = pd.DataFrame(df_encoded, index=df_encoded[:,0])

# pca explained   - 76%
print("PCA explained variance: %2f" %(pca.explained_variance_ratio_.sum()))

#standardize continuous data
scaler = StandardScaler()
scaler.fit(df.iloc[:,:2])
df.iloc[:,:2] = scaler.transform(df.iloc[:,:2])

#drop unneeded
df = df.drop(['RESULT_PER_HEAD'], axis = 1)

# glue back together (pca & encoded)
df_pca = df_pca.reset_index(drop=True)
df_encoded = df_encoded.reset_index(drop=True)

df_p = pd.concat([df_pca, df], axis = 1, sort = False)
df_e = pd.concat([df_encoded, df], axis = 1, sort = False)

df_p['tour_name'] = df_tour
df_e['tour_name'] = df_tour

############################
## Encoded or PCA #########
############################
df = df_p
#df = df_e

df = df.drop([163])


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


# split indepenent/dependent vars in all sets 

#train
X_train = df.iloc[:,:-2]
Y_attend_train = df['RESULT_ATTEND']
Y_gross_train = df['RESULT_GROSS']

#validation
X_val = validation.iloc[:,:-2]
Y_attend_val = validation['RESULT_ATTEND']
Y_gross_val = validation['RESULT_GROSS']

#test
X_test = test.iloc[:,:-2]
Y_attend_test = test['RESULT_ATTEND']
Y_gross_test = test['RESULT_GROSS']


#########################################
######### MODEL TESTING (GROSS) ########
########################################

'''
####### Lin Reg ###########
reg = LinearRegression()
reg.fit(X_train, Y_gross_train)

Y_gross_val_pred = reg.predict(X_val)

'''
####### RIDGE #############
reg = Ridge(alpha = .5)
reg.fit(X_train, Y_gross_train)

Y_gross_val_pred = reg.predict(X_val)


'''
###### SVR ################
svr = SVR()
# gridsearch
parameters = {'kernel':['rbf','poly','linear'], 'C':[1.0, 0.5, 2.0], \
               'epsilon' : [0.2, 0.5]}
reg = GridSearchCV(svr, parameters)
reg.fit(X_train, Y_gross_train)

# cross validsate
cv_results = cross_validate(reg, X_train, Y_gross_train)
cv_results['test_score']  

#predict 
Y_gross_val_pred = reg.predict(X_val)
'''

########################################
####### MODEL RESULTS (GROSS) ###########
#########################################

# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(Y_gross_val, Y_gross_val_pred))

print("Root MSE: %2f"
      % math.sqrt(mean_squared_error(Y_gross_val, Y_gross_val_pred)))

# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' 
      % r2_score(Y_gross_val, Y_gross_val_pred))

# Residual plot
sns.set(style="whitegrid")
sns.residplot(Y_gross_val, Y_gross_val_pred)


##############################
### FINAL TEST ###############
#############################

Y_pred = reg.predict(X_test)
for i in range(0, 7):
    print("Actual: %2f  | Predicted: %2f    | Error: %2f" 
              %(Y_gross_test[i + 350], Y_pred[i], 
                (Y_pred[i] - Y_gross_test[i + 350])))
    
    
################################
##  NEW DATA PIPELINE
###############################

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






######################################3
## NOTES TO SELF ####################
###################################
'''
# Label Encoder Notes

# Inverse the encoded
fit.apply(lambda x: d[x.name].inverse_transform(x))

# Using the dictionary to label future data
df.apply(lambda x: d[x.name].transform(x))
'''
