from typing import List
import glob
import os
from os.path import join, dirname
from dotenv import load_dotenv
from File import File


class FindFiles:

    def __init__(self):
        
        load_dotenv(verbose=True)
        dotenv_path = join(dirname(__file__), '.env')
        load_dotenv(dotenv_path)
        
        self._dir_top_level_path = os.environ.get("DIR_PATH")
        self._dir_path = os.environ.get("DIR_PATH") + r"\**\*.c?v"

        list_temp : List[File] = []
        for path in glob.glob(self._dir_path, recursive=True):
            f = File(file_path=path, dir_top_level_path=self._dir_top_level_path)
            list_temp.append(f)

        self._list_files_path = list_temp
        
    @property
    def dir_path(self) -> str:
        return self._dir_path

    @property
    def list_files_path(self) -> List[File]:
        return self._list_files_path

    @dir_path.setter
    def dir_path(self, dir_path) -> None:
        self._dir_path = dir_path
        
    def print_list_files_path(self) -> None:
        for lfp in self._list_files_path:
            print(lfp)
    
    def print_dir_names(self) -> None:
        for lfp in self._list_files_path:
            print(os.path.basename(lfp))

    def __str__(self) -> List[File]:
        return self._list_files_path
        
if __name__ == "__main__":
    
    ff = FindFiles()
    ff.print_dir_names()
    ff.print_list_files_path()