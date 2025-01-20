#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# # 这个函数用来读取xyz文件

# In[7]:


file_path = r'C:\Users\zhang\Desktop\桌面资料\论文\AI_test\predict_lmp\pre_file.xyz'
file_type = 'xyz'

# 分析的起始帧、终止帧、以及步长
start_frame = 0
steps_frame = 1
final_frame = 1



# In[10]:


def read_one_frame_xyz(file_path='None',frame=0):
    # 打开文件并读取所有行数据
    with open(file_path, 'r') as file:
        lines = file.readlines()
    # 每一页的原子数
    num_atom =int(lines[0])
    # 定义一页的行数
    lines_per_page = num_atom + 2
    # 计算总页数
    total_pages = (len(lines) + lines_per_page - 1) // lines_per_page

    if frame>total_pages:
        print('Input Error!')
    data = lines[frame*lines_per_page:(frame+1)*lines_per_page]
    ##  去除表头
    data = data[2:]
    ##  先对数据处理一遍
    new_data = []
    max_x,max_y,max_z = 0,0,0
    for atom in data:
        # 转换格式
        atom = atom.split()
        temp_x,temp_y,temp_z = float(atom[1]),float(atom[2]),float(atom[3])
        max_x,max_y,max_z = max(temp_x,max_x),max(temp_y,max_y),max(temp_z,max_z)
        new_data.append([atom[0],temp_x,temp_y,temp_z])
    return new_data


# In[ ]:




