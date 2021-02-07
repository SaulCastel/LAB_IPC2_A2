import xml.etree.ElementTree as ET
tree = ET.parse('country.xml')
root = tree.getroot()

for rank in root.iter("rank"):
    new_rank = int(rank.text) + 1
    rank.text = str(new_rank)
    rank.set("updated", "yes")

for country in root.findall("country"):
    rank = int(country.find("rank").text)
    if rank > 50:
        root.remove(country)

tree.write("output.xml")