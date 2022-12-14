# -*- coding: utf-8 -*-
"""Untitled11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uHHpHUSTwxyHXgGBlGjG6trlWCyKp6vI
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import RobustScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('churn modelling.csv', index_col=0)
df.head()

df.drop(['CustomerId', 'Surname'], axis=1, inplace=True)

df.shape

df.isna().sum()

X = df.drop('Exited', 1)
y = df.Exited

y.value_counts()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0, stratify=y)

X.columns

num_cols = ['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'EstimatedSalary']
cat_cols = ['HasCrCard', 'IsActiveMember', 'Geography', 'Gender']

ct = ColumnTransformer([
    ('s1', RobustScaler(), num_cols),
    ('s2', OneHotEncoder(sparse=False, handle_unknown='ignore'), cat_cols)
])

p = Pipeline([
    ('ct', ct),
    ('mod', LogisticRegression(random_state=0))
])

p.fit(X_train, y_train)

# predictions are for the default threshold of 0.5
preds = p.predict(X_test)
preds[:15]

# real class labels of the first 15 people in the test set
np.array(y_test)[:15]

from sklearn.metrics import confusion_matrix, plot_confusion_matrix

confusion_matrix(y_true=y_test, y_pred=preds)

p.classes_

confusion_matrix(y_test, preds, labels=(1,0))

confusion_matrix(y_test, preds, labels=(1,0)).ravel()

tp, fn, fp, tn = confusion_matrix(y_test, preds, labels=(1,0)).ravel()

precision = tp/(tp+fp)
precision

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score,\
fbeta_score, matthews_corrcoef

precision_score(y_test, preds)

confusion_matrix(y_test, preds, labels=(1,0))

confusion_matrix(y_test, preds, labels=(1,0)).ravel()

tp, fn, fp, tn = confusion_matrix(y_test, preds, labels=(1,0)).ravel()

precision = tp/(tp+fp)
precision

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score,\
fbeta_score, matthews_corrcoef

precision_score(y_test, preds)

recall_score(y_test, preds)

# harmonic mean of precision and recall
f1_score(y_test, preds)

# Precision more weight than recall (beta < 1)
fbeta_score(y_test, preds, beta=0.5)

# recall more weight than precision (beta > 1)
fbeta_score(y_test, preds, beta=2)

# when both classes need to be predicted with good accuracies, MCC is better than F-measures
matthews_corrcoef(y_test, preds)

from sklearn.metrics import SCORERS

sorted(SCORERS.keys())

from sklearn.metrics import plot_roc_curve, plot_precision_recall_curve, roc_curve

plot_roc_curve(p, X_test, y_test)
plt.plot([0,1], [0,1], c='k')

