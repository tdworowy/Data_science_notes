#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
from bokeh.plotting import figure, output_notebook, reset_output, show

reset_output()
output_notebook()
x = np.linspace(0,5,50)
y_cos = np.cos(x)
p = figure()
p.line(x, y_cos, line_width=2)
show(p)


# In[ ]:




