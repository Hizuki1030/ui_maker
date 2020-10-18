# coding:utf-8
import xml.etree.ElementTree as ET
import xml.dom.minidom as md

tree = ET.parse("components_test.xml")

root = tree.getroot()
components = root.find("components")
component =components.find("component")
tag=component.find("tag")
tag.text="inner_lines"

tree = ET.ElementTree(root)

tree.write("components_test.xml",encoding= "UTF-8")
