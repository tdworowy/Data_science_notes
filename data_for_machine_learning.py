#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pickle
import urllib
from sklearn.datasets import fetch_mldata, load_svmlight_file, fetch_covtype, fetch_20newsgroups


# In[6]:


# mnist = fetch_mldata("MNIST original") # [WinError 10060] A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
pickle.dump(mnist, open("mnist.pickle",'wb'))


# In[7]:


target_page = 'http://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/binary/ijcnn1.bz2'
with urllib.request.urlopen(target_page) as response:
    with open('jjcnn1.bz2','wb') as W:
        W.write(response.read())


# In[8]:


target_page = 'http://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/regression/cadata'
cadata=load_svmlight_file(urllib.request.urlopen(target_page))
pickle.dump(cadata,open('cadata.pickle', 'wb'))


# In[10]:


covertype_dataset = fetch_covtype(random_state=101, shuffle=True)
pickle.dump(covertype_dataset,open('covertype_dataset.pickle', 'wb'))


# In[12]:


news_groups_dataset = fetch_20newsgroups(shuffle=True, remove=('readers','footers','quotes'), random_state=6)
pickle.dump(news_groups_dataset, open('news_groups_dataset.pickle','wb'))


# In[ ]:




