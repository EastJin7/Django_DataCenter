#將Excel解析成圖片並重輸出新Excel

import csv
import pandas as pd
pd.set_option("display.max_rows", 2000)    #最大顯示2000 rows
pd.set_option("display.max_columns", 1000) #最大能顯示1000 columns
import numpy as np


from pylab import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']  
# 指定默認字形：解決plot不能顯示中文問題
matplotlib.rcParams['axes.unicode_minus'] = False
import matplotlib.pyplot as plt

from collections import Counter
import os 
import math

df = pd.read_csv('F:\Python\W12\goods\Form.csv')
with open('F:\Python\W12\goods\Form.csv','r') as fin:
    with open('output.csv','w') as fout:
        csvreader = csv.reader(fin)
        csvwriter = csv.writer(fout)
        yearTotal=0
        AllTotal=0
        Amount=len(df)
        mi = Amount/96
        i=1
        y=1
        year=2000+y
        yearList=[]
        totalList=[]
        csvwriter.writerow(['年份','年運量'])
        while(i!=Amount):
            yearTotal+=df.loc[i]['Total']
            if (i%96==0):
                print(str(year)+"年運量 : "+str(yearTotal)+"\n") #debug用
                csvwriter.writerow([str(year),str(yearTotal)])
                yearList.append(year) #+List
                totalList.append(yearTotal)
                AllTotal+=yearTotal
                y+=1
                year=2000+y
                yearTotal=0
            i+=1
        print("全部總運量 : "+ str(AllTotal))
#印圖表
yearList = list(map(int,yearList))
totalList = list(map(int,totalList))
plt.title('臺灣地區國際商港進出港貨物國輪與外輪承運量')
plt.xlabel('年份')
plt.ylabel('年運量')
plt.grid( color='#95a5a6',linestyle='--', linewidth=1 ,axis='y',alpha=0.4)
plt.legend()
plt.plot(yearList,totalList)
plt.show()