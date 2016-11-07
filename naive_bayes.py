#!/usr/bin/python

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


#########################################################
### your code goes here ###
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

print "total features train: ", len(features_train)
print "total features test: ", len(features_test)

pred = clf.predict(features_test[0])



t1 = time()
pred = clf.predict(features_test)
print "predeiction time:", round(time()-t1, 3), "s"
# print pred
# print labels_test

from sklearn.metrics import accuracy_score
acurracy = accuracy_score(pred,labels_test)
print "accuracy: " , acurracy


#########################################################


print '\n\n##################################################\n\n'
print "actual output:", ','.join(pred)
print "\n\n--------------------------\n\n"
print "expected output:", ','.join(labels_test)
