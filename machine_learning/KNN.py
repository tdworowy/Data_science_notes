#!/usr/bin/env python
# coding: utf-8

# In[8]:


#k-nearest neighbors
#from sklearn.utils import shuffle
from sklearn.datasets import fetch_mldata
from sklearn.model_selection import train_test_split
import pickle

mnist = pickle.load(open('mnist.pickle','rb'))
dir(mnist.train)
mnist.train.images, mnist.train.labels
mnist.train.images.shape


# In[10]:


mnist_data = mnist.train.images[:10000]
mnist_target = mnist.train.labels[:10000]


# In[11]:


from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(mnist_data, mnist_target, test_size=0.2, random_state=0)


# In[12]:


from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(3)
clf.fit(X_train, Y_train)


# In[14]:


y_pred = clf.predict(X_test)
from sklearn.metrics import classification_report
print(classification_report(Y_test, y_pred))


# In[15]:


get_ipython().run_line_magic('timeit', 'clf.fit(X_train, Y_train)')


# In[16]:


get_ipython().run_line_magic('timeit', 'clf.predict(X_test)')


# In[ ]:




