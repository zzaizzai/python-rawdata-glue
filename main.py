from FindFiles import FindFiles as ff 
from SendanSiken import SendanSiken as ss
import pandas as pd
import os

if __name__ == "__main__" :
    print("good")
    f = ff()
    # f.print_list_files_path()
    print(f.list_files_path[0])
    for aa in f.list_files_path:
        df : pd.DataFrame
        df = pd.read_csv(aa, encoding='shift_jis', header=0)
        if len(df.columns) == 1 :
            df = pd.read_table(aa, encoding='shift_jis', header=0)
        s = ss(df)
        print(df)
        s.get_all_max_values()