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

data = raw_data[1]

country_id = list(data['countries']['id'])
country_name = list(data['countries']['name'])
countries = zip(country_id, country_name)

for country in countries: #印出zip
    temp = Country(name = country[1],country_id=country[0])
    temp.save()
    #print(country)
#c=[
#    {"name" : "格利達尼亞","id":1},
#    {"name" : "利姆薩羅敏薩","id":2},
#    {"name" : "烏爾達哈","id":3}
#    ]
#for country in c:
#    temp = Country(name=country['name'],country_id=country['id'])
#    temp.save()

countries = Country.objects.all()
print(countries)
print("Insert success!")
