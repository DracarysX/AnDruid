from lxml import etree
from androguard.core.bytecodes.axml import AXMLPrinter

class Manifest:
    def __init__(self, manifest_path: str):
        self.__manifest_data = Manifest.parse_manifest(manifest_path)
    
    @staticmethod
    def parse_manifest(manifest_path: str) -> str:
        with open(manifest_path, 'rb') as manifest_file:
            manifest_bytes = manifest_file.read()
        axml = AXMLPrinter(manifest_bytes).get_xml_obj()
        return axml

    def get_manifest_data(self) -> etree._Element:
        return self.__manifest_data

    def __str__(self) -> str:
        return etree.tostring(self.__manifest_data, encoding='utf-8', pretty_print=True).decode("utf-8")
