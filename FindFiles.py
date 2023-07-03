from typing import List
import glob
import os
from os.path import join, dirname
from dotenv import load_dotenv

class FindFiles:
    
    _list_files_path : List[str]
    
    def __init__(self):
        
        load_dotenv(verbose=True)
        dotenv_path = join(dirname(__file__), '.env')
        load_dotenv(dotenv_path)
        
        self._dir_path = os.environ.get("DIR_PATH") + r"\**\*.crv"
        self._list_files_path = glob.glob(self._dir_path)
        
    @property
    def dir_path(self) -> str:
        return self._dir_path

    @property
    def list_files_path(self) -> List[str]:
        return self._list_files_path

    @dir_path.setter
    def dir_path(self, dir_path):
        self._dir_path = dir_path

    def print_list_files_path(self) -> None:
        for lfp in self._list_files_path:
            print(lfp)
    
    def print_dir_names(self) -> None:
        for lfp in self._list_files_path:
            print(os.path.basename(lfp))
        
if __name__ == "__main__":
    
    ff = FindFiles()
    ff.print_dir_names()
    ff.print_list_files_path()
