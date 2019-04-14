#!/usr/bin/env python
# coding: utf-8

# In[22]:


import networkx as nx


# In[23]:


dump_file_base = "dumped_graph"
def remvoe_file(file_name):
    import os
    if os.path.exists(file_name):
        os.remove(file_name)


# In[24]:


G = nx.krackhardt_kite_graph()


# In[25]:


GML_file = dump_file_base + '.gml'
remvoe_file(GML_file)
nx.write_gml(G, GML_file)
G2 = nx.read_gml(GML_file)
G2_to_int = [(int(node[0]),int(node[1])) for node in G2.edges()]
print ("G1:",G.edges())
print ("G2:",G2_to_int)
assert(list(G.edges()) == G2_to_int)


# In[ ]:




