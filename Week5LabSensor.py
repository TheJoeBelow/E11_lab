#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import math
import pandas as pd
# This line allows plots to show in the Jupyter notebook
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import io
import requests


# In[2]:


data = pd.read_csv('sensor_data.csv')


# In[3]:


#print(data)


# In[4]:


temp_data = data.loc[:,"Temperature":"Time"]
print(temp_data)


# In[5]:


plt.plot(temp_data['Temperature'])
plt.ylabel('Temperature (C)') # label the y-axis
plt.xlabel('Time (s)')
plt.title("CPM vs index")                                  # put a title!
plt.show()


# In[6]:


plt.plot(temp_data['Humidity'])
plt.ylabel('Humidity (gH20/kg air)') # label the y-axis
plt.xlabel('Time (s)')
plt.title("CPM vs index")                                  # put a title!
plt.show()


# In[7]:


plt.plot(temp_data['Pressure'])
plt.ylabel('Pressure (hPa)')
plt.xlabel('Time (s)')
plt.title("CPM vs index")                                  
plt.show()

