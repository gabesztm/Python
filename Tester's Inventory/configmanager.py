import xml.etree.ElementTree as ET
from os.path import join


class Configmanager():
    def __init__(self):
        self.configfile=join("Configuration","config.xml")
        self.configtree=ET.parse(self.configfile)
        self.configroot=self.configtree.getroot()
        self.devicelistfile=join("Configuration","devices.xml")
        self.devtree = ET.parse(self.devicelistfile)
        self.devxmlroot=self.devtree.getroot()
        self.urllistfile=join("Configuration", "urls.xml")
        self.urltree=ET.parse(self.urllistfile)
        self.urlxmlroot=self.urltree.getroot()

    def getconfigvalue(self, key):
        return self.configroot.find(key).text

    def getdevices(self,DeviceList):
        for dev in self.devxmlroot.findall("device"):
            device_properties={}
            device_properties['id']=dev.find("ID").text
            device_properties['mfg']=dev.find("Manufacturer").text
            device_properties['model']=dev.find("Model").text
            device_properties['OS']=dev.find("OS").text
            device_properties['version']=dev.find("version").text
            device_properties['type']=dev.find("type").text
            DeviceList.append(device_properties)

    def geturls(self, URLlist):
        for url in self.urlxmlroot.findall("url"):
            url_properties={}
            url_properties['name']=url.find("name").text
            url_properties['address']=url.find("address").text
            url_properties['type']=url.find("type").text
            URLlist.append(url_properties)
