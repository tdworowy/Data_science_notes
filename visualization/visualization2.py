#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt
iris = load_iris()
averge = np.mean(iris.data,axis=0)
std = np.std(iris.data,axis=0)
range_ = range(np.shape(iris.data)[1])


# In[5]:


plt.subplot(1,2,1)
plt.title("Horizontal bars")
plt.barh(range_, averge, color='r',xerr=std, alpha=1, align='center')
plt.yticks(range_, iris.feature_names)
plt.subplot(1,2,2)
plt.title("Vertical bars")
plt.bar(range_, averge, color='b', yerr=std, alpha=1, align='center')
plt.xticks(range_, range_)
plt.show()


# In[14]:


from sklearn.datasets import fetch_olivetti_faces
dataset = fetch_olivetti_faces(shuffle=True, random_state=5)
for k in range(6):
    plt.subplot(2,3,k+1)
    plt.imshow(dataset.data[k].reshape(64,64), cmap=plt.cm.gray, interpolation='nearest')
    plt.title("Person nr: %s" % str(dataset.target[k]))
    plt.axis('off')
plt.show()


# In[16]:


from sklearn.datasets import load_digits
digits = load_digits()
for number in range(1,10):
    plt.subplot(3,3,number)
    plt.imshow(digits.images[number], cmap='binary', interpolation='none',extent=[0,8,0,8])
    plt.grid()
plt.show()


# In[ ]:




