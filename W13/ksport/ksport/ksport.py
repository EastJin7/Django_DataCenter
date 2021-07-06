
import xml.etree.ElementTree as ET
#讀取
xml = ET.parse('最近24小時船舶實際進_出港時間ohr134.xml')
root = xml.getroot()
for node in root: #for取出子節點資料
    print(node.get("name")) #取出子節點
    for ship in node: #取出孫節點
        print("船名: " + ship[2].text + "\t" + ship[3].tag +": " + ship[3].text)

#寫入
xml_out = ET.Element('xml_out', Version="1.0") #根節點
for node in root: #子節點
    data = ET.SubElement(xml_out, 'data', name=node.get("name")) 
    for ship_in in node: #孫節點
        ship_out = ET.SubElement(data, 'ship')
        ship_name = ET.SubElement(ship_out, ship_in[2].tag)
        ship_name.text = ship_in[2].text
        ship_time = ET.SubElement(ship_out, ship_in[3].tag)
        ship_time.text = ship_in[3].text
#輸出XML
xml_out = ET.ElementTree(xml_out)
xml_out.write("ShipMoving_out.xml", encoding="utf-8",method="xml" )
