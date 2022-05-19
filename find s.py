#!/usr/bin/env python
# coding: utf-8

# In[29]:


import pandas as pd
import numpy as np


# In[32]:


data = pd.read_csv('play.csv')
data
c = np.array(data)[:,:-1]
c


# In[33]:


t = np.array(data)[:,-1]
t


# In[35]:


def train(c, t):
    for i, val in enumerate(t):
        if val == 'yes':
            spec = c[i].copy()
            break
            
    for i, val in enumerate(c):
        if t[i] == 'yes':
            for x in range(len(spec)):
                if val[x] != spec[x]:
                    spec[x] = '?'
                else:
                    pass
            print(spec)

print(train(c, t))


# In[ ]:




