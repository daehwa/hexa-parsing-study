
# coding: utf-8

# In[18]:

import requests as rq
from IPython.display import Image


# In[9]:

r = rq.get("https://clients1.google.com/complete/search?q=g&client=translate-web&ds=translate&hl=de&requiredfields=tl%3Ako&callback=_callbacks____0j7945lst")


# In[10]:

r.content


# In[32]:

r1 = rq.get("https://ssl.gstatic.com/images/icons/material/system/1x/share_black_18dp.png")
Image(r1.content)


# In[33]:

r1.content


# In[34]:

ggg = rq.get("http://bus.hexa.pro/bus/res/jm/images/ajax-loader.gif")
Image(ggg.content)


# In[35]:

ggg.content


# In[20]:


r2 = rq.get("https://portal.unist.ac.kr/unist_logon/layout/topImages/fall/bg_index04.jpg")
Image(r2.content)


# In[30]:

r3 = rq.get("https://unist.in/misc/cafeteria/")
r3.content.decode("UTF8")


# In[43]:

bus = rq.get("http://bus.hexa.pro/bus/get_ajax_inf.php?way=0")

