from os.path import isdir
from ....utils.file_utils.archive import Archive


class Apk:
    def __init__(self, apk_path: str, working_dir: str=''):
        self.__apk_path = apk_path
        self.__working_dir = working_dir
        if isdir(apk_path):
            # TODO
            pass
        else:
            apkArchive = Archive(apk_path)
            apkArchive.decompress(self.__working_dir)
            self.__apk_parser()
    
    def __apk_parser(self):
        # TODO
        pass