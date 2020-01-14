#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 16:44:01 2020

@author: chinmay
"""

import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn import datasets
import numpy as np

df = pd.read_excel (r'/home/chinmay/Downloads/Speed Test/Automated Module/Excel/Down_regulation.xlsx')

A = df.iloc[:,1:49]
B = df.iloc[:,49]

encoder = LabelEncoder()
encoder.fit(B)
encoded_b = encoder.transform(B)
# convert integers to dummy variables (i.e. one hot encoded)
dummy_b = np_utils.to_categorical(encoded_b)

'''
def baseline_model():
	# create model
	model = Sequential()
	model.add(Dense(8, input_dim=48, activation='relu'))
	model.add(Dense(3, activation='softmax'))
	# Compile model
	model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    
	return model

estimator = KerasClassifier(build_fn=baseline_model, epochs=200, batch_size=5, verbose=0)

kfold = KFold(n_splits=10, shuffle=True)

results = cross_val_score(estimator, A, dummy_b, cv=kfold)
print("Baseline: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))

'''

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

train1, test1 = train_test_split(df, test_size=0.1)

A1 = train1.iloc[:,1:49]
B1 = train1.iloc[:,49]
A2 = test1.iloc[:,1:49]
B2 = test1.iloc[:,49]

encoder = LabelEncoder()
encoder.fit(B1)
encoded_b1 = encoder.transform(B1)
# convert integers to dummy variables (i.e. one hot encoded)
dummy_b1 = np_utils.to_categorical(encoded_b1)

model = Sequential()
model.add(Dense(43, input_dim=48, activation='relu'))
model.add(Dense(38, input_dim=43, activation='relu'))
model.add(Dense(33, input_dim=38, activation='relu'))
model.add(Dense(28, input_dim=33, activation='relu'))
model.add(Dense(23, input_dim=28, activation='relu'))
model.add(Dense(18, input_dim=23, activation='relu'))
model.add(Dense(13, input_dim=18, activation='relu'))
model.add(Dense(8, input_dim=13, activation='relu'))
model.add(Dense(3, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
test = model.fit(A1,dummy_b1,epochs = 90, batch_size = 5)

ynew = model.predict(A2)
# convert integers to dummy variables (i.e. one hot encoded)


dff = pd.DataFrame(ynew)
dff.rename(columns={0:'Down',1:'Not_diff',2:'up'}, inplace=True)
result = dff.idxmax(axis=1)
print (result)

print(confusion_matrix(B2, result))
print(classification_report(B2, result))
