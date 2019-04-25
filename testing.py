# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 16:48:27 2019

@author: Andrew
"""

import numpy as np
import pandas as pd
from sklearn import preprocessing
from knn23 import *
from scipy.spatial.distance import euclidean
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import f_regression
from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import  RFECV
from sklearn.metrics import mean_squared_error
from sklearn.metrics import median_absolute_error
from sklearn.metrics import r2_score
from sklearn.metrics import explained_variance_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score

def print_binary_classif_error_report(preds, y_test):
    print('Accuracy: ' + str(accuracy_score(preds, y_test)))
    print('Precision: ' + str(precision_score(preds, y_test)))
    print('Recall: ' + str(recall_score(preds, y_test)))
    print('F1: ' + str(f1_score(preds, y_test)))
    print('ROC AUC: ' + str(roc_auc_score(preds, y_test)))
    
knn = KNN(5, euclidean)    
df = pd.read_csv('churn_data.csv')
df.head()

df = df.drop(['CustID'], axis=1)
le = preprocessing.LabelEncoder()
df.Gender = le.fit_transform(df.Gender)
df.Income = le.fit_transform(df.Income)
df.Churn = le.fit_transform(df.Churn)

cs = list(df.columns)
cs.remove('Churn')

data_x = df[cs]
data_y = df['Churn']

x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size= 0.2, random_state = 4)

selector_f = SelectPercentile(f_regression, percentile=25)
selector_f.fit(x_train, y_train)
fscores = []
for name, score, pv in zip(list(df), selector_f.scores_, selector_f.pvalues_):
    if pv <.05:
        fscores.append(name)

for i in df.columns:
    if i not in fscores:
        df = df.drop(i,axis = 1)
        
ds = list(df.columns)
data_x = df[ds]


x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size= 0.2, random_state = 4)    

knn.fit(x_train, y_train)

knn.pred(x_test)


















    























