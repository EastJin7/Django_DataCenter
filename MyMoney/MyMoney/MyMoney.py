import sys
import math
print("謹慎理財，不要把雞蛋放同個籃子裡\n")
go = int(input("想看幾種股票 ?"))
while go>0:
    print("-------------------------------------")
    inMoney = float(input("預算 : "))
    if inMoney!=0: #輸入0時預算與前面相同
        myMoney=inMoney
    st = float(input("每股金額 : "))
    s = float(input("股票股利 : "))
    n = float(input("現金股利 : "))
    if inMoney!=0: #輸入0時年數與前面相同
        year = int(input("打算放幾年 : "))

    haveStock=0
    haveNT=0
    firstGet=0
    buy=int(myMoney/st)
    buyk=buy/1000

    print("你可以購買{}股，即{:.3f}張（以下從整張計算）".format(buy,buyk))
    haveStock+=int(buy)
    for i in range(1,year+1,1):
        getStock=int(haveStock*s)
        getNT=int(haveStock*n)
        print("第 ",i," 年\n　獲得 ",getStock," 股和 ",getNT," 元現金")
        haveNT=haveNT+getNT
        haveStock=haveStock+getStock
        print("　除權息日後，你持有 ",haveStock," 股\n")
        if (i==1):
            firstStock=getStock
            firstGet=getStock*(st-s)+getNT
    print("首年獲利",int(firstGet),"，在",round((myMoney-firstGet)/(buy+firstStock),2),"元前退場")
    print("最終持有 ",haveStock," 股和 ",haveNT," 現金\n")
    stToMoney=int(haveStock*(st-s))
    print("如果不漲不跌，\n　賣出股票可得",stToMoney,"元")
    print("　總獲利:",stToMoney+haveNT-myMoney,"\n")
    print("如果跌幅很大，需在跌到",round((myMoney-haveNT)/haveStock,2),"元前殺出\n")
    go-=1