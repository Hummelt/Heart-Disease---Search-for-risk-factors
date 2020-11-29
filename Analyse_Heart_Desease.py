#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

data = pd.read_csv("heart.csv")
data.head()


# In[2]:


data.tail()


# In[3]:


data.describe()


# In[4]:


data.info()


# In[6]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')



# In[7]:


from pandas import DataFrame


# In[9]:


sns.distplot(data["age"])


# In[10]:


sns.distplot(data["sex"])
#1 = male; 0 = female


# In[11]:


sns.distplot(data["trestbps"]) 
#resting bloodpressure


# In[13]:


sns.distplot(data["chol"])


# In[14]:


data.corr()


# In[15]:


sns.pairplot(data)


# In[29]:


sns.heatmap(data.corr())


# In[17]:


sns.barplot(x="age", 
           y= "sex",
           data=data)


# In[26]:


from sklearn.model_selection import train_test_split


# In[27]:


x_train, x_test, y_train, y_test = train_test_split(data["age"], data["thalach"], test_size =0.5)
from sklearn.linear_model import LinearRegression
lm = LinearRegression()


# In[ ]:
sns.countplot(x='target',data=data,hue='sex')





# In[ ]:




