#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.datasets import make_classification
X, y = make_classification(n_samples = 100, n_features=100, 
                          n_informative=5, n_redundant=2, random_state=101)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)


# In[5]:


from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(C=0.1, penalty='l1', random_state=101) # the smaller the value the fewer features is chosen
classifier.fit(X_train, y_train)
print("Accuracy of trening samples: %3f" % classifier.score(X_train, y_train))
print("Accuracy of test samples: %3f" % classifier.score(X_test, y_test))


# In[6]:


from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(C=0.6, penalty='l1', random_state=101) # the smaller the value the fewer features is chosen
classifier.fit(X_train, y_train)
print("Accuracy of trening samples: %3f" % classifier.score(X_train, y_train))
print("Accuracy of test samples: %3f" % classifier.score(X_test, y_test))


# In[8]:


from sklearn.linear_model import RandomizedLogisticRegression
selector = RandomizedLogisticRegression(n_resampling=300, random_state=101)
selector.fit(X_train, y_train)
X_train_s = selector.transform(X_train)
X_test_s = selector.transform(X_test)
classifier.fit(X_train_s, y_train)


# In[9]:


print("Number of chosen variables: %i" % sum(selector.get_support()!=0))
print("Accuracy of trening samples: %3f" % classifier.score(X_train_s, y_train))
print("Accuracy of test samples: %3f" % classifier.score(X_test_s, y_test))


# In[12]:


from sklearn.linear_model import RandomizedLasso  # works for linear models
from sklearn.datasets import make_regression
X, y = make_regression(n_samples=100, n_features=10, n_informative=4, random_state=101)
rlasso = RandomizedLasso()
rlasso.fit(X,y)


# In[13]:


list(enumerate(rlasso.scores_)) # only 4 features are informative


# In[ ]:




