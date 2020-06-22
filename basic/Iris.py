#!/usr/bin/env python
# coding: utf-8

# In[3]:


from sklearn import datasets

iris = datasets.load_iris()

# In[4]:


print(iris.DESCR)
print(iris.data)
print(iris.data.shape)
print(iris.feature_names)
print(iris.target)
print(iris.target.shape)
print(iris.target_names)

# In[8]:


import pandas as pd
import numpy as np

colors = list()
palette = {0: 'red', 1: 'green', 2: "blue"}

# In[9]:


for c in np.nditer(iris.target):
    colors.append(palette[int(c)])
dataframe = pd.DataFrame(iris.data, columns=iris.feature_names)

# In[13]:


sc = pd.plotting.scatter_matrix(dataframe, alpha=0.3, figsize=(10, 10), diagonal='hist', color=colors, marker='o',
                                grid=True)

# In[ ]:
