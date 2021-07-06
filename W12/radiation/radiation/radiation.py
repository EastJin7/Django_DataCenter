import requests
from bs4 import BeautifulSoup
import csv
from os.path import exists
import time

html = requests.get("https://www.aec.gov.tw/trmc/gammadetect.html")
chromedriver = r"F:\Python\chromedriver.exe" 
bsObj = BeautifulSoup(html.content, "html.parser")
for single_div in bsObj.findAll("div",class_="col-md-4 col-sm-4 col-6 px-1 py-1"):
    cell = single_div.findAll("td")
    station_name = cell[0].find("span").text
    station_value = cell[1].find("span").text
    station_time = cell[2].find("span").text
    station_time = station_time.replace("\n","")
    print("監測站 : "+station_name+"\n監測值 : "+station_value+"\n監測時間 : "+station_time)

    file_name = "全國輻射觀測資料.csv"
    if not exists(file_name):
        data = [['監測站', '監測值','監測時間'], [station_name, station_value, station_time]]
    else:
        data = [[station_name, station_value, station_time]]
    f = open(file_name, "a")
    w = csv.writer(f)
    w.writerows(data)
    print (data)
    f.close()
