from typing import List
import pprint

import pandas as pd
from File import File


class SendanSiken():

    index_col_now : int = 3
    count : int = 1 

    def __init__(self, file_c: File):
        self._file_c = file_c
        self.set_df_init(file_c)

    @property
    def df(self):
        return self._df

    @property
    def file_c(self):
        return self._file_c
        
    def set_df_init(self, file_c: File):
        print(file_c.get_dir_name_upper_level())
        try:
            df = pd.read_csv(file_c.path, encoding='shift_jis', header=0)
            if len(df.columns) == 1 :
                df = pd.read_table(file_c.path, encoding='shift_jis', header=0)
        except Exception as e:
            df = pd.read_table(file_c.path, encoding='shift_jis', header=0)
            print(e)    
        
        df_temp = df
        df_temp = df.drop(df.index[0])
        df_temp = df.reset_index()
        self._df = df_temp

    def show_information(self) :
        print(self)        

    def get_all_max_values(self) -> List[dict]:

        list_result = []
        try:
            while(True):
                list_result.append(self.get_max_values())
                self.next_col()
        except:
            pass

        # TODO get average tension 
        tension_sum : float = 0
        elon_sum : float = 0
        count : int = 0 
        
        for result in list_result:
            tension_sum += float(result["tension_s200"])
            elon_sum += float(result["elon"])
            count += 1 
        
        tension_average = round(tension_sum / count, 2)    
        elon_average = round(elon_sum / count , 2)
        
        # print("  " +  self.file_c.get_labo_no())
        # print("  " +  self.file_c.get_dir_name_upper_level())
        # pprint.pprint(list_result, indent=2)
        # for result in list_result:
            # print("elon: " + str(result["elon"]) + " strength: " +str( result["strength"]) + " tension(200mm2) : " + str(result["tension_s200"]))
        
        print(" tension_s200_ave: ", tension_average, " elon_ave: ", elon_average)
        print()
    

        return list_result

    def next_col(self) -> None:
        self.index_col_now  = self.index_col_now + 2  
        self.count = self.count +  1 

    def get_max_values(self) -> dict:
        dict_values : dict  = {}

        index_row = self.get_index_max_value(self.index_col_now)
        dict_values["elon"] = self.get_value(self.index_col_now - 1 , index_row)
        dict_values["strength"] = self.get_value(self.index_col_now, index_row)
        dict_values["col"] = self.index_col_now
        dict_values["count"] = self.count
        dict_values["tension_s200"] =round( float(dict_values["strength"])/200, 2)

        return dict_values
    

    def get_index_max_value(self, index_col: int) -> int:
        index_max = self.df.iloc[:,index_col]
        max_value: float = -1
        max_index: int = -1 
        for i, value in enumerate(index_max):
            
        
            if str(value).isalpha():
                continue
            
            if float(value) > max_value :
                max_value = float(value)
                max_index = int(i)
                
        return max_index
    
    def get_value(self, index_col : int, inedx_row: int ) -> any:
        result = self.df.iat[inedx_row,  index_col]
        return result
    
    def set_index_max(self, index:int) -> int:
        self.index_max = index

    def set_index_col_now(self, col:int) -> int:
        self.index_col_now = col
    
    def get_index_max(self) -> int:
        return self.index_max
    
    def get_col_now(self) -> int:
        return self.get_col_now
    

if __name__ == "__main__":
    df = pd.read_table('MG-.crv', encoding='shift_jis', header=0)
    aa = SendanSiken(df)
    index_max = aa.get_index_max_value(3)
    aa.get_all_max_values()