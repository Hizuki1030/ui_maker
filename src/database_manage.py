import xml.etree.ElementTree as ET

class Database_manage:
    Libray={"m5stack":{"drawLine":"M5.lcd.drawLine","drawRectangle":"M5.Lcd.drawRect","fillRectangle":"M5.Lcd.fillRect","Triangle":"M5.Lcd.drawTriangle","fillTriangle":"M5.Lcd.fillTriangle","drawOval":"M5.Lcd.drawEllipse","fillOval":"M5.Lcd.fillEllipse","text":"M5.Lcd.drawString","image":"M5.Lcd.drawBmpFile"}}
    def __init__(self,Database_pass):
        self.Database_pass=Database_pass

    def export_Database_as_xml(self,components):
        root = ET.Element('root')
        tree = ET.ElementTree(element=root)
        components_element = ET.SubElement(root,"components")


        for id in components.keys():#{id:{"tag":__,"type":__,,,,,,,,,}}
            component=components[id]
            type=component["type"]
            coordinate=[int(x) for x in component["coordinate"]]#float配列をintにキャスト
            print(coordinate)
            coordinate=[str(x) for x in coordinate]#int配列をstrにキャスト
            if(type=="line"):
                ET.SubElement(components_element,type,{"tag":component["tag"], "ID":str(id), "color":component["lineColor"], "x0":coordinate[0], "y0":coordinate[1], "x1":coordinate[2], "y1":coordinate[3], "layer":str(component["layer"])})
                #ET.SubElement(components,"Line",{"tag":"line1", "ID":"001", "color":"black", "x0":"0", "y0":"0", "x1":"0", "y1":"10", "layer":"1"})
            elif(type == "Rectangle" or type =="fillRectangle" or type=="Oval" or type == "fillOval"):
                ET.SubElement(components_element,type,{"tag":component["tag"], "ID":str(id), "color":component["outlineColor"], "x0":coordinate[0], "y0":coordinate[1], "x1":coordinate[2], "y1":coordinate[3], "layer":str(component["layer"])})
            elif(type== "Triangle" or type=="fillTriangle"):
                ET.SubElement(components_element,type,{"tag":component["tag"], "ID":str(id), "color":component["fillColor"], "x0":coordinate[0], "y0":coordinate[1], "x1":coordinate[2], "y1":coordinate[3], "x2":coordinate[4], "y2":coordinate[5], "layer":str(component["layer"])})
            elif(type=="text"):
                ET.SubElement(components_element,type,{"tag":component["tag"], "ID":str(id), "color":component["fillColor"], "x0":coordinate[0], "y0":coordinate[1],"text":component["text"],"layer":str(component["layer"])})
            elif(type == "image"):
                ET.SubElement(components_element,type,{"tag":component["tag"], "ID":str(id), "x0":coordinate[0], "y0":coordinate[1],"image":component["image"],"layer":str(component["layer"])})

        tree.write(self.Database_pass, encoding='utf-8', xml_declaration=True)









    def make_command(self,Libray_name,type,name,color,coordinate_data,layer,string):#coordinateは配列で代入（引数の数が可変にならないようにするため）
        code=[] #
        color=self.colorChange_hex6_to_hex4(color)
        if(type=="drawLine"):
            code.append(layer)
            x0=coordinate_data[0][0]#座標データの呼び出し((x0,y0)(x1,y1),,,,,,,)
            y0=coordinate_data[0][1]
            x1=coordinate_data[1][0]
            y1=coordinate_data[1][1]
            code.append(self.Libray[Libray_name][type]+"("+str(x0)+","+str(y0)+","+str(x1)+","+str(y1)+","+str(color)+");"+"//"+str(name))
        elif(type == "drawRectangle" or type == "fillRectangle" ):
            code.append(layer)
            x0=coordinate_data[0][0]#座標データの呼び出し((x0,y0)(x1,y1),,,,,,,)
            y0=coordinate_data[0][1]
            x1=coordinate_data[1][0]
            y1=coordinate_data[1][1]
            w=int(x1)-int(x0)
            h=int(y1)-int(y0)
            code.append(self.Libray[Libray_name][type]+"("+str(x0)+","+str(y0)+","+str(w)+","+str(h)+","+str(color)+");"+"//"+str(name))
        elif( type == "drawOval" or type == "fillOval"):
            code.append(layer)
            x0=coordinate_data[0][0]#座標データの呼び出し((x0,y0)(x1,y1),,,,,,,)
            y0=coordinate_data[0][1]
            x1=coordinate_data[1][0]
            y1=coordinate_data[1][1]
            rx=(int(x1)-int(x0))/2
            ry=(int(y1)-int(y0))/2
            Xcenter=int(x0)+rx
            Ycenter=int(y0)+ry
            code.append(self.Libray[Libray_name][type]+"("+str(Xcenter)+","+str(Ycenter)+","+str(rx)+","+str(ry)+","+str(color)+");"+"//"+str(name))
        elif(type== "Triangle" or type=="fillTriangle"):
            code.append(layer)
            x0=coordinate_data[0][0]#座標データの呼び出し((x0,y0)(x1,y1),,,,,,,)
            y0=coordinate_data[0][1]
            x1=coordinate_data[1][0]
            y1=coordinate_data[1][1]
            x2=coordinate_data[2][0]
            y2=coordinate_data[2][1]
            code.append(self.Libray[Libray_name][type]+"("+str(x0)+","+str(y0)+","+str(x1)+","+str(y1)+","+str(x2)+","+str(y2)+","+str(color)+");"+"//"+str(name))
        elif(type== "text"):
            code.append(layer)
            x0=coordinate_data[0]#座標データの呼び出し((x0,y0)(x1,y1),,,,,,,)
            y0=coordinate_data[1]
            code.append(self.Libray[Libray_name][type]+"("+str(string)+","+str(x0)+","+str(y0)+");"+"//"+str(name))
        elif(type== "image"):
            code.append(layer)
            x0=coordinate_data[0]#座標データの呼び出し((x0,y0)(x1,y1),,,,,,,)
            y0=coordinate_data[1]
            code.append(self.Libray[Libray_name][type]+"("+str(string)+","+str(x0)+","+str(y0)+");"+"//"+str(name))

        return code

    def get_LayerAndcode(self,Libray_name):
        LayerANDcode=[]
        for a in self.element.getiterator("line"):#line要素を参照
            coordinate=[[a.get("x0"),a.get("y0")],[a.get("x1"),a.get("y1")]]
            LayerANDcode.append(self.make_command(Libray_name,"drawLine",a.get("tag"),a.get("color"),coordinate,a.get("layer"),""))

        for a in self.element.getiterator("Rectangle"):#Rectangle要素を参照
            coordinate=[[a.get("x0"),a.get("y0")],[a.get("x1"),a.get("y1")]]
            LayerANDcode.append(self.make_command(Libray_name,"drawRectangle",a.get("tag"),a.get("color"),coordinate,a.get("layer"),""))

        for a in self.element.getiterator("fillRectangle"):#fillRectangle要素を参照
            coordinate=[[a.get("x0"),a.get("y0")],[a.get("x1"),a.get("y1")]]
            LayerANDcode.append(self.make_command(Libray_name,"fillRectangle",a.get("tag"),a.get("color"),coordinate,a.get("layer"),""))

        for a in self.element.getiterator("Oval"):#Rectangle要素を参照
            coordinate=[[a.get("x0"),a.get("y0")],[a.get("x1"),a.get("y1")]]
            LayerANDcode.append(self.make_command(Libray_name,"drawOval",a.get("tag"),a.get("color"),coordinate,a.get("layer"),""))

        for a in self.element.getiterator("fillOval"):#fillRectangle要素を参照
            coordinate=[[a.get("x0"),a.get("y0")],[a.get("x1"),a.get("y1")]]
            LayerANDcode.append(self.make_command(Libray_name,"fillOval",a.get("tag"),a.get("color"),coordinate,a.get("layer"),""))

        for a in self.element.getiterator("Triangle"):#fillRectangle要素を参照
            coordinate=[[a.get("x0"),a.get("y0")],[a.get("x1"),a.get("y1")],[a.get("x2"),a.get("y2")]]
            LayerANDcode.append(self.make_command(Libray_name,"drawTriangle",a.get("tag"),a.get("color"),coordinate,a.get("layer"),""))

        for a in self.element.getiterator("fillTriangle"):#fillRectangle要素を参照
            coordinate=[[a.get("x0"),a.get("y0")],[a.get("x1"),a.get("y1")],[a.get("x2"),a.get("y2")]]
            LayerANDcode.append(self.make_command(Libray_name,"fillTriangle",a.get("tag"),a.get("color"),coordinate,a.get("layer"),""))

        for a in self.element.getiterator("text"):#text要素を参照
            coordinate=[a.get("x0"),a.get("y0")]
            LayerANDcode.append(self.make_command(Libray_name,"text",a.get("tag"),a.get("color"),coordinate,a.get("layer"),a.get("text")))

        for a in self.element.getiterator("image"):#text要素を参照
            coordinate=[a.get("x0"),a.get("y0")]
            LayerANDcode.append(self.make_command(Libray_name,"image",a.get("tag"),None,coordinate,a.get("layer"),a.get("image")))

        return LayerANDcode

    def get_UiCode(self,Libray_name):
        tree = ET.parse(self.Database_pass)
        self.element = tree.getroot()
        LayerANDcode=self.get_LayerAndcode(Libray_name)
        LayerANDcode.sort(reverse=True)
        code=[x[1] for x in LayerANDcode]
        print(LayerANDcode)
        return code

    def colorChange_hex6_to_hex4(self,value):#組み込み向けのディスプレイを16進数を4桁で指定するがtkinterでは6桁で指定するのでカラーコードの変換が必要
        value = value.lstrip('#')
        print("value",value)
        lv = len(value)
        RGB=tuple(int(value[i:i + lv // 3],base=16) for i in range(0, lv, lv // 3))#(x,x,x)
        red=int(RGB[0])
        green = int(RGB[1])
        blue= int(RGB[2])
        hex4= hex(((red>>3)<<11) | ((green>>2)<<5) | (blue>>3))
        return hex4
