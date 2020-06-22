#!/usr/bin/env python
# coding: utf-8

# In[3]:


# load data
import pandas as pd

iris_file = 'iris.csv'
iris = pd.read_csv(iris_file, header=None, names=['sepal_length', 'sepal_width',
                                                  'petal_length', 'petal_width',
                                                  'target'])
iris.head()

# In[4]:


iris.describe()

# In[7]:


# box plote
box = iris.boxplot(return_type='axes')

# In[8]:


# quantile 1
iris.quantile([0.1, 0.9])

# In[9]:


# quantile 2
iris.quantile([0.01, 0.02])

# In[10]:


# quantile 3
iris.quantile([0.99])

# In[11]:


# get categorical features
iris.target.unique()

# In[15]:


# similarity matrix
# 3.758667 and 1.198667 are mens
pd.crosstab(iris['petal_length'] > 3.758667, iris['petal_width'] > 1.198667)

# In[23]:


# similarity matrix 2
# 5.843333 and 1.198667 are mens
pd.crosstab(iris['sepal_length'] > 5.843333, iris['sepal_width'] > 1.198667)

# In[17]:


# scatter plot
# same data sa in similarity matrix 1
scatter_plot = iris.plot(kind='scatter', x='petal_width', y='petal_length', s=64, c='blue', edgecolors='white')

# In[25]:


# scatter plot
# same data sa in similarity matrix 2
scatter_plot = iris.plot(kind='scatter', x='sepal_width', y='sepal_length', s=64, c='blue', edgecolors='white')

# In[26]:


# scatter plot
scatter_plot = iris.plot(kind='scatter', x='sepal_width', y='petal_length', s=64, c='blue', edgecolors='white')

# In[27]:


# scatter plot
scatter_plot = iris.plot(kind='scatter', x='sepal_width', y='petal_width', s=64, c='blue', edgecolors='white')

# In[28]:


# scatter plot
scatter_plot = iris.plot(kind='scatter', x='sepal_length', y='petal_width', s=64, c='blue', edgecolors='white')

# In[31]:


# scatter plot
scatter_plot = iris.plot(kind='scatter', x='sepal_length', y='petal_length', s=64, c='blue', edgecolors='white')

# In[19]:


# distribution of features 1
distr = iris.petal_width.plot(kind='hist', alpha=0.5, bins=20)

# In[20]:


# distribution of features 2
distr = iris.petal_length.plot(kind='hist', alpha=0.5, bins=20)

# In[21]:


# distribution of features 3
distr = iris.sepal_width.plot(kind='hist', alpha=0.5, bins=20)

# In[22]:


# distribution of features 4
distr = iris.sepal_length.plot(kind='hist', alpha=0.5, bins=20)

# In[ ]:
