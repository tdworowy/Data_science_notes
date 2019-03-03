#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn import datasets
iris = datasets.load_iris()
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=0)


# In[2]:


from sklearn.naive_bayes import GaussianNB
cif = GaussianNB()
cif.fit(X_train, Y_train)
Y_pred = cif.predict(X_test)


# In[3]:


from sklearn.metrics import classification_report
print(classification_report(Y_test, Y_pred))


# In[4]:


get_ipython().run_line_magic('timeit', 'cif.fit(X_train, Y_train)')


# In[ ]:




