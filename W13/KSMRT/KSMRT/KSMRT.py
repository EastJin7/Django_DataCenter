import json

with open("4278fc6a-c3ea-4192-8ce0-40f00cdb40dd.json",encoding = 'utf-8') as file:
#for item in data:
    f = json.loads(file.read())
    data = f['data'] #進入第一層
    for item in data:
        print(item['車站編號'])
        print(item['車站中文名稱'])
        print(item['車站緯度'])
        print(item['車站經度'])


file_out = open("ks_out.json", 'w', encoding = 'utf-8')
temp_list = []
for item in data:
    tempDict = {'車站編號': item['車站編號'], '車站中文名稱':item['車站中文名稱'],'車站緯度':item['車站緯度'],'車站經度':item['車站經度']}
    temp_list.append(tempDict)
tempObj = json.dumps(temp_list,ensure_ascii=False) 
file_out.write(tempObj)
file_out.close()

"""
#讀取重輸出的檔案
nfile = open("ks_out.json",encoding = 'utf-8')
data = json.load(nfile)
for item in data:
    print([item['車站編號'], item['車站中文名稱'],item['車站緯度'],item['車站經度']])
nfile.close()
"""