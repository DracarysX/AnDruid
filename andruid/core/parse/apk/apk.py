from typing import List
from os.path import isdir, join as path_join
from lxml.etree import _Element

from .manifest import Manifest
from ....utils.file_utils.archive import Archive


class Apk:
    __ANDROID_NAME = '{http://schemas.android.com/apk/res/android}name'
    
    def __init__(self, apk_path: str, working_dir: str=''):
        self.__apk_path = apk_path
        self.__working_dir = working_dir
        self.__manifest = None

        apkArchive = Archive(apk_path)
        self.__apk_files_dir = apkArchive.decompress(self.__working_dir)
    
    def get_package_name(self) -> str:
        manifest_data = self.get_manifest().get_manifest_data()
        return manifest_data.get('package')

    def get_app_elements(self) -> List[_Element]:
        return Apk.get_child_elements('application', self.get_manifest().get_manifest_data())
    
    def get_app_names(self) -> List[str]:
        return Apk.get_elements_android_names(self.get_app_elements())
    
    def get_activity_elements(self, app_name: str=None) -> List[_Element]:
        activity_elements = []
        ACTIVITY = 'activity'
        for app_element in self.get_app_elements():
            if app_name:
                if app_element.get(Apk.__ANDROID_NAME) == app_name:
                    activity_elements += Apk.get_child_elements(ACTIVITY, app_element)
                    break
            else:
                activity_elements += Apk.get_child_elements(ACTIVITY, app_element)
        return activity_elements
    
    def get_activity_names(self, app_name: str=None) -> List[str]:
        return Apk.get_elements_android_names(self.get_activity_elements(app_name))

    def get_manifest(self) -> Manifest:
        if self.__manifest is None:
            self.__manifest = Manifest(path_join(self.__apk_files_dir, 'AndroidManifest.xml'))
        return self.__manifest

    
    @staticmethod
    def get_child_elements(element_name: str, father_element: _Element):
        return father_element.findall(element_name)

    @staticmethod
    def get_elements_android_names(elements: List[_Element]):
        element_names = []
        for element in elements:
            element_names.append(element.get(Apk.__ANDROID_NAME))
        return element_names