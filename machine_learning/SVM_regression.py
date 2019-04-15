#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pickle
X_train, y_train = pickle.load(open('cadata.pickle','rb'))
from sklearn.preprocessing import scale
first_rows = 6000
X_train = scale(X_train[:first_rows,:].toarray())
y_train = y_train[:first_rows]/10**4.0 # Resoults will be in 1000s of dolars


# In[10]:


import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVR
hypotesis = SVR(gamma ='scale')
scores = cross_val_score(hypotesis, X_train, y_train, cv=3, scoring='neg_mean_absolute_error')
print("SVR -> accuracy of cross-validation:\nmean = %f\nstandard deviation = %f" %(np.mean(scores),np.std(scores)))


# In[ ]:




