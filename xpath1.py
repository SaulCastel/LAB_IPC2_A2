import xml.etree.ElementTree as ET
tree = ET.parse("country.xml")
root = tree.getroot()

for country in root.findall(".//country"):
    rank = country.find("./rank").text 
    year = country.find("./year").text
    print(year, rank, sep=", ")