#!/usr/bin/python
|

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
from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors = 4)
neigh.fit(features_train, labels_train)

t0 = time()
neigh.fit(features_train, labels_train)
print "# training time: ", round(time() - t0,3) ,'s'

t1 = time()
pred_neigh = neigh.predict(features_test)
print "# prediction time: ", round(time() - t1, 3) ,'s'

from sklearn.metrics import accuracy_score
accuracy_neigh = accuracy_score(pred_neigh, labels_test)
print "# accuracy_neigh : ", accuracy_neigh

print '# parameters: ', neigh
#########################################################


print '\n\n##################################################\n\n'
print "actual output:", ','.join(pred)
print "\n\n--------------------------\n\n"
print "expected output:", ','.join(labels_test)
