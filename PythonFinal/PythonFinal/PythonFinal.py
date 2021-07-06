import csv
import pandas as pd
pd.set_option("display.max_rows", 5000)    #最大顯示5000 rows
pd.set_option("display.max_columns", 10000) #最大能顯示10000 columns
import numpy as np

from pylab import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 指定默認字形：解決plot不能顯示中文問題
matplotlib.rcParams['axes.unicode_minus'] = False
import matplotlib.pyplot as plt

df = pd.read_csv('F:\Python\PythonFinal\Form.csv')

def getDF(i,t):
    x = df.iat[i-1,t]
    for j in range(0,7):
        x += df.iat[i+181+j*180,t]
    return x
with open('F:\Python\W12\goods\Form.csv','r') as fin:
    with open('output.csv','w') as fout:
        csvreader = csv.reader(fin)
        csvwriter = csv.writer(fout)
        AllTotal=0
        yearTotal=0
        ROC=0
        JP=0
        KR=0
        HK=0
        CN=0
        US=0
        UK=0
        """
        VN=0
        TH=0
        MY=0
        SG=0
        PH=0
        KH=0
        ID=0
        IN=0
        SA=0
        KW=0
        PA=0
        BS=0
        HN=0
        VC=0
        AB=0
        AD=0
        BZ=0
        NZ=0
        TL=0
        MC=0
        FR=0
        DE=0
        IT=0
        NL=0
        NO=0
        DK=0
        PT=0
        GR=0
        CY=0
        MT=0
        OT=0
        """
        Amount=len(df)
        mi = Amount/12
        i=1
        y=1
        year=2000+y
        yearList=[]
        totalList=[]
        ROCList=[]
        JPList=[]
        KRList=[]
        HKList=[]
        CNList=[]
        USList=[]
        UKList=[]
        """
        VNList=[]
        THList=[]
        MYList=[]
        SGList=[]
        PHList=[]
        KHList=[]
        IDList=[]
        INList=[]
        SAList=[]
        KWList=[]
        PAList=[]
        BSList=[]
        HNList=[]
        VCList=[]
        ABList=[]
        ADList=[]
        BZList=[]
        NZList=[]
        TLList=[]
        MCList=[]
        FRList=[]
        DEList=[]
        ITList=[]
        NLList=[]
        NOList=[]
        DKList=[]
        PTList=[]
        GRList=[]
        CYList=[]
        MTList=[]
        OTList=[]
        """
        csvwriter.writerow(['年份','中華民國','日本','韓國','香港','中國','美國','英國'])
        #csvwriter.writerow(['年份','中華民國','日本','韓國','香港','中國','越南','泰國','馬來西亞','新加坡','菲律賓','柬埔寨','印尼','印度','沙烏地阿拉伯','科威特','賴比瑞亞','美國','巴拿馬','巴哈馬','宏都拉斯','聖文森','安地瓜巴布達','安地卡','貝里斯','紐西蘭','吐瓦魯','馬紹爾群島','法國','德國','義大利','荷蘭','英國','挪威','丹麥','葡萄牙','希臘','塞浦路斯','馬爾他','其他國籍'])
        a=180
        while(i<=180):
            ROC = getDF(i,5)
            JP = getDF(i,7)
            KR = getDF(i,9)
            HK = getDF(i,11)
            CN = getDF(i,13)
            US = getDF(i,35)
            UK = getDF(i,65)
            """
            VN += getDF(i,15)
            TH += getDF(i,17)
            MY += getDF(i,19)
            SG += getDF(i,21)
            PH += getDF(i,23)
            KH += getDF(i,25)
            ID += getDF(i,27)
            IN += getDF(i,29)
            SA += getDF(i,31)
            KW += getDF(i,33)
            PA += getDF(i,37)
            BS += getDF(i,39)
            HN += getDF(i,41)
            VC += getDF(i,43)
            AB += getDF(i,45)
            AD += getDF(i,47)
            BZ += getDF(i,49)
            NZ += getDF(i,51)
            TL += getDF(i,53)
            MC += getDF(i,55)
            FR += getDF(i,57)
            DE += getDF(i,59)
            IT += getDF(i,61)
            NL += getDF(i,63)
            NO += getDF(i,67)
            DK += getDF(i,69)
            PT += getDF(i,71)
            GR += getDF(i,73)
            CY += getDF(i,75)
            MT += getDF(i,77)
            OT += getDF(i,79)
            """
            if (i%12==0):
                #yearTotal = ROC+JP+KR+HK+CN+VN+TH+MY+SG+PH+KH+ID+IN+SA+KW+US+PA+BS+HN+VC+AB+AD+BZ+NZ+TL+MC+FR+DE+IT+NL+UK+NO+DK+PT+GR+CY+MT+OT
                csvwriter.writerow([str(year),str(ROC),str(JP),str(KR),str(HK),str(CN),str(US),str(UK)])
                #csvwriter.writerow([str(year),str(ROC),str(JP),str(KR),str(HK),str(CN),str(VN),str(TH),str(MY),str(SG),str(PH),str(KH),str(ID),str(IN),str(SA),str(KW),
                #                    str(US),str(PA),str(BS),str(HN),str(VC),str(AB),str(AD),str(BZ),str(NZ),str(TL),str(MC),str(FR),str(DE),str(IT),str(NL),str(UK),
                #                    str(NO),str(DK),str(DK),str(PT),str(GR),str(CY),str(MT),str(OT)])
                yearList.append(year) #+List
                ROCList.append(ROC)
                JPList.append(JP)
                KRList.append(KR)
                HKList.append(HK)
                CNList.append(CN)
                USList.append(US)
                UKList.append(UK)
                """
                VNList.append(VN)
                THList.append(TH)
                MYList.append(MY)
                SGList.append(SG)
                PHList.append(PH)
                KHList.append(KH)
                IDList.append(ID)
                INList.append(IN)
                SAList.append(SA)
                KWList.append(KW)
                PAList.append(PA)
                BSList.append(BS)
                HNList.append(HN)
                VCList.append(VC)
                ABList.append(AB)
                ADList.append(AD)
                BZList.append(BZ)
                NZList.append(NZ)
                TLList.append(TL)
                MCList.append(MC)
                FRList.append(FR)
                DEList.append(DE)
                ITList.append(IT)
                NLList.append(NL)
                NOList.append(NO)
                DKList.append(DK)
                PTList.append(PT)
                GRList.append(GR)
                CYList.append(CY)
                MTList.append(MT)
                OTList.append(OT)
                """
                #totalList.append(yearTotal)
                #AllTotal+=yearTotal
                y+=1
                year=2000+y
                yearTotal=0
                ROC=0
                JP=0
                KR=0
                HK=0
                CN=0
                US=0
                UK=0
                """
                VN=0
                TH=0
                MY=0
                SG=0
                PH=0
                KH=0
                ID=0
                IN=0
                SA=0
                KW=0
                PA=0
                BS=0
                HN=0
                VC=0
                AB=0
                AD=0
                BZ=0
                NZ=0
                TL=0
                MC=0
                FR=0
                DE=0
                IT=0
                NL=0
                NO=0
                DK=0
                PT=0
                GR=0
                CY=0
                MT=0
                OT=0
                """
            i+=1
        #print("全部總運量 : "+ str(AllTotal))
#印圖表
yearList = list(map(int,yearList))
ROCList = list(map(int,ROCList))
JPList = list(map(int,JPList))
KRList = list(map(int,KRList))
HKList = list(map(int,HKList))
CNList = list(map(int,CNList))
USList = list(map(int,USList))
UKList = list(map(int,UKList))
plt.title('我國2001年-2015年間進港船舶總運量（主要貿易國）')
plt.xlabel('年份')
plt.ylabel('年運量（噸）')
plt.grid( color='#95a5a6',linestyle='--', linewidth=1 ,axis='y',alpha=0.4)
plt.plot(yearList,ROCList,label='我國')
plt.plot(yearList,JPList,label='日本')
plt.plot(yearList,KRList,label='韓國')
plt.plot(yearList,HKList,label='香港')
plt.plot(yearList,CNList,label='中國')
plt.plot(yearList,USList,label='美國')
plt.plot(yearList,UKList,label='英國')
plt.legend()
plt.show()