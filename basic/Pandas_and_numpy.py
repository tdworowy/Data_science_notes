#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

iris_filename = "iris.csv"
iris = pd.read_csv(iris_filename, sep=',', decimal='.', header=None, names=['sepal_length', 'sepal_width',
                                                                            'petal_length', 'petal_width',
                                                                            'target'])

# In[5]:


print(iris.values)

# In[6]:


print(iris.dtypes)

# In[12]:


import numpy as np

array = np.arange(5).reshape(1, 5)
print(array)
x = array + 1
print(x)
y = array * array
print(y)

# In[14]:


array2 = np.array([1, 2, 3, 4, 5] * 5).reshape(5, 5)
array3 = array2.T
print(array2 * array3)

# In[16]:


print(np.sum(array2, axis=0))
print(np.sum(array2, axis=1))
print(np.average(array2, axis=0))
print(np.average(array2))

# In[23]:


array4 = np.arange(5 * 5, dtype='float').reshape(5, 5)
coefs = np.array([1., 0.5, 0.5, 0.5, 0.5])
coefs_matrix = np.column_stack((coefs, coefs[::-1]))
print(coefs_matrix)

# In[24]:


# https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.dot.html
np.dot(array4, coefs)

# In[25]:


np.dot(coefs, array4)

# In[26]:


np.dot(array4, coefs_matrix)

# In[29]:


# Indexation (it create data view not copy)
array5 = np.arange(100, dtype=int).reshape(10, 10)
print(array5[2:9:2, :])

# In[30]:


(array5[2:9:2, 5:])

# In[32]:


print(array5[2:9:2, 5::-1])

# In[35]:


mask = (array5 >= 20) & (array5 <= 90) & ((array5 / 10.) % 1 >= 0.5)
print(array5[mask])

# In[36]:


row_index = [1, 1, 2, 7]
col_index = [0, 2, 4, 8]
print(array5[row_index, col_index])

# In[40]:


# add data (2 dimensions)
dataset = np.arange(50).reshape(10, 5)
single_line = np.arange(1 * 5).reshape(1, 5)
few_lines = np.arange(3 * 5).reshape(3, 5)

new_data = np.vstack((dataset, single_line))
print(new_data)
new_data = np.vstack((new_data, few_lines))
print(new_data)

# alternative  w_data = np.vstack((new_data,single_line, few_lines))


# In[43]:


# add data (3 dimensions)
np.dstack((dataset * 1, dataset * 2, dataset * 3))

# In[ ]:
