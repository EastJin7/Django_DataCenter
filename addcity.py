#執行後自動取出所有posts內的物件
import os
import django
import pandas as pd
import time
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dataCenter.settings')
django.setup()

from mysite.models import Country, City
url="https://simpleisbetterthancomplex.com/tutorial/2020/01/19/how-to-use-chart-js-with-django.html"
raw_data = pd.read_html(url)
time.sleep(3)

data = raw_data[0]
cities = list()
for i in range(len(data)):
    temp = tuple(data['cities'].iloc[i])
    cities.append(temp)
#print(cities)

for city in cities:
    #先根據country_id內容去找到country表格裡的紀錄
    #再把紀錄放到下面指令的country參數
    tcountry=Country.objects.get(country_id=city[2])
    temp = City(name=city[1], country=tcountry, population=city[3])
    temp.save()
    print(temp)

#0:id 1:name 2:countryid 3:population

cities = City.objects.all()
#print(cities)
print("Insert success!")
