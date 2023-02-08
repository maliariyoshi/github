#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().system('pip install geopandas')
import geopandas as gpd
import pandas as pd


# In[6]:


jpn=gpd.read_file('japan_prefectures.geojson')


# In[7]:


jpn_cult = pd.read_csv('jpn_cultivated.csv')[['id', 'name', '% land']]
jpn_cult.rename(columns = {'% land':'Percentage of Cultivated Land'}, inplace = True)


# In[8]:


jpn_cult_map = pd.merge(jpn, jpn_cult, left_on='id', right_on='id')
jpn_cult_map = jpn_cult_map[['Percentage of Cultivated Land', 'name', 'geometry']]
jpn_cult_map.explore('Percentage of Cultivated Land')


# In[ ]:





# In[ ]:




