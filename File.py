import os

class File:

    def __init__(self, file_path : str, dir_top_level_path: str):
        self._path = file_path
        self._dir_top_level_path = dir_top_level_path

    @property
    def path(self) -> str:
        return self._path
    
    @property
    def dir_top_level_path(self) -> str :
        return self._dir_top_level_path
    
    def get_labo_no(self):
        return os.path.dirname(self.get_dir_name_upper_level())

    def get_conditions(self):
        upper_names = self.get_dir_name_upper_level()
        upper_names_without_file_name = upper_names[ len(self.get_labo_no()) : - len(self.get_file_name_with_extension()) - 1]
        
        if len(upper_names_without_file_name) == 0:
            return "NA"
        
        return upper_names_without_file_name

    def get_file_name_without_extension(self):
        return os.path.splitext(os.path.basename(self.path))[0]

    def get_file_name_with_extension(self) -> str :
        return os.path.basename(self.path)

    def get_dir_name_upper_level(self) -> str :
        return self.path[len(self.dir_top_level_path) + 1:]

    def __str__(self) -> str:
        return self._path