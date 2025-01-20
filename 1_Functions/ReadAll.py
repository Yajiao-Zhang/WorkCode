#!/usr/bin/env python
# coding: utf-8

# In[79]:


# 写一个函数，既能够读取xyz，也能够读取lmp文件，然后根据输入读取


# In[80]:


# 自定义的Atom类，在各个类型文件读取中应用
class Atom:
    def __init__(self, atom_id=None, atom_type=None, charge=None, x=None, y=None, z=None, vx=None, vy=None, vz=None, fx=None, fy=None, fz=None, c_Ke_atom=None, c_Pe_atom=None, v_E_total=None):
        self.atom_id = atom_id
        self.atom_type = atom_type
        self.charge = charge
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self.fx = fx
        self.fy = fy
        self.fz = fz
        self.c_Ke_atom = c_Ke_atom
        self.c_Pe_atom = c_Pe_atom
        self.v_E_total = v_E_total
    
    def print_non_default_values(self):
        for attr_name, attr_value in vars(self).items():
            if attr_value is not None:
                print(attr_name, ":", attr_value)
    # 输出所有
    def print_all(self):
        attributes = vars(self)
        for attribute, value in attributes.items():
            print(attribute,' : ', value)
    
    # 更具dic值赋值
    def set_properties(self, properties):
        for key, value in properties.items():
            if hasattr(self, key):
                setattr(self, key, value)


# In[1]:


# # 定义属性类型和对应的值
# properties = {
#     'atom_id': 1,
#     'atom_type': 'H',
#     'charge': 0.5,
#     'x': 0.0,
#     'y': 0.0,
#     'z': 0.0
# }
# atom = Atom()
# # 使用字典赋值给属性
# atom.set_properties(properties)
# # # 创建一个原子对象，提供特定属性值
# # atom1 = Atom(atom_id=1, atom_type=2, x=3.14, v_E_total=10.5)

# # 调用 print_non_default_values() 方法，输出不为默认值的属性信息
# atom.print_non_default_values()


# In[81]:


def read_file(file_path='None',file_type='None',start_frame=0,step_frame=0,end_frame=0,label=0,parameter=[]):
    file_extension = file_path.split('.')[-1].lower()
    # 检查格式
    if file_extension!=file_type:
        raise TypeError("File format error.")
    # 按照类型处理数据
    if file_extension == 'xyz':
        # 处理 xyz 文件格式的读取逻辑
        data = read_xyz_file(file_path,start_frame=start_frame,step_frame=end_frame,end_frame=step_frame)
        return data
    
    elif file_extension == 'lmp':
        # 处理 lmp 文件格式的读取逻辑
        data = read_lmp_file(file_path,start_frame=start_frame,step_frame=step_frame,end_frame=end_frame,label=label,parameter=parameter)
        # print(parameter)
        return data
    
    elif file_extension == 'con':
        # 处理 con 文件格式的读取逻辑
        data = read_con_file(file_path,start_frame=start_frame,step_frame=step_frame,end_frame=step_frame)
        return data
    
    else:
        raise TypeError("Unsupported file format.")


# In[82]:


def read_xyz_file(file_path):
    pass
    # 实现读取 xyz 文件的逻辑
    # 返回读取到的数据
def read_con_file(file_path):
    # 实现读取 con 文件的逻辑
    # 返回读取到的数据
    pass


# In[83]:


# file_path = r'C:\Users\zhang\Desktop\桌面资料\论文\AI_test\lmp_file\1crystal_300k.lmp'


# In[84]:


def read_lmp_file(file_path='None',start_frame=0,step_frame=0,end_frame=0,label=0, parameter=[]):
    # 实现读取 lmp 文件的逻辑
    # 所有信息储存的总列表
    list_all_frames = []
    # 返回读取到的数据
    if label==0:
        print('Origin lmp file will be returned')  
    # 返回读取到的自定义信息 
    elif label==1:
        print('Custom data will be returned:',parameter)
        # 打开文件并读取所有行数据
        with open(file_path, 'r') as file:
            lines = file.readlines()
        # 每一页的原子数
        num_atom =int(lines[3])
        # 定义一页的行数
        lines_per_page = num_atom + 9
        # 定义一行都有哪些属性
        lines_feature = (lines[8].split())[2:]
        # 需要返回的属性的索引
        feature_index = [ index for index, value in enumerate(lines_feature) if value in parameter]
        # print(lines_feature,feature_index)
        # 定义性质的字典
        feature_dic = {}
        # 计算总页数
        total_pages = (len(lines) + lines_per_page - 1) // lines_per_page
        # 遍历每一页

        for frame in range(start_frame,end_frame,step_frame):
            # 每一页的数据存储在这个list中
            list_frame = []
            # 计算当前页的起始行号和结束行号
            start_line = frame * lines_per_page
            end_line = start_line + lines_per_page
            # 从总行数据中获取当前页的行数据
            page_lines = lines[start_line:end_line]
            ## 开始分析每一页中的数据
            #print("Current frame number :",page)
            # 每一页的第九行开始才是原子数据
            for i_atom in page_lines[9:]:
                atom = Atom()
                ii = i_atom.split()
                for i_para,i_index in zip(parameter,feature_index):
                    if i_para=='id':
                        i_para = 'atom_'+ i_para
                        feature_dic[i_para] = int(ii[i_index])
                    elif i_para == 'type':
                        i_para = 'atom_'+ i_para
                        feature_dic[i_para] = ii[i_index]
                    else:
                        feature_dic[i_para] = float(ii[i_index])
                # 设置值
                atom.set_properties(feature_dic)
                list_frame.append(atom)
            list_all_frames.append(list_frame)
        return list_all_frames


# In[73]:


# x = read_lmp_file(file_path=file_path,start_frame=0,step_frame=2,end_frame=10,label=1,parameter= ['id','type','x','y','z'])


# In[74]:


# 定义一个函数能够返回需要的类型是第几个


# In[78]:


# x[2][108].print_all()


# In[ ]:




