#!/usr/bin/python

"""
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project.

    Use a Naive Bayes Classifier to identify emails by their authors

    authors and labels:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
#sys.path.append("/home/abhiteshd/Documents/Abhitesh _docs/Abhitesh/BITS/Semester-4 (June 2016)/udacity/projects/naive_bayes/projects/tools/")
from preprocess import preprocess


# import nltk
# print nltk.stopword()
# from nltk.corpus import stopwords
# https://pythonprogramming.net/stop-words-nltk-tutorial/
#
#
### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

# print features_train

# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]


#########################################################
### your code goes here ###
print "\n----------------------------------------\n"
from sklearn import tree
from sklearn.ensemble import AdaBoostClassifier
# Create and fit an AdaBoosted decision tree
bdt = AdaBoostClassifier(tree.DecisionTreeClassifier(max_depth=5),
                         algorithm="SAMME",
                         n_estimators=200)
t0 = time()
bdt.fit(features_train, labels_train)
print "# training time: ", round(time() - t0,3) ,'s'

t1 = time()
pred_bdt = bdt.predict(features_test)
print "# prediction time: ", round(time() - t1, 3) ,'s'

from sklearn.metrics import accuracy_score
accuracy_bdt = accuracy_score(pred_bdt, labels_test)
print "# accuracy_bdt : ", accuracy_bdt

print '# parameters: ', bdt
#########################################################


print '\n\n##################################################\n\n'
print "actual output:", ','.join(pred_bdt)
print "\n\n--------------------------\n\n"
print "expected output:", ','.join(labels_test)
