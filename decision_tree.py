#!/usr/bin/python
|

import sys
from time import time
sys.path.append("../tools/")
from preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

# print type(labels_train)
# print dict((i, labels_train.count(i)) for i in labels_train)
# print '\n\n----------------------------\n\n'
# print dict((i, labels_test.count(i)) for i in labels_test)

# sys.exit('--checking count--')


#########################################################
### your code goes here ###
from sklearn import tree
clf = tree.DecisionTreeClassifier(min_samples_split = 40)
t0 = time()
clf.fit(features_train, labels_train)
print "training time: ", round(time() - t0,3) ,'s'

t1 = time()
pred = clf.predict(features_test)
print "prediction time: ", round(time() - t1, 3) ,'s'

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(pred, labels_test)
print "accuracy: ", accuracy


#########################################################
print '\n\n##################################################\n\n'
print "actual output:", ','.join(pred)
print "\n\n--------------------------\n\n"
print "expected output:", ','.join(labels_test)
