#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
categotical_feature = pd.Series(['sunny','cloudy', 'snowy', 'rainy', 'foggy'])
mapping = pd.get_dummies(categotical_feature)
mapping


# In[11]:


### Same thing but with sklearn
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
le = LabelEncoder()
ohe = OneHotEncoder()
levels = ['sunny', 'cloudy', 'snowy', 'rainy', 'foggy']
fit_levels = le.fit_transform(levels)
levels_transformed = [ [level] for level in fit_levels]
ohe.fit(levels_transformed)
print(levels_transformed)
print(ohe.transform([le.transform(['sunny'])]).toarray())
print(ohe.transform([le.transform(['cloudy'])]).toarray())


# In[12]:


### Text data
from sklearn.datasets import fetch_20newsgroups
categories = ['sci.med', 'sci.space']
twenty_sci_news = fetch_20newsgroups(categories=categories)


# In[13]:


print(twenty_sci_news.data[0])


# In[15]:


twenty_sci_news.filenames


# In[16]:


### count words
from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
word_count = count_vect.fit_transform(twenty_sci_news.data)
word_count.shape


# In[18]:


print(word_count[0])


# In[20]:


word_list = count_vect.get_feature_names()
for n in word_count[0].indices:
    print("Word: %s. Count: %s" % (word_list[n], word_count[0, n]))


# In[25]:


### Word Frequency
from sklearn.feature_extraction.text import TfidfVectorizer
tf_vect = TfidfVectorizer(use_idf=False, norm='l1')
word_freq = tf_vect.fit_transform(twenty_sci_news.data)
word_list = tf_vect.get_feature_names()
for n in word_freq[0].indices:
    print("Word: %s. Frequency: %0.3f" % (word_list[n], word_freq[0,n]))


# In[28]:


## TFIDF algoritm short for term frequency–inverse document frequency, is a numerical statistic that is intended to reflect how important a 
## word is to a document in a collection or corpus.[1] It is often used as a weighting factor in searches of information 
## retrieval, text mining, and user modeling. The tf–idf value increases proportionally to the number of times a word appears 
## in the document and is offset by the number of documents in the corpus that contain the word, which helps to adjust for the 
##fact that some words appear more frequently in general. Tf–idf is one of the most popular term-weighting schemes today; 83% of text-based recommender systems in digital libraries use tf–idf.[2]

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vect = TfidfVectorizer()
word_tfidf = tfidf_vect.fit_transform(twenty_sci_news.data)
word_list = tfidf_vect.get_feature_names()
for n in word_tfidf[0].indices:
    print("Word: %s. Value tf-idf: %0.3f" % (word_list[n], word_tfidf[0,n])) 


# In[29]:


## TFIDF algoritm  for n-grams
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vect = TfidfVectorizer(ngram_range=(1,3))
word_tfidf = tfidf_vect.fit_transform(twenty_sci_news.data)
word_list = tfidf_vect.get_feature_names()
for n in word_tfidf[0].indices:
    print("Words: %s. Value tf-idf: %0.3f" % (word_list[n], word_tfidf[0,n])) 


# In[ ]:




