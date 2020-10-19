import xml.etree.ElementTree as ET

class Database_manage:
    Libray={"m5stack":{"drawLine":"M5.lcd.drawLine","drawRectangle":"M5.Lcd.drawRect","fillRectangle":"M5.Lcd.fillRect","Triangle":"M5.Lcd.drawTriangle","fillTriangle":"M5.Lcd.fillTriangle","drawEllipse":"M5.Lcd.drawEllipse","fillEllipse":"M5.Lcd.fillEllipse","text":"M5.Lcd.drawString","picture":"M5.Lcd.drawBmpFile"}}
    Database_pass=""
    def __init__(self,Database_pass):
        self.Database_pass=Database_pass
        tree = ET.parse(Database_pass)
        self.element = tree.getroot()

    def export_Database_as_xml(self,components):
        root = ET.Element('root')
        tree = ET.ElementTree(element=root)
        components_element = ET.SubElement(root,"components")


        for id in components.keys():#{id:{"tag":__,"type":__,,,,,,,,,}}
            component=components[id]
            type=component["type"]
            coordinate=[str(x) for x in component["coordinate"]]#配列をstrにキャスト
            if(type=="line"):
                ET.SubElement(components_element,type,{"tag":component["tag"], "ID":str(id), "color":component["lineColor"], "x0":coordinate[0], "y0":coordinate[1], "x1":coordinate[2], "y1":coordinate[3], "layer":str(component["layer"])})
                #ET.SubElement(components,"Line",{"tag":"line1", "ID":"001", "color":"black", "x0":"0", "y0":"0", "x1":"0", "y1":"10", "layer":"1"})
        tree.write(self.Database_pass, encoding='utf-8', xml_declaration=True)









    def make_command(self,Libray_name,type,name,color,coordinate_data,layer,string):#coordinateは配列で代入（引数の数が可変にならないようにするため）
        code=[]
        code.append(layer)
        if(type=="drawLine" or type == "drawRectangle" or type == "fillRectangle" or type == "drawEllipse" or type == "fillEllipse"):

            x0=coordinate_data[0][0]
            y0=coordinate_data[0][1]
            x1=coordinate_data[1][0]
            y1=coordinate_data[1][1]
            code.append(self.Libray[Libray_name][type]+"("+str(x0)+","+str(y0)+","+str(x1)+","+str(y1)+","+str(color)+");"+"//"+str(name))
        elif(type== "Triangle" or type=="fillTriangle"):

            x0=coordinate_data[0][0]
            y0=coordinate_data[0][1]
            x1=coordinate_data[1][0]
            y1=coordinate_data[1][1]
            x2=coordinate_data[2][0]
            y2=coordinate_data[2][1]
            code.append(self.Libray[Libray_name][type]+"("+str(x0)+","+str(y0)+","+str(x1)+","+str(y1)+","+str(x2)+","+str(y2)+","+str(color)+");"+"//"+str(name))
        elif(type== "text"):

            x0=coordinate_data[0]
            y0=coordinate_data[1]
            code.append(self.Libray[Libray_name][type]+"("+str(string)+","+str(x0)+","+str(y0)+");"+"//"+str(name))
        elif(type== "picture"):

            x0=coordinate_data[0]
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
            LayerANDcode.append(self.make_command(Libray_name,"drawRectangle",a.get("tag"),a.get("color"),coordinate,a.get("layer"),""))

        for a in self.element.getiterator("fillOval"):#fillRectangle要素を参照
            coordinate=[[a.get("x0"),a.get("y0")],[a.get("x1"),a.get("y1")]]
            LayerANDcode.append(self.make_command(Libray_name,"fillRectangle",a.get("tag"),a.get("color"),coordinate,a.get("layer"),""))

        for a in self.element.getiterator("Triangle"):#fillRectangle要素を参照
            coordinate=[[a.get("x0"),a.get("y0")],[a.get("x1"),a.get("y2")],[a.get("x1"),a.get("y2")]]
            LayerANDcode.append(self.make_command(Libray_name,"fillRectangle",a.get("tag"),a.get("color"),coordinate,a.get("layer"),""))

        for a in self.element.getiterator("fillTriangle"):#fillRectangle要素を参照
            coordinate=[[a.get("x0"),a.get("y0")],[a.get("x1"),a.get("y2")],[a.get("x1"),a.get("y2")]]
            LayerANDcode.append(self.make_command(Libray_name,"fillRectangle",a.get("tag"),a.get("color"),coordinate,a.get("layer"),""))

        for a in self.element.getiterator("text"):#text要素を参照
            coordinate=[a.get("x0"),a.get("y0")]
            LayerANDcode.append(self.make_command(Libray_name,"text",a.get("tag"),a.get("color"),coordinate,a.get("layer"),a.get("text")))

        for a in self.element.getiterator("picture"):#text要素を参照
            coordinate=[a.get("x0"),a.get("y0")]
            LayerANDcode.append(self.make_command(Libray_name,"text",a.get("tag"),a.get("color"),coordinate,a.get("layer"),a.get("pass")))

        return LayerANDcode

    def get_UiCode(self,Libray_name):
        LayerANDcode=self.get_LayerAndcode(Libray_name)
        LayerANDcode.sort(reverse=True)
        print(LayerANDcode)
        code=[x[1] for x in LayerANDcode]

        return code
