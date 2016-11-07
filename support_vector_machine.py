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

# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

#########################################################
### your code goes here ###
from sklearn import svm
clf = svm.SVC(kernel = 'rbf', C =100000)
t1 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t1, 3), "s"

t2 = time()
pred = clf.predict(features_test)
print "prediction time:", round(time()-t2, 3), "s"

# count = 0
# for i in pred:
#     if i == 1:
#         count += 1

# print 'no. of prediction in favor of Chris: ', count

# print '10th element: ' , pred[10]
# print '26th element: ' , pred[26]
# print '50th element: ' , pred[50]


from sklearn.metrics import accuracy_score
accuracy = accuracy_score(pred, labels_test)
print "accuracy score: ", accuracy
print '# parameters: ', clf

#########################################################


print '\n\n##################################################\n\n'
print "actual output:", ','.join(pred)
print "\n\n--------------------------\n\n"
print "expected output:", ','.join(labels_test)
