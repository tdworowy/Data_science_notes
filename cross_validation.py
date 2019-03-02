#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.datasets import load_digits
import numpy as np
digits = load_digits()
print(digits.DESCR)
x = digits.data
y = digits.target


# In[3]:


# hypotheses
from sklearn import svm
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn import datasets
h1 = svm.LinearSVC(C=1.0)
h2 = svm.SVC(kernel='rbf', degree=3, gamma=0.001, C=1.0)# classifier with a radial base function
h3 = svm.SVC(kernel='poly', degree=3,gamma='auto', C=1.0) # third degree polynomial classifier


# In[14]:


def cross_validate(eval_scoring): #https://scikit-learn.org/stable/modules/model_evaluation.html
    random_state = 1
    cv_folds = 10
    workers = -1 # use whole processor 
    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.30, random_state = random_state)
    for hypotezis in [h1, h2, h3]:
        scores = cross_val_score(hypotezis, X_train, Y_train, cv = cv_folds, scoring = eval_scoring, n_jobs= workers)
        print("%s \nEffectiveness of cross validation:\naverage: %s \nstandard deviation: %s \n" % (hypotezis, np.mean(scores), np.std(scores)))
print('***accuracy***')
cross_validate(eval_scoring = 'accuracy')
print('***f1***')
cross_validate(eval_scoring = 'f1_weighted')


# In[ ]:




