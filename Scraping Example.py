#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json
from bs4 import BeautifulSoup as bs


# In[3]:


url="https://www.rankingthebrands.com/Brand-detail.aspx?brandID="
open("PageScrapingExample.csv","w")
pageID=range(1,11)
for link in pageID:
    r=requests.get(url+str(link))
    
    if(r.status_code!=200):
        print("Link Failed:",link)
        continue
    
    page=r.text
    soup=bs(page,'html.parser')
    
    titleSoup=soup.find_all('div',attrs={'class':'pathLeft'})[0]
    title=titleSoup.find('span').text
    
    award=soup.find_all('div',attrs={'class':'rankingcell01'})
    if len(award)<1:
        continue
    
    yearValue=soup.find_all('div',attrs={'class':'rankingcell02'})
    year=[y for y in yearValue if yearValue.index(y)%2==0]
    rank=[r for r in yearValue if yearValue.index(r)%2==1]
    
    for wards in award:
        i=award.index(wards)
        data=[title,wards.text,year[i].text,rank[i].text]
        print(",".join(data),file=open("PageScrapingExample.csv","a"))


# In[ ]:





# In[ ]:





# In[ ]:




