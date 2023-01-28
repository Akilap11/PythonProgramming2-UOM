import xml.etree.ElementTree as ET

root=ET.Element("tag1")

tag2=ET.SubElement(root,"tag2")
tag2.text="Animal"

tag3=ET.SubElement(root,"tag3")
tag3.text="Domestic"

tag4=ET.SubElement(root,"tag4")

tag4_1=ET.SubElement(tag4,"tag4.1")
tag4_1.text="Cat"

tag4_2=ET.SubElement(tag4,"tag4.2")
tag4_2.text="Persian"

tag5=ET.SubElement(root,"tag5")
tag5.text="Iran"

tag6=ET.SubElement(root,"tag6")
tag6.text="Male"

tag7=ET.SubElement(root,"tag7")
tag7.text="2021.05.04"

ET.dump(root)