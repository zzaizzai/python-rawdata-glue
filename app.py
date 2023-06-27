import pandas as pd
from typing import List

class sendansiken():

    df: pd.DataFrame
    index_col_now : int = 3

    def __init__(self, df: pd.DataFrame):
        df_temp = df 
        df_temp = df.drop(df.index[0])
        df_temp = df.reset_index()
        self.df = df_temp


    def get_all_max_values(self) -> List[dict]:

        list_result = []
        try:
            while(True):
                list_result.append(self.get_max_values())
                self.next_col()
        except Exception as e:
            pass

        print(list_result)

        return list_result

    def next_col(self) -> None:
        self.index_col_now  = self.index_col_now + 2  

    def get_max_values(self) -> dict:
        dict_values : dict  = {}

        index_row = self.get_index_max_value(self.index_col_now)
        dict_values["elon"] = self.get_value(self.index_col_now - 1 , index_row)
        dict_values["strength"] = self.get_value(self.index_col_now, index_row)
        dict_values["col"] = self.index_col_now

        return dict_values
    

    def get_index_max_value(self, index_col: int) -> int:
        index_max = self.df.iloc[:,index_col]
        max_value: float = -1
        max_index: int = -1 
        for i, value in enumerate(index_max):
        
            if type(value) is str:
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
    
    def get_data(self) -> pd.DataFrame:
        return self.data
    

if __name__ == "__main__":
    # df = pd.read_table('MG-.xlsx', header=0)
    df = pd.read_excel('MG-.xlsx', header=0)
    aa = sendansiken(df)
    index_max = aa.get_index_max_value(3)
    aa.get_all_max_values()
    
