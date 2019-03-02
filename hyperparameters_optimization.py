#!/usr/bin/env python
# coding: utf-8

# In[5]:


from sklearn.datasets import load_digits
digits = load_digits()
X, Y = digits.data, digits.target

from sklearn import svm
h = svm.SVC()
hp = svm.SVC(probability=True, random_state=1)


# In[7]:


from sklearn.model_selection import GridSearchCV
search_grid = [
    {'C': [1, 10, 100, 1000], 'kernel':['linear']},
    {'C': [1, 10, 100, 1000], 'gamma': [0.001, 0.0001], 'kernel':['rbf'] },
]
socrer = 'accuracy'


# In[8]:


search_func = GridSearchCV(estimator=h, param_grid=search_grid, scoring=socrer, n_jobs=-1, iid=False, refit=True, cv=10)
get_ipython().run_line_magic('timeit', 'search_func.fit(X, Y)')
print(search_func.best_estimator_)
print(search_func.best_params_)
print(search_func.best_score_)


# In[9]:


search_func = GridSearchCV(estimator=hp, param_grid=search_grid, scoring=socrer, n_jobs=-1, iid=False, refit=True, cv=10)
get_ipython().run_line_magic('timeit', 'search_func.fit(X, Y)')
print(search_func.best_estimator_)
print(search_func.best_params_)
print(search_func.best_score_)


# In[11]:


# scorrer f1_weighted
search_func = GridSearchCV(estimator=h, param_grid=search_grid, scoring="f1_weighted", n_jobs=-1, iid=False, refit=True, cv=10)
get_ipython().run_line_magic('timeit', 'search_func.fit(X, Y)')
print(search_func.best_estimator_)
print(search_func.best_params_)
print(search_func.best_score_)


# In[ ]:




