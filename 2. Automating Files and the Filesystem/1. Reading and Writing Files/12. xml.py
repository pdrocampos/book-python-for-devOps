import xml.etree.ElementTree as ET

tree = ET.parse('http_feeds.feedburner.com_oreilly_radar_atom.xml')
root = tree.getroot
print(root)

for child in root:
    print(child.tag, child.attrib)


ns = {'default': 'http://www.w3.org/2005/Atom'}
authors = root.findall("default:entry/default:author/default:name", ns)

for author in authors:
    print(author,text)





