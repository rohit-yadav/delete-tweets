
# coding: utf-8

# # Analysing and Deleting Tweets

# ### Asking the right Quesitons
# 
#    * Wordcloud
#    * Number of tweets each month
#    * No of Tweets during the day of the week
#    * No of Tweets during the day - Time during I tweet most
#    * Impressions and profile visit visualization.
#    * All the hash tags I have used so far
#    * Delete all tweets - get user authentication to delete

# In[1]:


# Importing the modules
import time
import urllib
from bs4 import BeautifulSoup
import requests
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


# In[2]:


profile_url = "https://twitter.com/realRohitYadav"
# profile_url = "https://twitter.com/narendramodi"

# Requesting the url
response = requests.get(profile_url)
html = response.text

# Soup object
soup = BeautifulSoup(html, 'html.parser')


# In[3]:


soup.title

