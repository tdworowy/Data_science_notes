#!/usr/bin/env python
# coding: utf-8

# In[1]:


# https://en.wikipedia.org/wiki/Bootstrapping_(statistics) 
# allows data repeat witch might by problematic

import random
def Bootstrap(n, n_iter=3, random_state=None):
    """
    Data generator for cross validation. In each iteration will generate set of indexes(0,n>.
    Returns data sample and list of all omitted indexes
    """
    if random_state:
        random.seed(random_state)
    for j in range(n_iter):
        bs = [random.randint(0, n-1) for i in range(n)]
        out_bs = list({i for i in range(n)} - set(bs))
        yield bs, out_bs

boot = Bootstrap(n=100, n_iter=10, random_state=1)
for train_idx, validation_idx in boot:
    print(train_idx, validation_idx)


# In[ ]:




