#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


# In[2]:


x = np.linspace(0,5,50)
y_cos = np.cos(x)
y_sin = np.sin(x)
y_tan = np.tan(x)


# In[3]:


plt.figure()
plt.plot(x, y_cos)
plt.plot(x, y_sin)
plt.xlabel('X')
plt.ylabel('Y')
plt.title("TITLE")
plt.show()


# In[4]:


plt.figure()
plt.plot(x, y_tan)
plt.xlabel('X')
plt.ylabel('Y')
plt.title("TITLE")
plt.show()


# In[5]:


plt.subplot(1,2,1)
plt.plot(x,y_cos,'r--')
plt.title('cos')
plt.subplot(1,2,2)
plt.plot(x,y_sin,'b-')
plt.title('sin')
plt.show()


# In[6]:


from sklearn.datasets import make_blobs
D = make_blobs(n_samples=100,n_features=2, centers=3, random_state=7)
groups = D[1]
coordinates = D[0]
plt.plot(coordinates[groups==0,0],coordinates[groups==0,1],'ys',label="Group 0")
plt.plot(coordinates[groups==1,0],coordinates[groups==1,1],'m*',label="Group 1")
plt.plot(coordinates[groups==2,0],coordinates[groups==2,1],'rD',label="Group 2")
plt.ylim(-2,10)
plt.xlim(-15,15)
plt.yticks([10,6,2,-2])
plt.xticks([-15,-5,5,-15])
plt.grid()
plt.annotate("Squares",(-12,2.5))
plt.annotate("Stars",(0,6))
plt.annotate("Diamonds",(10,3))
plt.legend(loc='lower left',numpoints=1)
plt.show()


# In[7]:


x = np.random.normal(loc=0.0,scale=1.0, size=500)
z = np.random.normal(loc=3.0,scale=1.0, size=500)
plt.hist(np.column_stack((x,z)),bins=20,histtype='bar',color=['c','b'], stacked=True)
plt.grid()
plt.show()


# In[8]:


plt.hist(np.column_stack((x,z)),bins=20,histtype='step',color=['c','b'], stacked=False)
plt.grid()
plt.show()


# In[9]:


plt.hist(np.column_stack((x,z)),bins=20,histtype='bar',color=['c','b'], stacked=False)
plt.grid()
plt.show()


# In[10]:


plt.hist(np.column_stack((x,z)),bins=20,histtype='step',color=['c','b'], stacked=True)
plt.grid()
plt.show()


# In[ ]:




