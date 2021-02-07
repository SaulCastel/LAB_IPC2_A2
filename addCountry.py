import xml.etree.ElementTree as ET
tree = ET.parse('country.xml')
root = tree.getroot()

country = ET.Element("country", attrib={"name":"France"})
root.append(country)
tree.write("output.xml")