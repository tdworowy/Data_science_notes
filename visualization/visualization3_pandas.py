#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
groups = list(iris.target)
iris_df['groups'] = pd.Series([iris.target_names[k] for k in groups])


# In[3]:


boxplots = iris_df.boxplot(return_type='axes')
boxplots


# In[6]:


boxplots = iris_df.boxplot(column='sepal length (cm)', by='groups', return_type='axes')
boxplots


# In[7]:


boxplots = iris_df.boxplot(column='sepal width (cm)', by='groups', return_type='axes')
boxplots


# In[8]:


densityplot = iris_df.plot(kind='density')
densityplot


# In[10]:


single_distribution = iris_df['petal width (cm)'].plot(kind='hist', alpha=1)


# In[11]:


single_distribution = iris_df['sepal length (cm)'].plot(kind='hist', alpha=1)


# In[12]:


colors_palette = {0:'red', 1:'yellow', 2:'blue'}
colors = [colors_palette[c] for c in groups]
simple_scatterplot = iris_df.plot(kind='scatter',x=0, y=1, c=colors)


# In[15]:


hexbib = iris_df.plot(kind='hexbin',x=0, y=1, gridsize=10)


# In[21]:


from pandas.plotting import scatter_matrix
colors_palette = {0:'red', 1:'yellow', 2:'blue'}
colors = [colors_palette[c] for c in groups]
matrix_of_scatterplots = scatter_matrix(iris_df, alpha=1, figsize=(10,10), color=colors, diagonal='kde')


# In[22]:


from pandas.plotting import parallel_coordinates
pll = parallel_coordinates(iris_df, 'groups')


# In[ ]:




