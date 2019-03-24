#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings
warnings.filterwarnings("ignore")

from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.utils import np_utils
import numpy as np
from keras import backend as K
K.set_image_dim_ordering('th')


# In[2]:


from keras.datasets import mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()


# In[3]:


num_pixels = X_train.shape[1] * X_train.shape[2]
n_channels = 1 #All picutures are in shades of gray
def preprocess(matrix):
    return matrix.reshape(matrix.shape[0],
                         n_channels,
                         matrix.shape[1],
                         matrix.shape[2]).astype('float32') /255.


# In[4]:


print(X_train.shape)
print(X_train.dtype)
print(np.max(X_train))


# In[5]:


X_train, X_test = preprocess(X_train), preprocess(X_test)


# In[6]:


print(X_train.shape)
print(X_train.dtype)
print(np.max(X_train))


# In[7]:


y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)
num_classes = y_train.shape[1]
print(y_train.shape)
print(y_train.shape[1])


# In[8]:


def basline_model():
    model = Sequential()
    model.add(Flatten(input_shape=(1,28,28)))
    model.add(Dense(num_pixels, activation='relu', kernel_initializer="normal"))
    model.add(Dense(num_classes, activation='softmax', kernel_initializer="normal"))
    model.compile(loss='categorical_crossentropy',optimizer='adam', metrics=['accuracy'])
    return model    


# In[9]:


def convolution_small():
    model = Sequential()
    model.add(Convolution2D(32,5,5,border_mode='valid',input_shape = (1,28,28),activation='relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.2))
    model.add(Flatten())
    model.add(Dense(128,activation='relu'))
    model.add(Dense(num_classes,activation='softmax'))
    model.compile(loss='categorical_crossentropy',optimizer='adam', metrics=['accuracy'])
    return model    


# In[10]:


def convolution_large():
    model = Sequential()
    model.add(Convolution2D(30,5,5, border_mode='valid',input_shape = (1,28,28),activation='relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Convolution2D(15,3,3, activation='relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.2))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(num_classes,activation='softmax'))
    model.compile(loss='categorical_crossentropy',optimizer='adam', metrics=['accuracy'])
    return model


# In[11]:


np.random.seed(101)
models = [('Baseline', basline_model()),
         ('Small', convolution_small()),
         ('Large', convolution_large())]
for name, model in models:
    print("Model: %s" % name)
    model.fit(X_train, y_train, validation_data=(X_test, y_test),
             nb_epoch=10, batch_size=100, verbose=2)
    scores = model.evaluate(X_test, y_test, verbose=0)
    print("Base error: %f" % (100-scores[1]*100))
    print("_"*20)


# In[ ]:




