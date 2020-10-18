import xml.etree.ElementTree as et

root = et.Element('root')
tree = et.ElementTree(element=root)

components = et.SubElement(root,"components")

component = et.SubElement(components,"Line",{"tag":"line1", "ID":"001", "color":"black", "x0":"0", "y0":"0", "x1":"0", "y1":"10", "layer":"1"})
component = et.SubElement(components,"Line",{"tag":"line2", "ID":"002", "color":"black", "x0":"0", "y0":"0", "x1":"0", "y1":"10", "layer":"2"})

component = et.SubElement(components,"Rectangle",{"tag":"Rectangle1", "ID":"003", "color":"black", "x0":"0", "y0":"0", "x1":"0", "y1":"10", "layer":"1"})
component = et.SubElement(components,"fillRectangle",{"tag":"Rectangle2", "ID":"004", "color":"black", "x0":"0", "y0":"0", "x1":"0", "y1":"10", "layer":"2"})

component = et.SubElement(components,"Triangle",{"tag":"Triangle1", "ID":"005", "color":"black", "x0":"0", "y0":"0", "x1":"0", "y1":"10","x2":"0", "y2":"10", "layer":"1"})
component = et.SubElement(components,"fillTriangle",{"tag":"Triangle2", "ID":"006", "color":"black", "x0":"0", "y0":"0", "x1":"0", "y1":"10","x2":"0", "y2":"10", "layer":"2"})

component = et.SubElement(components,"Ellipse",{"tag":"Ellipse1", "ID":"001", "color":"black", "x0":"0", "y0":"0", "x1":"0", "y1":"10", "layer":"1"})
component = et.SubElement(components,"fillEllipse",{"tag":"fillEllipse2", "ID":"002", "color":"black", "x0":"0", "y0":"0", "x1":"0", "y1":"10", "layer":"2"})

component = et.SubElement(components,"text",{"tag":"text1", "ID":"001","text":"hello", "color":"black", "x0":"0", "y0":"0","layer":"1"})
component = et.SubElement(components,"picture",{"tag":"picture1", "ID":"002","pass":"c/xxxxxxx","color":"black", "x0":"0", "y0":"0", "layer":"3"})

tree.write('components_test.xml', encoding='utf-8', xml_declaration=True)
