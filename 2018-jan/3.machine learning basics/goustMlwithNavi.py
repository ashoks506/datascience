# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:59:35 2018

@author: asatharla
"""

import pandas as pd
import os
from sklearn import naive_bayes
import pydot
import io
from sklearn import model_selection

print(os.getcwd())
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/graphviz-2.38/release/bin'

goust_train = pd.read_csv('ghouls_train.csv')
goust_train.shape
goust_train.info()

#separeate features from target column
features = ['bone_length','hair_length','has_soul','rotting_flesh']
X_train = goust_train[features]
y_train = goust_train[['type']]

#create an instance of machine learning class 
nb_estimator = naive_bayes.GaussianNB()
nb_estimator.fit(X_train, y_train)

scores = model_selection.cross_validate(nb_estimator, X_train, y_train, cv=10)
print(scores)
scores.get('test_score').mean()
scores.get('train_score').mean()

goust_test = pd.read_csv('ghouls_test.csv')
goust_test.shape
goust_test.info()

X_test = goust_test[features]
goust_test['type'] = nb_estimator.predict(X_test)

goust_test.to_csv('naive_goust_hair_soul_flesh.csv', columns=['id','type'],index=False)
