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

features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]

#########################################################
### your code goes here ###
import matplotlib.pyplot as plt
from sklearn import svm, datasets
import numpy as np
import itertools
from sklearn.metrics import confusion_matrix


# clf = svm.SVC(kernel = 'rbf', C =10000)
clf = svm.SVC(kernel='rbf', C=1000)
t1 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t1, 3), "s"

class_names = list(set(labels_train))




t2 = time()
pred = clf.predict(features_test)
print "prediction time:", round(time()-t2, 3), "s"

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(pred, labels_test)
print "accuracy score: ", accuracy
#########################################################
print '# parameters: ', clf

# -------- cross validation graph

import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn import datasets, svm

# digits = datasets.load_digits()
# X = digits.data
# y = digits.target
svc = clf

# svc = svm.SVC(kernel='linear')
C_s = np.logspace(-10, 0, 10)
scores = list()
scores_std = list()
for C in C_s:
    svc.C = C
    this_scores = cross_val_score(svc, features_train, features_test, n_jobs=2)
    scores.append(np.mean(this_scores))
    scores_std.append(np.std(this_scores))

# Do the plotting
import matplotlib.pyplot as plt
plt.figure(1, figsize=(4, 3))
plt.clf()
plt.semilogx(C_s, scores)
plt.semilogx(C_s, np.array(scores) + np.array(scores_std), 'b--')
plt.semilogx(C_s, np.array(scores) - np.array(scores_std), 'b--')
locs, labels = plt.yticks()
plt.yticks(locs, list(map(lambda x: "%g" % x, locs)))
plt.ylabel('CV score')
plt.xlabel('Parameter C')
plt.ylim(0, 1.1)
plt.show()


# def plot_confusion_matrix(cm, classes,
#                           normalize=False,
#                           title='Confusion matrix',
#                           cmap=plt.cm.Blues):
#     """
#     This function prints and plots the confusion matrix.
#     Normalization can be applied by setting `normalize=True`.
#     """
#     plt.imshow(cm, interpolation='nearest', cmap=cmap)
#     plt.title(title)
#     plt.colorbar()
#     tick_marks = np.arange(len(classes))
#     plt.xticks(tick_marks, classes, rotation=45)
#     plt.yticks(tick_marks, classes)

#     if normalize:
#         cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
#         print("Normalized confusion matrix")
#     else:
#         print('Confusion matrix, without normalization')

#     print(cm)

#     thresh = cm.max() / 2.
#     for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
#         plt.text(j, i, cm[i, j],
#                  horizontalalignment="center",
#                  color="white" if cm[i, j] > thresh else "black")

#     plt.tight_layout()
#     plt.ylabel('True label')
#     plt.xlabel('Predicted label')

# # Compute confusion matrix
# cnf_matrix = confusion_matrix(labels_test, pred)
# np.set_printoptions(precision=2)

# # Plot non-normalized confusion matrix
# plt.figure()
# plot_confusion_matrix(cnf_matrix, classes=class_names,
#                       title='Confusion matrix, without normalization')

# # Plot normalized confusion matrix
# plt.figure()
# plot_confusion_matrix(cnf_matrix, classes=class_names, normalize=True,
#                       title='Normalized confusion matrix')

# plt.show()

# kernel curve

# # create a mesh to plot in
# x_min, x_max = features_train[:, 0].min() - 1, features_train[:, 0].max() + 1
# y_min, y_max = features_train[:, 1].min() - 1, features_train[:, 1].max() + 1
# h = (x_max / x_min)/100
# xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
# 	np.arange(y_min, y_max, h))

# print '\n\n-----------\n\n'
# print h
# print yy.ravel()
# print '\n\n-----------\n\n'

# plt.subplot(1, 1, 1)
# Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
# Z = Z.reshape(xx.shape)
# plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)

# plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
# plt.xlabel('Sepal length')
# plt.ylabel('Sepal width')
# plt.xlim(xx.min(), xx.max())
# plt.title('SVC with linear kernel')
# plt.show()





# print '\n\n##################################################\n\n'
# print "actual output:", ','.join(pred)
# print "\n\n--------------------------\n\n"
# print "expected output:", ','.join(labels_test)
