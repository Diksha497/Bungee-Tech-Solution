#!/usr/bin/env python
# coding: utf-8

# In[147]:


import sqlite3
import pandas as pd
from pandas import DataFrame


# In[149]:


data = pd.read_csv (r'input//main.csv')


# In[150]:


data.head()


# In[151]:


filter_count=data[data.COUNTRY.str.startswith('USA')].reset_index().drop('index',axis=1)
filter_count


# In[152]:


filter_count.to_csv('filteredCountry.csv') 


# In[153]:


data = pd.read_csv (r'filteredCountry.csv')


# In[158]:


# cleaning the data and doing type conversion of price column from objrct to float
data['PRICE_NUM']= data['PRICE'].apply(lambda x : x[1:x.find('.')+2])
data['PRICE_NUM']= data['PRICE_NUM'].replace('[,\?�]+','',regex=True)

data['PRICE_NUM'] = pd.to_numeric(data['PRICE_NUM'])
data


# In[155]:


grp_data = pd.DataFrame(data.groupby('SKU')['PRICE_NUM'].nsmallest(2)).reset_index().drop('level_1', axis=1)
grp_data['rank'] = grp_data.groupby('SKU').rank(method="first", ascending=True)
pivot_data = grp_data.pivot('SKU', columns='rank',values='PRICE_NUM').reset_index()


# In[156]:


pivot_data.columns= ['SKU', 'First_Min_Price', 'Second_Min_Price']
pivot_data


# In[157]:


pivot_data.to_csv('LowestPrice.csv') 


# In[ ]:




