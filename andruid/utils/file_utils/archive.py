from os.path import dirname, join as path_join, normpath
from zipfile import ZipFile


class Archive:
    def __init__(self, file_path: str):
        self.__file_path = file_path

    def decompress(self, results_dir: str=''):
        archive_file_dir = dirname(self.__file_path)
        results_dir = normpath(path_join(archive_file_dir, results_dir))
        with ZipFile(self.__file_path, 'r') as zip_file:
            zip_file.extractall(results_dir)
