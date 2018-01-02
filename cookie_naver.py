
# coding: utf-8

# In[1]:

import requests as rq


# In[2]:

address = "http://me.naver.com/index.nhn"
header = {'cookie':"NNB=HQ2LWEYSVLXFM; npic=hRIytk+1G6D0VyNGG1VJtq4kutrHa2QDG1DxN4C32Tm2NUWjdSFnkEcgfdH3fFChCA==; _ga=GA1.2.461330223.1459436013; ASID=cbe552ed00000159222ea56e0000004b; nx_ssl=2; nid_iplevel=1; nid_inf=-1318714469; NID_AUT=Uw1cmKlsyQoKq0PtG0NiFpqQovJFixpUV2O/EoUtBiR+BGkPPrN3N6Pyorumha69; JSESSIONID=D86127E1351539E9AF61CC35D20AC4DB; _MEC_V3=%7C%7C%7C%7C%7C%7C%7Ctrue%7C%7C; NID_SES=AAABUQSe5Y56XA6tpVSNL1MVOZP+LCzIfE6avFtOQOD3SjCDp71xxD2HvXgLkRveefAm+vALba3SSYa6+Yk3zj5JlM+2tm9F2tiJkWePMBADMymjmufoZhdliit33lnPj2sAyRrSSGpc9BFVsa95hTAvpDYPWo6bh+TZtBKeazzkyJDYYxOaFLwih9ZywYM1q+5CCeFAppUbcE5gMurHefWGGNbZZ9Dn9Mxk/JDGCGCsKdS/iGSTXsI0owhFVng133yk0tSGHKdfhHSpqX5f5FyYPBFBYG/jnDaWzSsWqcnsZacgxx9ySlBWeyAJVlVwnHcHdNGT0j1t15/ZMHRHu92aiij3q7t3RFl3ebqRefJtLbdHguDs3hFzhp0z0rc+NH86+V7cB/8HSjAXJmxxy7inS1rZSIxFZmev92iW/IQMKB7NGtV7Qby89ReNMGpP0BhqKZFrNUW8/Xp3U6rCZGvTwTM="}


# In[12]:

r = rq.get(address)


# In[13]:

print(r.content.decode('UTF-8'))

