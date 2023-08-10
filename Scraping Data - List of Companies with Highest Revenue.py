#!/usr/bin/env python
# coding: utf-8

# In[3]:


from bs4 import BeautifulSoup
import requests


# In[4]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')


# In[5]:


print(soup)


# In[6]:


soup.find('table', class_ = 'wikitable sortable')


# In[7]:


soup.find('table')


# In[8]:


<table class="wikitable sortable jquery-tablesorter">
<caption>


# In[13]:


table = soup.find_all('table')[1]
table()


# In[10]:


world_titles = table.find_all('th')

world_titles


# In[47]:


world_table_titles = [titles.text.strip() for titles in world_titles]

print(world_table_titles)


# In[51]:


import pandas as pd


# In[55]:


df = pd.DataFrame(columns = world_table_titles)

df


# In[60]:


columns_data = table.find_all('tr')


# In[62]:


for row in columns_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data


# In[63]:


df


# In[65]:


df.to_csv(r'C:\Users\Arfan\Documents\Largest Companies\Companies.csv', index = False)


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





# In[ ]:





# In[ ]:





# In[ ]:




