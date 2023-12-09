#!/usr/bin/env python
# coding: utf-8

# In[26]:


import requests
from bs4 import BeautifulSoup

url = 'https://theresanaiforthat.com/saved/'
html = requests.get(url)

s = BeautifulSoup(html.content, 'html.parser')

results = s.find_all('div', class_='ai_content')

job_title = []
for result in results:
    job = result.find('li', class_='data-name')
    if job:
        job_title.append(job.text)

for job in job_title:
    print(job)


# In[27]:


#Webscrapped data of Saved AI names and no. of saves

Saved_ai = [
    {"name": "StableLM Zephyr 3B", "saves": 16},
    {"name": "Casablanca", "saves": 50},
    {"name": "Beloga", "saves": 96},
    {"name": "AutoDubber", "saves": 232},
    {"name": "VideoDubber", "saves": 382},
    {"name": "ResumeBuild", "saves": 73}
]


# In[28]:


#Sorting the AIs based on "number of saves" in descending order.

Saved_ai = sorted(Saved_ai, key=lambda x: x["saves"], reverse=True)

#printing the final sorted list
for ai in Saved_ai:
    print(f"{ai['name']} - Saves: {ai['saves']}")


# In[29]:


#printing the final sorted list
for ai in Saved_ai:
    print(f"{ai['name']} - Saves: {ai['saves']}")


# In[ ]:




