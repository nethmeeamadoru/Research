import pandas as pd
from collections import Counter
from imblearn.over_sampling import RandomOverSampler
from sklearn.preprocessing import OneHotEncoder
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import tree
import pickle
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report

rawdata = pd.read_csv('dataset/testDataTrial.csv') # removed 
# rawdata['Age'] = rawdata['Age'].astype(float)

rawdata.head()

rawdata.loc[rawdata['Treatment'] == 'Temporary Filling', 'Treatment'] = "Temporary filling"

X = rawdata.iloc[:,1:35]

y = rawdata.iloc[:,35]

#random oversampler
print('Original dataset shape %s' % Counter(y))

rus = RandomOverSampler(random_state=42)
X, y = rus.fit_resample(X, y)
print('Resampled dataset shape %s' % Counter(y))


# one hot encode
onehot_encoder = OneHotEncoder(sparse=False)
y = y.reshape(-1,1)
onehot_encoded_y = onehot_encoder.fit_transform(y)

X_trainDT, X_testDT, y_trainDT, y_testDT = train_test_split(X, y, test_size=0.3, random_state=42)

# Decision Tree Classifier
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_trainDT, y_trainDT)

# Bayesian Classifier
bayes_clf = GaussianNB()
bayes_clf.fit(X_trainDT, y_trainDT)

y_pred = clf.predict(X_testDT)
bayes_y_pred = bayes_clf.predict(X_testDT)

target_names = ['Extraction',
 'X ray',
 'Permanent filling',
 'LCC',
 'Scaling',
 'Consultation',
 'Temporary filling',
 'GIC',
 'AB x',
 'Ortho plate adjustments',
 'Root canal treatment']


# Evaluate Accuracy
print('Accuracy of Decision Trees')
print(classification_report(y_testDT, y_pred, target_names=target_names))
print('*'*100)
print('Accuracy of Bayesian Model')
print(classification_report(y_testDT, bayes_y_pred, target_names=target_names))

print('Prediction: ', bayes_y_pred)

pickle.dump(clf, open('test/sample_test.pkl', 'wb')) # removed test/
pickle.dump(bayes_clf, open('test/bayes_sample_test.pkl', 'wb')) # removed test/
