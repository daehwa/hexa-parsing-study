
# coding: utf-8

# In[4]:

import requests as rq
from bs4 import BeautifulSoup as bs


# In[31]:

r = rq.get('http://df.gamebogam.com/item/buqiang.asp')
soup = bs(r.text,"html.parser")
print(r.encoding)

#print(soup.select("table"))
obj = soup.select("table")[2].select("tr")[0].select("td")[0].select("td")
for o in obj:
    print(o.text.encode("ISO-8859-1").decode("utf-8"))


# In[50]:

r = rq.get('https://www.naver.com/')
soup = bs(r.text,"html.parser")
obj = soup.find_all('span', attrs={"class":"ah_k"})
for o in obj :
    print(o.text)


# In[52]:

search_text = "더치페이"
r = rq.get('https://play.google.com/store/search?q='+search_text+'&c=apps&hl=ko')
soup = bs(r.text,"html.parser")
app_names = soup.find_all('a',attrs={"class":"title"})
for app in app_names:
    print(app.text)


# In[55]:

image_name = "고양이"
r = rq.get('https://www.google.co.kr/search?biw=1536&bih=759&tbm=isch&sa=1&q='+image_name+'&oq='+image_name+'&gs_l=psy-ab.3..0l4.2042.2581.0.3070.7.6.0.0.0.0.310.808.2-2j1.3.0....0...1.1j4.64.psy-ab..5.2.596....0.u1qtg3aaBHE')
soup = bs(r.text,"html.parser")
cute_images = soup.find_all('img',attrs={"class":"rg_ic rg_i"})
print(cute_images)


# In[57]:

r = rq.get('http://sksmsskly.blog.me/220998851014')
soup = bs(r.text,"html.parser")
hack_image = soup.find_all('img',attrs={"id":"SEDOC-1493945425145-773224432_image_0_img"})
print(hack_image)

