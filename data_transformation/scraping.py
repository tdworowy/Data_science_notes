#!/usr/bin/env python
# coding: utf-8

# In[1]:


import urllib.request
from bs4 import BeautifulSoup
def get_soup(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    return BeautifulSoup(response, 'html.parser')


# In[2]:


from bs4 import BeautifulSoup
url = 'https://en.wikipedia.org/wiki/William_Shakespeare'
soup = get_soup(url)


# In[3]:


soup.title


# In[4]:


def get_links(soup):
    try:
        section = soup.find_all(id='mw-normal-catlinks')[0]
    except(IndexError):
        return []
        
    links = []
    for catlink in section.find_all('a')[1:]:
        link = catlink.get('href')
        print(catlink.get('title'), '->', link)
        links.append(link)
    return links


# In[7]:


def get(base_links):
    soupes = map(lambda link:get_soup('https://en.wikipedia.org'+link),base_links)
    return map(get_links, soupes)
base_links = get_links(soup)

new_links = get(base_links)
new_links2 = get(new_links)
new_links3 = get(new_links2)
print(list(new_links))
print(list(new_links2))
print(list(new_links3))


# In[ ]:




