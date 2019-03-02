#!/usr/bin/env python
# coding: utf-8

# In[5]:


from sklearn.datasets import load_boston
boston = load_boston()
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.2, random_state=0)


# In[8]:


from sklearn.linear_model import LinearRegression
regr = LinearRegression()
regr.fit(X_train, y_train)
y_pred = regr.predict(X_test)
from sklearn.metrics import mean_absolute_error
print("MAE: %s" % mean_absolute_error(y_test, y_pred))


# In[9]:


# mesure time
get_ipython().run_line_magic('timeit', 'regr.fit(X_train, y_train)')


# In[12]:


# Plot outputs
import matplotlib.pyplot as plt
plt.figure(figsize=(4, 3))
plt.scatter(y_test, y_pred)
plt.plot([0, 50], [0, 50], '--k')
plt.axis('tight')
plt.xlabel('True price ($1000s)')
plt.ylabel('Predicted price ($1000s)')
plt.tight_layout()


# In[ ]:




