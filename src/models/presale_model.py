# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 13:28:46 2018

@author: andyj
"""
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import math
import seaborn as sns
import numpy as np

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_validate
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import Ridge
from sklearn.svm import SVR

# import data
data_dir = '../../data/processed/sales/'

df = pd.read_csv(data_dir + 'ps_sales_3.0.csv')
df = df.drop(['Unnamed: 0'], axis =1)

# drop all categorical but tour_type -> considered in sales model
df = df.drop(['State', 'year', 'month', 'season', 'region', 'day_of_week', 
              'RESULT_PER_HEAD', 'RESULT_ATTEND', 'Open', 'tour_type',
              'tour_name'], axis = 1)

df = df.drop([4])

df['Total Sold'] = (df['Percent Sold']/100)*df['Capacity']
df['Total Sold'] = df['Total Sold'].apply(lambda x: math.ceil(x))

# Standardize all inputs
scaler = StandardScaler()
df.iloc[:,:-1] = scaler.fit_transform(df.iloc[:,:-1])

#test train split
X_train, X_test, y_train, y_test = train_test_split(df.iloc[:,:-1], 
                                                    df['RESULT_GROSS'], 
                                                    test_size=0.15, random_state=42)


#Fit models!

####### RIDGE #############
reg = Ridge(alpha = .5)
reg.fit(X_train, y_train)

y_pred = reg.predict(X_test)


###### SVR ################
svr = SVR()
# gridsearch
parameters = {'kernel':['rbf','poly','linear'], 'C':[1.0, 0.5, 2.0], \
               'epsilon' : [0.2, 0.5]}
reg = GridSearchCV(svr, parameters)
reg.fit(X_train, y_train)

# cross validsate
cv_results = cross_validate(reg, X_train, y_train)
cv_results['test_score']  

#predict 
y_pred = reg.predict(X_test)


### RESULTS
########################################
####### MODEL RESULTS (GROSS) ###########
#########################################

# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(y_test, y_pred))

print("Root MSE: %2f"
      % math.sqrt(mean_squared_error(y_test, y_pred)))

# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' 
      % r2_score(y_test, y_pred))

# Residual plot
sns.set(style="whitegrid")
sns.residplot(y_test, y_pred)


################################
##  NEW DATA PIPELINE
###############################

df_pred = pd.read_csv('../../data/processed/upcoming/leg2_cleaned.csv')

df_pred = scaler.transform(df_pred)

results = reg.predict(df_pred)

np.savetxt("../../data/predictions/leg2_presale.csv", results, delimiter=",")
'''
PIPELINE

-only use [cap, days out, total sold, precent sold, days_ps_xcross]
- Transform with scaler
-run reg predict
-PRINT OUT to CSV
'''

