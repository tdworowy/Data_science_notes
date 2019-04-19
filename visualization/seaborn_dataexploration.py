#!/usr/bin/env python
# coding: utf-8

# In[5]:


import seaborn as sns
import pandas as pd
import numpy as np
sns.set()
from sklearn.datasets import load_iris
iris = load_iris()
X_iris, Y_iris = iris.data, iris.target
features_iris = [a[:-5].replace(" ","_") for a in iris.feature_names]
target_labels = {j: flower for j, flower in enumerate(iris.target_names)}
df_iris = pd.DataFrame(X_iris, columns=features_iris)
df_iris['target'] = [target_labels[y] for y in Y_iris]
from sklearn.datasets import load_boston
boston = load_boston()
X_boston, Y_boston = boston.data, boston.target
features_boston = np.array(['V'+'_'.join([str(b),a])for a,b in zip(boston.feature_names, range(len(boston.feature_names)))])
df_boston = pd.DataFrame(X_boston, columns=features_boston)
df_boston['target'] = Y_boston
df_boston['target_level'] = pd.qcut(Y_boston, 3)


# In[7]:


with sns.axes_style("ticks"):
    sns.factorplot(data=df_boston, x='V8_RAD', y="target")


# In[8]:


with sns.axes_style("whitegrid"):
    sns.regplot(data=df_boston, x='V12_LSTAT', y='target', order=3)
    


# In[10]:


with sns.axes_style("whitegrid"):
    sns.jointplot("V4_NOX","V7_DIS", data=df_boston, kind='reg', order=3)


# In[12]:


with sns.axes_style("whitegrid"):
    sns.jointplot("V4_NOX","V7_DIS", data=df_boston, kind='scatter')


# In[13]:


with sns.axes_style("whitegrid"):
    sns.jointplot("V4_NOX","V7_DIS", data=df_boston, kind='kde')


# In[17]:


import matplotlib.pyplot as plt
with sns.axes_style("darkgrid"):
    chart = sns.FacetGrid(df_iris, col='target')
    chart.map(plt.scatter, 'sepal_length', 'petal_length')


# In[18]:


import matplotlib.pyplot as plt
with sns.axes_style("darkgrid"):
    chart = sns.FacetGrid(df_iris, col='target')
    chart.map(sns.distplot, 'sepal_length')


# In[19]:


import matplotlib.pyplot as plt
with sns.axes_style("darkgrid"):
    chart = sns.FacetGrid(df_boston, col='target_level')
    chart.map(sns.regplot, 'V4_NOX', 'V7_DIS')


# In[21]:


with sns.axes_style('whitegrid'):
    ax = sns.violinplot(x='target', y='sepal_length', data=df_iris, palette='pastel')
sns.despine(offset=10, trim=True)


# In[22]:


with sns.axes_style('whitegrid'):
    chart = sns.pairplot(data=df_iris, hue='target', diag_kind='hist')


# In[ ]:




