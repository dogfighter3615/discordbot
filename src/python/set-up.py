import xml.etree.ElementTree as ET

root = ET.Element("root")

object1 = ET.SubElement(root, "object")
object1.set("token", "put your token here without quotes")

object2 = ET.SubElement(root, "object")
object2.set("trello", "")

tree = ET.ElementTree(root)

b_xml = ET.tostring(root)
with open('things.txt', 'wb') as f:
    f.write(b_xml)