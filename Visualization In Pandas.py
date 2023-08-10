#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[7]:


df = pd.read_csv(r"C:\Users\Arfan\Downloads\Ice Cream Ratings.csv")
df = df.set_index('Date')
df


# In[49]:


print(plt.style.available)
plt.style.use('classic')


# In[50]:


df.plot(kind = 'line' , title = 'Ice Cream Ratings' , xlabel = 'Daily Ratings' , ylabel = 'Scores')


# In[51]:


df.plot.barh(stacked = True)


# In[27]:


df.plot.scatter(x = 'Texture Rating' , y = 'Overall Rating' , s = 1000 , c = 'Red')


# In[33]:


df.plot.hist(bins = 25)


# In[34]:


df.boxplot()


# In[36]:


df.plot.area(figsize = (10,5))


# In[42]:


df.plot.pie(y = 'Flavor Rating' , figsize = (70,20))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




