from typing import List
from os.path import isdir, join as path_join
from lxml.etree import _Element

from .manifest import Manifest
from ....utils.file_utils.archive import Archive


class Apk:
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
        return Manifest.get_child_elements_of_element('application', self.get_manifest().get_manifest_data())
    
    def get_app_names(self) -> List[str]:
        return Manifest.get_android_names(self.get_app_elements())
    
    def get_activity_elements(self, app_name: str=None) -> List[_Element]:
        ACTIVITY = 'activity'
        app_elements = self.get_app_elements()
        activity_elements = []
        if app_name:
            app_element = Manifest.find_element_by_android_name(app_elements,app_name)
            activity_elements = Manifest.get_child_elements_of_element(ACTIVITY, app_element)
        else:
            activity_elements = Manifest.get_child_elements_of_elements(ACTIVITY, app_elements)
        return activity_elements
    
    def get_activity_names(self, app_name: str=None) -> List[str]:
        return Manifest.get_android_names(self.get_activity_elements(app_name))

    def get_manifest(self) -> Manifest:
        if self.__manifest is None:
            self.__manifest = Manifest(path_join(self.__apk_files_dir, 'AndroidManifest.xml'))
        return self.__manifest
