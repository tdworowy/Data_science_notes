#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

iris_file = 'iris.csv'
iris = pd.read_csv(iris_file, sep=',', decimal='.', header=None, names=['sepal_length', 'sepal_width',
                                                                        'petal_length', 'petal_width',
                                                                        'target'])

# In[2]:


iris.head(20)

# In[3]:


iris.columns

# In[4]:


target = iris['target']
print(target)

# In[5]:


x = iris[['sepal_length', 'sepal_width']]
print(x)

# In[6]:


#### lazy read
iris_chunk = pd.read_csv(iris_file, header=None, names=['sepal_length', 'sepal_width',
                                                        'petal_length', 'petal_width',
                                                        'target'], chunksize=10)

for chunk in iris_chunk:
    print("Dimensions", chunk.shape)
    print(chunk, "\n")

# In[7]:


#### lazy read iterator
iris_iterator = pd.read_csv(iris_file, header=None, names=['sepal_length', 'sepal_width',
                                                           'petal_length', 'petal_width',
                                                           'target'], iterator=True)
print(iris_iterator.get_chunk(10).shape)
print(iris_iterator.get_chunk(2))

# In[8]:


#### batch read CSV
import csv
import numpy as np


def batch_read(file_name, batch=5):
    with open(file_name, 'rt') as data_stream:
        batch_output = list()
        for n, row in enumerate(csv.reader(data_stream, dialect='excel')):
            if n > 0 and n % batch == 0:
                yield (np.array(batch_output))
                batch_output = list()
            batch_output.append(row)
        leftyield(np.array(batch_output))


batch = batch_read(iris_file, batch=3)
print(next(batch))
print(next(batch))

# In[9]:


#### Custom data frame
custom_data_frame = pd.DataFrame({'Col1': range(5), 'Col2': [1.0] * 5, "Col3": 1, 'Col4': "Test Test"})
print(custom_data_frame)

# In[10]:


#### Maks data
mask_feature = iris['sepal_length'] > 6.0
print(mask_feature)

# In[11]:


##### Mask data #2 set new value
mask_target = iris['target'] == 'Iris-virginica'
iris.loc[mask_target, 'target'] = 'New value'
print(iris['target'].unique())

# In[12]:


##### Grouping
grouped_mean = iris.groupby(['target']).mean()  # mean
print(grouped_mean)
grouped_variance = iris.groupby(['target']).var()  # variance
print(grouped_variance)

# In[13]:


#### sorting
iris.sort_values(by='sepal_length').head()

# In[14]:


#### Use one apply, execute function for rows or columns
iris.apply(np.count_nonzero, axis=1).head()

# In[15]:


#### Use one apply, execute function for rows or columns
iris.apply(np.count_nonzero, axis=0).head()

# In[16]:


#### Use one apply, execute function for rows or columns
iris.apply(lambda x: x is not 2, axis=1).head()

# In[17]:


#### Use one applymap
iris.applymap(lambda el: len(str(el))).head()

# In[29]:


#### Get data
print(iris['sepal_width'][20])
print(iris.loc[20, 'sepal_width'])
print(iris.iloc[20, 1])

print(iris[['sepal_width', 'petal_length']][18:20])

print(iris.loc[[18, 19, 20], ['sepal_width', 'petal_length']])

# In[ ]:


# In[ ]:
