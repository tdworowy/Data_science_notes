#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline, FeatureUnion

X, y = make_classification(n_samples=100, n_features=100,
                           n_informative=5, n_redundant=2, random_state=101)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)

classifier = LogisticRegression(C=0.1, penalty='l1', random_state=101)

# In[2]:


# define parallel steps
from sklearn.decomposition import PCA, KernelPCA
from sklearn.preprocessing import FunctionTransformer


def identity(x):
    return x


def inverse(x):
    return 1.0 / x


paraller = FeatureUnion(transformer_list=[
    ('pca', PCA()),
    ('kernelpca', KernelPCA()),
    ('inverse', FunctionTransformer(inverse, validate=True)),
    ('original', FunctionTransformer(identity, validate=True))], n_jobs=-1)

# In[3]:


# define date pipeline
from sklearn.preprocessing import RobustScaler
from sklearn.linear_model import RandomizedLogisticRegression
from sklearn.feature_selection import RFECV

selector = RandomizedLogisticRegression(n_resampling=300, random_state=101, n_jobs=-1)
pipeline = Pipeline(steps=[('paraller_transformation', paraller),
                           ('random_selection', selector),
                           ('logistic_reg', classifier)])

# In[6]:


# find best combination of parameres
import warnings

warnings.filterwarnings("ignore")

from sklearn.model_selection import GridSearchCV

search_dict = {'logistic_reg__C': [100, 10, 1, 0.1, 0.01],
               'logistic_reg__penalty': ['l1', 'l2']}
search_func = GridSearchCV(estimator=pipeline, param_grid=search_dict, scoring='accuracy', n_jobs=-1,
                           iid=False, refit=True, cv=10)
search_func.fit(X_train, y_train)

# In[8]:


print("BEST ESTIMATOR")
print(search_func.best_estimator_)
print("BEST SCORE")
print(search_func.best_score_)
print("BEST PARAMS")
print(search_func.best_params_)

# In[10]:


# Generate prediction for test (and terin) data 
from sklearn.metrics import classification_report

print("Result for test data:")
print(classification_report(y_test, search_func.predict(X_test)))
print("Result for train data:")
print(classification_report(y_train, search_func.predict(X_train)))

# In[ ]:
