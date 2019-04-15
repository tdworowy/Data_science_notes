#!/usr/bin/env python
# coding: utf-8

# In[2]:


#T-distributed Stochastic Neighbor Embedding is a machine learning algorithm for visualization
from sklearn.manifold import TSNE
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
iris = load_iris()
X, y = iris.data, iris.target
X_tsne = TSNE(n_components = 2).fit_transform(X)
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y, alpha=0.8, s=60, marker='o', edgecolors='white')
plt.show()


# In[ ]:




