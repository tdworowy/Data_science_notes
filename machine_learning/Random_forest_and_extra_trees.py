#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, RandomForestRegressor, ExtraTreesRegressor


# In[2]:


# Classification
import pickle
import numpy as np
covertype_dataset = pickle.load(open('covertype_dataset.pickle','rb'))
covertype_X = covertype_dataset.data[:80000,:]
covertype_Y = covertype_dataset.target[:80000] -1
covertypes = ['Spruce/Fir','Lodgepole Pine', 'Ponderosa Pine', 'Cottonwod/Wollow', 'Aspen', 'Dougles-fir', 'Krummholz']


# In[3]:


get_ipython().run_cell_magic('time', '', 'hypothesis = RandomForestClassifier(n_estimators=600, random_state=101)\nscores = cross_val_score(hypothesis, covertype_X, covertype_Y, cv=3, scoring=\'accuracy\', n_jobs=-1)\nprint("RandomForestClassifier -> accuracy of cross-validation:\\nmean = %f\\nstandard deviation = %f" %(np.mean(scores),np.std(scores)))')


# In[4]:


get_ipython().run_cell_magic('time', '', 'hypothesis = ExtraTreesClassifier(n_estimators=600, random_state=101)\nscores = cross_val_score(hypothesis, covertype_X, covertype_Y, cv=3, scoring=\'accuracy\', n_jobs=-1)\nprint("ExtraTreesClassifier -> accuracy of cross-validation:\\nmean = %f\\nstandard deviation = %f" %(np.mean(scores),np.std(scores)))')


# In[5]:


# Regression
import pickle
X_train, y_train = pickle.load(open('cadata.pickle','rb'))
from sklearn.preprocessing import scale
first_rows = 6000
X_train = scale(X_train[:first_rows,:].toarray())
y_train = y_train[:first_rows]/10**4.0 # Resoults will be in 1000s of dolars


# In[6]:


hypotesis = RandomForestRegressor(n_estimators=600, random_state=101)
scores = cross_val_score(hypotesis, X_train, y_train, cv=3, scoring='neg_mean_absolute_error', n_jobs=-1)
print("RandomForestRegressor -> accuracy of cross-validation:\nmean = %f\nstandard deviation = %f" %(np.mean(scores),np.std(scores)))


# In[7]:


hypotesis = ExtraTreesRegressor(n_estimators=600, random_state=101)
scores = cross_val_score(hypotesis, X_train, y_train, cv=3, scoring='neg_mean_absolute_error', n_jobs=-1)
print("RandomForestRegressor -> accuracy of cross-validation:\nmean = %f\nstandard deviation = %f" %(np.mean(scores),np.std(scores)))


# In[ ]:




