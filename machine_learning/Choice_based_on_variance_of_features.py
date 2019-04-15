#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
from sklearn.datasets import make_classification
X, y = make_classification(n_samples=10, n_features=6, n_informative=3, n_redundant=1, random_state=101)


# In[10]:


print("varinace: %s" % np.var(X, axis=0))


# In[12]:


from sklearn.feature_selection import VarianceThreshold
X_selected = VarianceThreshold(threshold=1.0).fit_transform(X)
print("Before %s" % X[0,:])
print("After %s" % X_selected[0,:])


# In[ ]:




