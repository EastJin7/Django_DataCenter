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
        while(i<=15*12):
            ROC += df.iat[i-1,5]+df.iat[i+181,5]+df.iat[i+361,5]+df.iat[i+541,5]+df.iat[i+721,5]+df.iat[i+901,5]+df.iat[i+1081,5]+df.iat[i+1261,5]
            JP += df.iloc[i-1,7]+df.iat[i+181,7]+df.iat[i+361,7]+df.iat[i+541,7]+df.iat[i+721,7]+df.iat[i+901,7]+df.iat[i+1081,7]+df.iat[i+1261,7]
            KR += df.iloc[i-1,9]+df.iat[i+181,9]+df.iat[i+361,9]+df.iat[i+541,9]+df.iat[i+721,9]+df.iat[i+901,9]+df.iat[i+1081,9]+df.iat[i+1261,9]
            HK += df.iloc[i-1,11]+df.iat[i+181,11]+df.iat[i+361,11]+df.iat[i+541,11]+df.iat[i+721,11]+df.iat[i+901,11]+df.iat[i+1081,11]+df.iat[i+1261,11]
            CN += df.iloc[i-1,13]+df.iat[i+181,13]+df.iat[i+361,13]+df.iat[i+541,13]+df.iat[i+721,13]+df.iat[i+901,13]+df.iat[i+1081,13]+df.iat[i+1261,13]
            US += df.iloc[i-1,35]+df.iat[i+181,35]+df.iat[i+361,35]+df.iat[i+541,35]+df.iat[i+721,35]+df.iat[i+901,35]+df.iat[i+1081,35]+df.iat[i+1261,35]
            UK += df.iloc[i-1,65]+df.iat[i+181,65]+df.iat[i+361,65]+df.iat[i+541,65]+df.iat[i+721,65]+df.iat[i+901,65]+df.iat[i+1081,65]+df.iat[i+1261,65]
            """
            VN += df.iloc[i-1,15]+df.iat[i+181,5]+df.iat[i+361,5]+df.iat[i+541,5]+df.iat[i+721,5]+df.iat[i+901,5]+df.iat[i+1081,5]+df.iat[i+1261,5]
            TH += df.iloc[i-1,17]+df.iat[i+181,5]+df.iat[i+361,5]+df.iat[i+541,5]+df.iat[i+721,5]+df.iat[i+901,5]+df.iat[i+1081,5]+df.iat[i+1261,5]
            MY += df.iloc[i-1,19]+df.iat[i+181,5]+df.iat[i+361,5]+df.iat[i+541,5]+df.iat[i+721,5]+df.iat[i+901,5]+df.iat[i+1081,5]+df.iat[i+1261,5]
            SG += df.iloc[i-1,21]+df.iat[i+181,5]+df.iat[i+361,5]+df.iat[i+541,5]+df.iat[i+721,5]+df.iat[i+901,5]+df.iat[i+1081,5]+df.iat[i+1261,5]
            PH += df.iloc[i-1,23]+df.iat[i+181,5]+df.iat[i+361,5]+df.iat[i+541,5]+df.iat[i+721,5]+df.iat[i+901,5]+df.iat[i+1081,5]+df.iat[i+1261,5]
            KH += df.iloc[i-1,25]+df.iat[i+181,5]+df.iat[i+361,5]+df.iat[i+541,5]+df.iat[i+721,5]+df.iat[i+901,5]+df.iat[i+1081,5]+df.iat[i+1261,5]
            ID += df.iloc[i-1,27]+df.iat[i+181,5]+df.iat[i+361,5]+df.iat[i+541,5]+df.iat[i+721,5]+df.iat[i+901,5]+df.iat[i+1081,5]+df.iat[i+1261,5]
            IN += df.iloc[i-1,29]+df.iat[i+181,5]+df.iat[i+361,5]+df.iat[i+541,5]+df.iat[i+721,5]+df.iat[i+901,5]+df.iat[i+1081,5]+df.iat[i+1261,5]
            SA += df.iloc[i-1,31]+df.iat[i+181,5]+df.iat[i+361,5]+df.iat[i+541,5]+df.iat[i+721,5]+df.iat[i+901,5]+df.iat[i+1081,5]+df.iat[i+1261,5]
            KW += df.iloc[i-1,33]+df.iat[i+181,5]+df.iat[i+361,5]+df.iat[i+541,5]+df.iat[i+721,5]+df.iat[i+901,5]+df.iat[i+1081,5]+df.iat[i+1261,5]
            PA += df.iloc[i-1,37]+df.iat[i+181,5]+df.iat[i+361,5]+df.iat[i+541,5]+df.iat[i+721,5]+df.iat[i+901,5]+df.iat[i+1081,5]+df.iat[i+1261,5]
            BS += df.iloc[i-1,39]+df.iat[i+181,5]+df.iat[i+361,5]+df.iat[i+541,5]+df.iat[i+721,5]+df.iat[i+901,5]+df.iat[i+1081,5]+df.iat[i+1261,5]
            HN += df.iloc[i-1,41]+df.iat[i+181,5]+df.iat[i+361,5]+df.iat[i+541,5]+df.iat[i+721,5]+df.iat[i+901,5]+df.iat[i+1081,5]+df.iat[i+1261,5]
            VC += df.iloc[i-1,43]+df.iat[i+181,5]+df.iat[i+361,5]+df.iat[i+541,5]+df.iat[i+721,5]+df.iat[i+901,5]+df.iat[i+1081,5]+df.iat[i+1261,5]
            AB += df.iloc[i-1,45]+df.iat[i+181,5]+df.iat[i+361,5]+df.iat[i+541,5]+df.iat[i+721,5]+df.iat[i+901,5]+df.iat[i+1081,5]+df.iat[i+1261,5]
            AD += df.iloc[i-1,47]+df.iat[i+181,5]+df.iat[i+361,5]+df.iat[i+541,5]+df.iat[i+721,5]+df.iat[i+901,5]+df.iat[i+1081,5]+df.iat[i+1261,5]
            BZ += df.iloc[i-1,49]+df.iat[i+181,5]+df.iat[i+361,5]+df.iat[i+541,5]+df.iat[i+721,5]+df.iat[i+901,5]+df.iat[i+1081,5]+df.iat[i+1261,5]
            NZ += df.iloc[i-1,51]+df.iat[i+181,5]+df.iat[i+361,5]+df.iat[i+541,5]+df.iat[i+721,5]+df.iat[i+901,5]+df.iat[i+1081,5]+df.iat[i+1261,5]
            TL += df.iloc[i-1,53]+df.iat[i+181,5]+df.iat[i+361,5]+df.iat[i+541,5]+df.iat[i+721,5]+df.iat[i+901,5]+df.iat[i+1081,5]+df.iat[i+1261,5]
            MC += df.iloc[i-1,55]+df.iat[i+181,5]+df.iat[i+361,5]+df.iat[i+541,5]+df.iat[i+721,5]+df.iat[i+901,5]+df.iat[i+1081,5]+df.iat[i+1261,5]
            FR += df.iloc[i-1,57]+df.iat[i+181,57]+df.iat[i+361,57]+df.iat[i+541,57]+df.iat[i+721,57]+df.iat[i+901,57]+df.iat[i+1081,57]+df.iat[i+1261,57]
            DE += df.iloc[i-1,59]+df.iat[i+181,5]+df.iat[i+361,5]+df.iat[i+541,5]+df.iat[i+721,5]+df.iat[i+901,5]+df.iat[i+1081,5]+df.iat[i+1261,5]
            IT += df.iloc[i-1,61]+df.iat[i+181,5]+df.iat[i+361,5]+df.iat[i+541,5]+df.iat[i+721,5]+df.iat[i+901,5]+df.iat[i+1081,5]+df.iat[i+1261,5]
            NL += df.iloc[i-1,63]+df.iat[i+181,5]+df.iat[i+361,5]+df.iat[i+541,5]+df.iat[i+721,5]+df.iat[i+901,5]+df.iat[i+1081,5]+df.iat[i+1261,5]
            NO += df.iloc[i-1,67]+df.iat[i+181,5]+df.iat[i+361,5]+df.iat[i+541,5]+df.iat[i+721,5]+df.iat[i+901,5]+df.iat[i+1081,5]+df.iat[i+1261,5]
            DK += df.iloc[i-1,69]+df.iat[i+181,5]+df.iat[i+361,5]+df.iat[i+541,5]+df.iat[i+721,5]+df.iat[i+901,5]+df.iat[i+1081,5]+df.iat[i+1261,5]
            PT += df.iloc[i-1,71]+df.iat[i+181,5]+df.iat[i+361,5]+df.iat[i+541,5]+df.iat[i+721,5]+df.iat[i+901,5]+df.iat[i+1081,5]+df.iat[i+1261,5]
            GR += df.iloc[i-1,73]+df.iat[i+181,5]+df.iat[i+361,5]+df.iat[i+541,5]+df.iat[i+721,5]+df.iat[i+901,5]+df.iat[i+1081,5]+df.iat[i+1261,5]
            CY += df.iloc[i-1,75]+df.iat[i+181,5]+df.iat[i+361,5]+df.iat[i+541,5]+df.iat[i+721,5]+df.iat[i+901,5]+df.iat[i+1081,5]+df.iat[i+1261,5]
            MT += df.iloc[i-1,77]+df.iat[i+181,5]+df.iat[i+361,5]+df.iat[i+541,5]+df.iat[i+721,5]+df.iat[i+901,5]+df.iat[i+1081,5]+df.iat[i+1261,5]
            OT += df.iloc[i-1,79]+df.iat[i+181,5]+df.iat[i+361,5]+df.iat[i+541,5]+df.iat[i+721,5]+df.iat[i+901,5]+df.iat[i+1081,5]+df.iat[i+1261,5]
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