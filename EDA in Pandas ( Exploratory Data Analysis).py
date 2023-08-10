#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[14]:


df = pd.read_csv(r"C:\Users\Arfan\Downloads\world_population.csv")
df


# In[15]:


pd.set_option('display.float_format' , lambda x: '%.2f' % x)
df


# In[16]:


df.info()


# In[17]:


df.describe()


# In[18]:


df.isnull().sum()


# In[19]:


df.nunique()


# In[20]:


df.sort_values(by = '2022 Population' , ascending = False).head(10)


# In[21]:


df.corr()


# In[37]:


sns.heatmap(df.corr(), annot = True)

plt.rcParams["figure.figsize"] = (16,10)
plt.show()


# In[23]:


df


# In[24]:


df.groupby('Continent').mean().sort_values(by = "2022 Population" , ascending = False)


# In[25]:


df[df["Continent"].str.contains("Oceania")]


# In[39]:


df2 = df.groupby('Continent')['1970 Population', '1980 Population', '1990 Population',
       '2000 Population' ,'2010 Population', '2015 Population', '2020 Population','2022 Population'].mean().sort_values(by = "2022 Population" , ascending = False)
df2


# In[29]:


df.columns


# In[40]:


df3 = df2.transpose()
df3


# In[41]:


df3.plot()


# In[53]:


df.boxplot(figsize = (25,15))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




