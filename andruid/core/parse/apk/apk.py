from typing import List
from os.path import isdir, join as path_join

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

    def get_app_names(self) -> List[str]:
        manifest_data = self.get_manifest().get_manifest_data()
        application_elements = manifest_data.findall('application')
        app_names = []
        for app_element in application_elements:
            app_names.append(app_element.get('{http://schemas.android.com/apk/res/android}name'))
        return app_names
    
    def get_manifest(self) -> Manifest:
        if self.__manifest is None:
            self.__manifest = Manifest(path_join(self.__apk_files_dir, 'AndroidManifest.xml'))
        return self.__manifest
