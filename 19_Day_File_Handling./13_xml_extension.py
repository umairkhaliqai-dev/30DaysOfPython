# Extensible Markup Language – hierarchical data
import xml.etree.ElementTree as ET
root = ET.Element("day19")
topic = ET.SubElement(root, "topic")
topic.text = "File Handling"
tree = ET.ElementTree(root)
tree.write("day19.xml")