#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import networkx as nx


# In[2]:


G = nx.Graph()
G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(3,1)
G.add_edge(3,4)
G.add_edge(4,1)
G.add_edge(4,2)
nx.draw_networkx(G)
plt.show()


# In[3]:


G = nx.Graph()
G.add_edges_from([(1,2), (2,3),(3,4), (4,1), (5,4)])
nx.draw_networkx(G)
plt.show()


# In[6]:


k = nx.fast_gnp_random_graph(15,0.40)
nx.draw_networkx(k)
plt.show()


# In[8]:


G = nx.krackhardt_kite_graph()
nx.draw_networkx(G)
plt.show()


# In[10]:


print(nx.has_path(G, source=1, target=9))
print(nx.shortest_path(G, source=1, target=9))
print(nx.shortest_path_length(G, source=1, target=9))


# In[14]:


all_paths = list(nx.shortest_simple_paths(G, source=1, target=9))
for path in all_paths:
    print(path)


# In[11]:


paths = nx.all_pairs_shortest_path(G)
for path in paths:
    print(path)


# In[14]:


import community.community_louvain as community
#print(dir(community))
G = nx.powerlaw_cluster_graph(100, 1, .4, seed=101)
partition = community.best_partition(G)
for i in set(partition.values()):
    print("Society ",i)
    members = list_nodes = [nodes for nodes in partition.keys() if partition[nodes] ==1]
    print(members)
values = [partition.get(node) for node in G.nodes()]
nx.draw_spring(G, cmap=plt.get_cmap('jet'), node_color=values, node_size=30, with_labes=False)
plt.show()
print("Level of modularity: ", community.modularity(partition, G))


# In[ ]:




