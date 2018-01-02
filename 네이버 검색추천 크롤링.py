
# coding: utf-8

# In[41]:

import requests
import json


# In[42]:

from ipywidgets import widgets


# In[140]:

from IPython.display import display
text = widgets.Text()
display(text)


# In[133]:

def handle_submit(sender):
    result = requests.get("https://ac.search.naver.com/nx/ac?_callback=window.__jindo_callback._$3361_0&q="+text.value+"&q_enc=UTF-8&st=100&frm=nv&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&ans=2&run=2&rev=4&con=1")
    splited_data = result.content.decode("UTF8").split("window.__jindo_callback._$3361_0(")
    splited_data2 = splited_data[1].split(")")
    json_data = json.loads(splited_data2[0])
    list = json_data['items']
    for x in list[0]:
        print(x[0])


# In[144]:

text.on_submit(handle_submit)

