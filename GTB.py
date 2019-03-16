#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Gradient tree bosting
import pickle
covertype_dataset = pickle.load(open('covertype_dataset.pickle','rb'))
covertype_X = covertype_dataset.data[:15000,:]
covertype_Y = covertype_dataset.target[:15000] -1
covertype_val_X = covertype_dataset.data[15000:20000,:] 
covertype_val_Y = covertype_dataset.target[15000:20000] -1
covertype_test_X = covertype_dataset.data[20000:25000,:]
covertype_test_Y = covertype_dataset.target[20000:25000] -1


# In[7]:


from sklearn.model_selection import cross_val_score,StratifiedKFold
from sklearn.ensemble import GradientBoostingClassifier
hypothesis = GradientBoostingClassifier(max_depth=5, n_estimators=50, random_state=101)
hypothesis.fit(covertype_X, covertype_Y)


# In[9]:


from sklearn.metrics import accuracy_score
print("GradientBoostingClassifier -> accuracy on test set:", accuracy_score(covertype_test_Y, hypothesis.predict(covertype_test_X)))


# In[ ]:




