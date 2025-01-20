#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


# 计算ppp中的距离
def cal_ppp_distance(pos1, pos2, box_size):
    # 计算两个位置之间的最小距离，考虑周期性边界条件
    pos1,pos2,box_size = np.array(pos1),np.array(pos2),np.array(box_size)
    # 计算位置差矢量
    delta = pos2 - pos1
    
    # 应用最小图像约束，确保距离在周期内最短
    delta = delta - np.round(delta / box_size) * box_size
    # 计算距离
    distance = np.linalg.norm(delta)
    if distance<1e-4:
        distance = float('inf')
    return distance


# In[ ]:




