
# coding: utf-8

# In[110]:

import requests
import json
import re
import ast
from ipywidgets import widgets


from IPython.display import display,clear_output
text = widgets.Text()
display(text)


# In[126]:

def handle_submit(sender):
    clear_output()
    #using json
    #test_string = requests.get("https://ac.search.naver.com/nx/ac?_callback=window.__jindo_callback._$3361_0&q="+text.value+"&q_enc=UTF-8&st=100&frm=nv&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&ans=2&run=2&rev=4&con=1")
    #list = re.findall("\(((?:.|\n)*)\)", test_string.text)
    #json_data = json.loads(list[0])
    #data = json_data['items']
    #for x in data[0]:
    #    print(x[0])

    
    test_string = requests.get("https://ac.search.naver.com/nx/ac?_callback=window.__jindo_callback._$3361_0&q="+text.value+"&q_enc=UTF-8&st=100&frm=nv&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&ans=2&run=2&rev=4&con=1")
    list = re.findall("\[\"(.*?)\"\,", test_string.text)
    for x in list:
        print(x)
    
text.on_submit(handle_submit)

