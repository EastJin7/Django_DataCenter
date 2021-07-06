import requests
from bs4 import BeautifulSoup
import csv
import urllib3
urllib3.disable_warnings() #不要HTTPS警告
url = 'https://isin.twse.com.tw/isin/C_public.jsp?strMode=2'
html = requests.get("https://isin.twse.com.tw/isin/C_public.jsp?strMode=2", verify = False)
import pandas as pd
"""
import re

df = pd.read_html(html.text)[0]
df.columns = df.iloc[0]
df = df.iloc[1:]
#df = df.drop('備註', axis=1)
df = df.reset_index(drop=True)
new_df = df['有價證券代號及名稱'].str.replace(u'\u3000',' ').str.split(u' ',expand=True)
#new_df.columns = ['有價證券代號', '有價證券名稱','產業別','市場別','上市日']
print(new_df)
"""
columns = ['dtype', 'code', 'name', '國際證券辨識號碼', '上市日', '市場別', '產業別', 'CFI']

bsObj = BeautifulSoup(html.text, 'lxml') 
table = bsObj.find("table", {"class" : "h4"})
items = []
for tr in table.findAll("tr"):
    if tr('b'):
        dtype = tr.text.strip()
    else:
        for td in tr.findAll("td"):
            row = td.text.strip()
            code, name = row[0].replace('\u3000','|').split(u'|')
            items.append(dict(zip(columns, [dtype, code, name, *row[1: -1]])))

data = pd.DataFrame(items)
print(data)





#for tr in table.findAll("tr"):

    #print(tr.contents[0])
#    for td in tr.findAll('td')[8:]:
#        print(td)
    #print (tr.findAll("td").contents[0])
    #.replace('\u3000',' ').split(u' ')

    #if len(data) == 1: #title
    #    pass
    #else:
        #data.append(tr.findAll("td")[1].contents[0].replace('\u3000',' ').split(u' '))

    #if len(data) ==0:
        #data.append(td.text.strip().replace('\u3000',''))
        
    #else:
            #print(data)