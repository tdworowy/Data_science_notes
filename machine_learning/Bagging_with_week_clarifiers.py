#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Bootstrap aggregating, also called bagging, is a machine learning ensemble meta-algorithm 
# designed to improve the stability and accuracy of machine learning algorithms used in statistical 
# classification and regression. It also reduces variance and helps to avoid overfitting. 
# Although it is usually applied to decision tree methods, it can be used with any type of method. 
# Bagging is a special case of the model averaging approach.
# https://en.wikipedia.org/wiki/Bootstrap_aggregating

import pickle
import numpy as np
covertype_dataset = pickle.load(open('covertype_dataset.pickle','rb'))
covertype_X = covertype_dataset.data[:50000,:]
covertype_Y = covertype_dataset.target[:50000] -1
covertypes = ['Spruce/Fir','Lodgepole Pine', 'Ponderosa Pine', 'Cottonwod/Wollow', 'Aspen', 'Dougles-fir', 'Krummholz']


# In[2]:


from sklearn.model_selection import cross_val_score
from sklearn.ensemble import BaggingClassifier
from sklearn.neighbors import KNeighborsClassifier
hypothesis = BaggingClassifier(KNeighborsClassifier(n_neighbors=1),
max_samples=0.7, max_features=0.7, n_estimators=100)
scores = cross_val_score(hypothesis, covertype_X, covertype_Y, cv=3, scoring='accuracy', n_jobs=-1)
print("BaggingClassifier -> accuracy of cross-validation:\nmean = %f\nstandard deviation = %f" %(np.mean(scores),np.std(scores)))


# In[ ]:




