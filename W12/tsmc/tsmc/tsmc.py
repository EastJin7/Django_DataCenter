import docx
import math

wordFile = docx.Document(r'F:\Python\W12\tsmc\tsmc_data.docx')
with open("tsmc_txt.txt", 'w', encoding='utf-8') as wordTxt:
    for para in wordFile.paragraphs:
        data = math.ceil(20/(float(para.text)*0.001425))
        price = float(para.text)*data*0.001425
        print('每股價格 : %5.2f, 每日需購股數 : %3.0f, 手續費 : %5.2f' 
              %(float(para.text), data, price))
        wordTxt.write(str(data)+'\n')