# coding:utf-8
import xml.etree.ElementTree as ET
import re
tree = ET.parse("components_test.xml")

def make_command(Libray_name,type,name,color,coordinate_data,layer):#coordinateは配列で代入（引数の数が可変にならないようにするため）
    code=[]
    code.append(layer)
    if(type=="drawLine" or type == "drawRectangle" or type == "fillRectangle" ):

        x0=coordinate_data[0][0]
        y0=coordinate_data[0][0]
        x1=coordinate_data[1][0]
        y1=coordinate_data[1][1]
        code.append(Libray[Libray_name][type]+"("+str(x0)+","+str(y0)+","+str(x1)+","+str(y1)+","+str(color)+");"+"//"+str(name))
    return code



element = tree.getroot()
Libray={"m5stack":{"drawLine":"m5.lcd.drawLine","drawRectangle":"M5.Lcd.drawRect","fillRectangle":"M5.Lcd.fillRect"}}
LayerANDcode=[]
for a in element.getiterator("line"):#line要素を参照
    coordinate=[[a.get("x0"),a.get("y0")],[a.get("x1"),a.get("y1")]]
    LayerANDcode.append(make_command("m5stack","drawLine",a.get("name"),a.get("color"),coordinate,a.get("layer")))

for a in element.getiterator("Rectangle"):#Rectangle要素を参照
    coordinate=[[a.get("x0"),a.get("y0")],[a.get("x1"),a.get("y1")]]
    LayerANDcode.append(make_command("m5stack","drawRectangle",a.get("name"),a.get("color"),coordinate,a.get("layer")))

for a in element.getiterator("fillRectangle"):#fillRectangle要素を参照
    coordinate=[[a.get("x0"),a.get("y0")],[a.get("x1"),a.get("y1")]]
    LayerANDcode.append(make_command("m5stack","fillRectangle",a.get("name"),a.get("color"),coordinate,a.get("layer")))



print(sorted(LayerANDcode))
