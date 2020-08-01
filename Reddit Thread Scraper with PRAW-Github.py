#!/usr/bin/env python
# coding: utf-8

# # Fill in your information

# In[89]:


import praw
reddit = praw.Reddit(
    client_id = 'yourclientid',
    client_secret = 'yourclientsecret',
    user_agent = 'yourname',
    username = 'yourusername',
    password = 'yourpassword')


# # Required Packages

# In[90]:


import pandas as pd


# In[91]:


import datetime as dt


# # Scraping Top Posts from Reddit Subthreads

# In[104]:


posts = []


# In[173]:


subreddit = reddit.subreddit('name of the subthread')


# In[174]:


top_subreddit = subreddit.top(limit=1000)


# In[175]:


topics_dict = { "title":[],"score":[],"id":[],"url":[],"comms_num": [],"created": [],"body":[]}


# In[176]:


for submission in subreddit.top(limit = 1000):
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)


# # Format as the dataframe 

# In[177]:


topics_data = pd.DataFrame(topics_dict)


# In[178]:


topics_data


# # Change Timestamp

# In[179]:


def get_date(created):
    return dt.datetime.fromtimestamp(created)


# In[180]:


_timestamp = topics_data["created"].apply(get_date)


# In[181]:


topics_data = topics_data.assign(timestamp = _timestamp)


# In[182]:


topics_data


# # Save it as a CSV File

# In[183]:


topics_data.to_csv('C:/your path/filename.csv', index=False) 


# In[ ]:




