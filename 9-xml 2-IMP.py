import xml.etree.ElementTree as ET 
vehicle_xml_data_as_string = "<motorvehicles><vehicle><registration_no>CBB1456</registration_no><make>Toyota</make><model>Premio</model></vehicle><vehicle><registration_no>PR2245</registration_no><make>Mazda</make><model>Bongo</model></vehicle><vehicle><registration_no>DE2115</registration_no><make>TATA</make><model>Sumo</model></vehicle><vehicle><registration_no>CAR7785</registration_no><make>Kia</make><model>Optima</model></vehicle></motorvehicles>" 
root = ET.fromstring(vehicle_xml_data_as_string) 
for element in root.iter(tag='vehicle'): 
    if(element.find('registration_no').text == 'DE2115'): 
        element.find('make').text= 'Nissan' 
        element.find('model').text= 'Skyline' 
        print(element.find('registration_no').text)


