#!/usr/bin/env python
# coding: utf-8

# In[1]:


# outliers values (one dimension)
from sklearn.datasets import load_boston
boston = load_boston()

continuous_variables = [n for n in range(boston.data.shape[1]) if n!=3]
print(continuous_variables)


# In[2]:


import numpy as np
from sklearn import preprocessing
normalize_data = preprocessing.StandardScaler().fit_transform(boston.data[:,continuous_variables])
ouliers_rows, outliter_columns = np.where(np.abs(normalize_data)>3)
print(ouliers_rows)
print(outliter_columns)


# In[3]:


print(list(zip(ouliers_rows, outliter_columns)))


# In[4]:


# EllipticEcvelop distribution
from sklearn.datasets import make_blobs
from sklearn.covariance import EllipticEnvelope
from matplotlib import pyplot as plt
def generate_distribiution(blobs):
    blob = make_blobs(n_samples=100, n_features=2, centers=blobs, cluster_std=1.5, shuffle=True,random_state=5)

    robust_covariance_est = EllipticEnvelope(contamination=.1).fit(blob[0])# contamination -- percentage of outliers
    detection = robust_covariance_est.predict(blob[0])
    outliers = np.where(detection == -1)[0]
    inliers = np.where(detection == 1)[0]

    plt.scatter(blob[0][:,0],blob[0][:,1], c='blue', alpha=0.8, s=60, marker='o', edgecolors='white')
    plt.show()
    return (outliers, inliers, blob)


# In[5]:


# EllipticEcvelop distribution and outliers
def plot_outliers(outliers, inliers, blob):
    in_points = plt.scatter(blob[0][inliers,0], blob[0][inliers,1],
                           c='blue', alpha=0.8, s=60, marker='o', edgecolors='white')
    out_points = plt.scatter(blob[0][outliers,0], blob[0][outliers,1],
                           c='red', alpha=0.8, s=60, marker='o', edgecolors='white')
    plt.legend((in_points,out_points),('Typical','Outliners'),scatterpoints=1, loc='lower right')
    plt.show()


# In[6]:


plot_outliers(*generate_distribiution(1))
plot_outliers(*generate_distribiution(4)) # algorithm doesn't work well for more than one blob (more clasters)
plot_outliers(*generate_distribiution(8)) # it will onlu show outliers data in one, smallest cluster
plot_outliers(*generate_distribiution(24))


# In[11]:


from sklearn.decomposition import PCA
boston = load_boston()
# outliers in boston data 1
continuous_variables = [n for n in range(boston.data.shape[1]) if n!=3]
normalized_data = preprocessing.StandardScaler().fit_transform(boston.data[:,continuous_variables])
pca = PCA(n_components=2)
Zscore_components = pca.fit_transform(normalize_data)
vtot = "The variance explained " + str(round(np.sum(pca.explained_variance_ratio_),3))
v1 =  str(round(np.sum(pca.explained_variance_ratio_[0]),3))
v2 =  str(round(np.sum(pca.explained_variance_ratio_[1]),3))


# In[12]:


# outliers in boston data 2
robust_covariance_est = EllipticEnvelope(store_precision=False, assume_centered = False, contamination=.05)
robust_covariance_est.fit(normalized_data)
detection = robust_covariance_est.predict(normalized_data)
outliers = np.where(detection == -1)
regular = np.where(detection == 1)


# In[13]:


# outliers in boston data 3
# 
from matplotlib import pyplot as plt
in_points = plt.scatter(Zscore_components[regular,0],Zscore_components[regular,1], 
                        color='blue', alpha=0.8, s=60, marker='o', edgecolors='white')
out_points = plt.scatter(Zscore_components[outliers,0],Zscore_components[outliers,1], 
                        color='red', alpha=0.8, s=60, marker='o', edgecolors='white')

plt.legend((in_points,out_points),('Typical','Outliners'),scatterpoints=1, loc='best')
plt.xlabel('First component (%s)' % v1)
plt.ylabel('Second component (%s)' % v2)
plt.xlim([-7,7])
plt.ylim([-6,6])
plt.title(vtot) # EllipticEnvelope only shows outliers data in the one, smallest cluster
plt.show()


# In[ ]:




