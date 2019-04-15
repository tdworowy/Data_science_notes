#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.datasets import load_digits
digits = load_digits()
X, Y = digits.data, digits.target

from sklearn import svm
h = svm.SVC()
hp = svm.SVC(probability=True, random_state=1)

from sklearn.model_selection import RandomizedSearchCV


# In[9]:


search_dict = {'kernel': ['linear', 'rbf'], 
               'C':[1, 10, 100, 1000],
              'gamma':[0.01, 0.001, 0.0001]}
scorer = 'accuracy'
search_func = RandomizedSearchCV(estimator=h, param_distributions= search_dict, n_iter=10, scoring=scorer, n_jobs=1,
                                iid=False, refit=True, cv=10, return_train_score=True)
get_ipython().run_line_magic('timeit', 'score = search_func.fit(X, Y)')
print(search_func.best_estimator_)
print(search_func.best_params_)
print(search_func.best_score_)


# In[11]:


search_func.cv_results_ 


# In[ ]:




