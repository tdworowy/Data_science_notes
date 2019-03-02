#!/usr/bin/env python
# coding: utf-8

# In[5]:


from sklearn.model_selection import KFold
kfolding = KFold(n_splits=10, shuffle=True, random_state=1)
X = range(0, 100)
for train_idx, validation_idx in kfolding.split(X):
    print(train_idx, validation_idx)


# In[ ]:




