import pandas as pd


class sendansiken():

    df: pd.DataFrame
    index_col_now : int = 3

    def __init__(self, df: pd.DataFrame):
        df_temp = df 
        df_temp = df.drop(df.index[0])
        df_temp = df.reset_index()
        self.df = df_temp

    def next_col(self):
        self.index_col_now  = self.index_col_now + 2  

    def get_index_max_value(self, index_col: int) -> int:
        index_max = self.df.iloc[:,index_col]
        max_value: float = -1
        max_index: int = -1 
        for i, value in enumerate(index_max):
        
            if value.isalpha():
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
    df = pd.read_table('MG-.crv', encoding='shift_jis', header=0)
    aa = sendansiken(df)
    index_max = aa.get_index_max_value(3)
    print(aa.get_value(index_col=2, inedx_row=index_max))
    print(aa.get_value(index_col=3, inedx_row=index_max))
    
