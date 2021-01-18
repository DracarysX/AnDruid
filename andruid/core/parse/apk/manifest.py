from typing import List
from lxml.etree import _Element
from lxml import etree
from androguard.core.bytecodes.axml import AXMLPrinter

class Manifest:
    __ANDROID_NAME = '{http://schemas.android.com/apk/res/android}name'
    def __init__(self, manifest_path: str):
        self.__manifest_data = Manifest.parse_manifest(manifest_path)
    
    @staticmethod
    def parse_manifest(manifest_path: str) -> str:
        with open(manifest_path, 'rb') as manifest_file:
            manifest_bytes = manifest_file.read()
        axml = AXMLPrinter(manifest_bytes).get_xml_obj()
        return axml
    
    @staticmethod
    def get_child_elements_of_element(element_name: str, father_element: _Element):
        return father_element.findall(element_name)

    @staticmethod
    def get_child_elements_of_elements(element_name: str, father_elements: List[_Element]):
        child_elements = []
        for element in father_elements:
            child_elements += Manifest.get_child_elements_of_element(element_name, element)
        return child_elements
 
    @staticmethod
    def get_android_names(elements: List[_Element]):
        element_names = []
        for element in elements:
            element_names.append(element.get(Manifest.__ANDROID_NAME))
        return element_names

    @staticmethod
    def find_element_by_android_name(in_elements :List[_Element], android_name_filter: str) -> _Element:
        ret_element = None
        for element in in_elements:
            if element.get(Manifest.__ANDROID_NAME) == android_name_filter:
                ret_element = element
        return ret_element
    
    def get_manifest_data(self) -> _Element:
        return self.__manifest_data

    def __str__(self) -> str:
        return etree.tostring(self.__manifest_data, encoding='utf-8', pretty_print=True).decode("utf-8")
