#!/usr/bin/env python
# coding: utf-8

# In[1]:


# binary clasyfication

from sklearn.datasets import load_boston
boston = load_boston()
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.2, random_state=0)


# In[4]:


import numpy as np
avg_price_house = np.average(boston.target)
high_priced_idx = (y_train >= avg_price_house)
y_train[high_priced_idx] = 1
y_train[np.logical_not(high_priced_idx)] = 0
y_train = y_train.astype(np.int8)

high_priced_idx = (y_test >= avg_price_house)
y_test[high_priced_idx] = 1
y_test[np.logical_not(high_priced_idx)] = 0
y_test = y_test.astype(np.int8)


# In[7]:


from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(solver='liblinear')
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))


# In[ ]:




