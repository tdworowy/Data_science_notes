#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sklearn.datasets import load_digits
digits = load_digits()
print(digits.DESCR)
x = digits.data
y = digits.target


# In[3]:


x[0]


# In[10]:


# hypotheses
from sklearn import svm
h1 = svm.LinearSVC(C=1.0)
h2 = svm.SVC(kernel='rbf', degree=3, gamma=0.001, C=1.0)# classifier with a radial base function
h3 = svm.SVC(kernel='poly', degree=3,gamma='auto', C=1.0) # third degree polynomial classifier


# In[6]:


h1.fit(x, y)
print(h1.score(x, y)) # the effectiveness of the algorithm, tested for the same data as was trained


# In[7]:


h2.fit(x, y)
print(h2.score(x, y)) # the effectiveness of the algorithm, tested for the same data as was trained


# In[11]:


h3.fit(x, y)
print(h3.score(x, y)) # the effectiveness of the algorithm, tested for the same data as was trained


# In[14]:


from sklearn.model_selection import train_test_split
random_state = 1
X_train, X_test, Y_train, Y_test = train_test_split(x,y, 
                                                    test_size=0.30, 
                                                    random_state = random_state) # 30% data is Test set, 70% traing set
h1.fit(X_train, Y_train) 
print(h1.score(X_test, Y_test))

h2.fit(X_train, Y_train)
print(h2.score(X_test, Y_test))

h3.fit(X_train, Y_train)
print(h3.score(X_test, Y_test))


# In[17]:


from sklearn.model_selection import train_test_split
random_state = 1
X_train, X_validation_test, Y_train, Y_validation_test = train_test_split(x,y, 
                                                                        test_size=0.40, 
                                                                        random_state = random_state)

X_validation, X_test, Y_validation, Y_test = train_test_split(X_validation_test,Y_validation_test, 
                                                             test_size=0.50, 
                                                             random_state = random_state)

for hypothesis in [h1, h2, h3]:
    hypothesis.fit(X_train, Y_train)
    print ("%s\n -> average effectiveness at the validation stage = %s" %
           (hypothesis, hypothesis.score(X_validation, Y_validation)))
    print ("%s\n -> average effectiveness at the test stage = %s" %
           (hypothesis, hypothesis.score(X_test, Y_test)))


# In[ ]:




