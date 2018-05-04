
# coding: utf-8

# ## Interactive Graphs

# First import the various libraries:

# In[1]:


import pandas as pd
import numpy as np
import cufflinks as cf


# In[2]:


from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

#print(__version__) # requires version >= 1.9.0


# In[3]:


# For Notebooks
init_notebook_mode(connected=True)


# In[4]:


# For offline use
cf.go_offline()


# ### Fake Data

# In[5]:


df = pd.DataFrame(np.random.randn(100,4),columns='A B C D'.split())


# In[6]:


#df.head()


# In[7]:


df2 = pd.DataFrame({'Category':['A','B','C'],'Values':[32,43,50]})


# In[8]:


#df2.head()


# ## Using Cufflinks and iplot()
# 
# * scatter
# * bar
# * box
# * spread
# * ratio
# * heatmap
# * surface
# * histogram
# * bubble

# ## Scatter

# In[9]:


df.iplot(kind='scatter',x='A',y='B',mode='markers',size=10)


# ## Bar Plots

# In[10]:


df2.iplot(kind='bar',x='Category',y='Values')


# In[11]:


df.count().iplot(kind='bar')


# ## Boxplots

# In[12]:


df.iplot(kind='box')


# ## 3d Surface

# In[13]:


df3 = pd.DataFrame({'x':[1,2,3,4,5],'y':[10,20,30,20,10],'z':[5,4,3,2,1]})
df3plot = df3.iplot(kind='surface',colorscale='rdylbu')


# ## Spread

# In[14]:


df[['A','B']].iplot(kind='spread')


# ## histogram

# In[15]:


df['A'].iplot(kind='hist',bins=25)


# In[16]:


df.iplot(kind='bubble',x='A',y='B',size='C')


# ## scatter_matrix()
# 
# Similar to sns.pairplot()

# In[17]:


df.scatter_matrix()

