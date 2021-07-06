#抓取台銀匯率資訊
import requests
from bs4 import BeautifulSoup
html = requests.get("https://rate.bot.com.tw/xrt/quote/l6m/USD")
bsObj = BeautifulSoup(html.content, "lxml")

def noLine(s):#消除多餘空行
    s = s.replace("\r","")
    s = s.replace("\n","")
    s = s.replace(" ","")
    return s

for single_tr in bsObj.find("table", {"title":"歷史本行營業時間牌告匯率"}).find("tbody").findAll("tr"):
    time = noLine(single_tr.findAll("a")[0].contents[0])
    print("掛牌日期 : "+time)
    cashBuy = noLine(single_tr.findAll("td")[2].contents[0] )
    print("現金買入 : "+cashBuy)
    cashSell = noLine(single_tr.findAll("td")[3].contents[0] )
    print("現金賣出 : "+cashSell)