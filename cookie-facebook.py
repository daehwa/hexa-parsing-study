
# coding: utf-8

# In[31]:

import requests as rq


# In[38]:

address = "https://www.facebook.com/"

cookie = {'cookie':"sb=k2UbV_gMtVdk34gnBmJQ8WQh; datr=SqjuVkbkIQZnUxsWeHVAFF4z; c_user=100003587245593; xs=20%3AZEq3T2OXs9BaiQ%3A2%3A1491990389%3A20568%3A10139; fr=0h22THlCuRx95Nitg.AWXTn37cIOERPXK0Ljj-hayx9fY.BW7tQo.c6.FnH.0.0.BZy7oh.AWXsGe7g; presence=EDvF3EtimeF1506523742EuserFA21B03587245593A2EstateFDutF1506523742003CEchFDp_5f1B03587245593F3CC; wd=783x710; dpr=1.25"}

#header = {
#   'Accept': "image/gif, image/jpeg, image/pjpeg, application/x-ms-application, application/xaml+xml, application/x-ms-xbap, application/vnd.ms-excel, application/vnd.ms-powerpoint, */*",
#   'Accept-Encoding': "gzip, deflate",
#   'Accept-Language': "ko-KR",
#   'Connection': "Keep-Alive",
#   'Cookie': "PortalAlias=portal; saplb_*=(J2EE5524620)5524650; JSESSIONID=xeF3KIsHUTaCB-GKR1vwbvIsrLzDXgHiS1QA_SAPhSNSu4B7caDYBS7anZbXvBF6; F5_UNIST=1946223626.20480.0000; ume.logon.locale=ko; JSESSIONMARKID=Xwukxg99Qvx2EZ6ZgLl1XJ-Yi5wR4E9Dx0PqpMVAA; _ga=GA1.3.453752370.1458131746; MYSAPSSO2=AjExMDAgABBwb3J0YWw6ZGFlaHdha2ltiAATYmFzaWNhdXRoZW50aWNhdGlvbgEACDIwMTUxMDQ5AgADMDAwAwADVUVQBAAMMjAxNzA5MjcxNDMyBQAEAAAACQoACDIwMTUxMDQ5%2FwEEMIIBAAYJKoZIhvcNAQcCoIHyMIHvAgEBMQswCQYFKw4DAhoFADALBgkqhkiG9w0BBwExgc8wgcwCAQEwIjAdMQwwCgYDVQQDEwNVRVAxDTALBgNVBAsTBEoyRUUCAQAwCQYFKw4DAhoFAKBdMBgGCSqGSIb3DQEJAzELBgkqhkiG9w0BBwEwHAYJKoZIhvcNAQkFMQ8XDTE3MDkyNzE0MzIyNFowIwYJKoZIhvcNAQkEMRYEFPN%2F4rCr168V%2Ft5SSAVaH2P%2FIhaIMAkGByqGSM44BAMELjAsAhQ2njASxq5BdtA3eomzlH2aJyxG2gIUEaM0VZrFg%2FK6s20wuhL3MjUTMzE%3D",
#   'Host': "portal.unist.ac.kr",
#   'User-Agent': "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; APCPMS=^N2015101508102653575433672F8C99B3D73F_5240^; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.2; SMJB)"}


# In[39]:

r = rq.get(address,headers=cookie)


# In[40]:

print(r.content.decode('UTF-8'))

