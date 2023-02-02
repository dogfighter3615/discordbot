import xml.etree.ElementTree as ET

root = ET.Element("root")

token = ET.SubElement(root, "object")
token.set("token", "put your token here")

trello = ET.SubElement(root, "object")
trello.set("trello", "")

guild_id = ET.SubElement(root, "object")
guild_id.set("guild_id", "")

channel_id = ET.SubElement(root, "object")
channel_id.set("channel_id", "")

minecraft_ip = ET.SubElement(root, "minecraft_address")
minecraft_ip.set("ip", "")
minecraft_ip.set("port", "")

tree = ET.ElementTree(root)

b_xml = ET.tostring(root)
with open('bot/things.xml', 'wb') as f:
    f.write(b_xml)

print("done")
