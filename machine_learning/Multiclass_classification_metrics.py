#!/usr/bin/env python
# coding: utf-8

# In[3]:


from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
iris = datasets.load_iris()
X_train, X_test, Y_train, Y_test = train_test_split(iris.data, iris.target, test_size=0.50, random_state=4)
classifier = DecisionTreeClassifier(max_depth=2) # low efficiency classifier
classifier.fit(X_train, Y_train)
Y_pred = classifier.predict(X_test)


# In[4]:


# confuxion matrix
from sklearn import metrics
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, Y_pred)
print(cm)


# In[6]:


import matplotlib.pyplot as plt
img = plt.matshow(cm, cmap=plt.cm.autumn)
plt.colorbar(img, fraction=0.045)
for x in range(cm.shape[0]):
    for y in range(cm.shape[1]):
        plt.text(x, y, "%0.2f" % cm[x, y], size=12, color='black', ha='center', va='center')
plt.show()


# In[7]:


# accuracy
metrics.accuracy_score(Y_test, Y_pred)


# In[11]:


# precision 1
metrics.precision_score(Y_test, Y_pred, average='weighted')


# In[12]:


# precision 2
metrics.precision_score(Y_test, Y_pred, average='macro')


# In[13]:


# precision 3
metrics.precision_score(Y_test, Y_pred, average='micro')


# In[17]:


# recall 1
metrics.recall_score(Y_test, Y_pred, average='weighted')


# In[18]:


# recall 2
metrics.recall_score(Y_test, Y_pred, average='macro')


# In[19]:


# recall 3
metrics.recall_score(Y_test, Y_pred, average='micro')


# In[22]:


# f1 1
metrics.f1_score(Y_test, Y_pred, average='weighted')


# In[23]:


# f1 2
metrics.f1_score(Y_test, Y_pred, average='macro')


# In[24]:


# f1 3
metrics.f1_score(Y_test, Y_pred, average='micro')


# In[26]:


from sklearn.metrics import classification_report
print(classification_report(Y_test, Y_pred, target_names=iris.target_names))


# In[ ]:




