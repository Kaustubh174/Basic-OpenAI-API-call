#!/usr/bin/env python
# coding: utf-8

# ## Basic Open AI api call

# In[ ]:


get_ipython().system('pip install -q openai')


# In[1]:


import openai
import os


#  #### After installing and importing all the required you need put your api in the section (your api key)

# In[7]:


os.environ['OPENAI_API_KEY'] = 'your api key'
openai.api_key = os.getenv('OPENAI_API_KEY')


# #### After this you need to import the OpenAI Library and set the role of the system and the user
# 
# System is the role you want your api to behave like in our case it is an helpful assistant.
# User role in where you need to set the question you want to be answered

# In[8]:


from openai import OpenAI
client = OpenAI()

    
response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {'role':'system','content':'you are a helpful assistant.'},
        {'role':'user','content':'what is the einstein field equation?'}
    ]
)
##each message has roles. roles=> system, user, assistant
##other agruments are temperature, max tokens

print(response)


# #### The above output is has your required output but you need to change the print command to a where your actual output is

# In[9]:


print(response.choices[0].message.content)


# In[ ]:




