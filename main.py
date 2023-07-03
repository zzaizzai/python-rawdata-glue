from FindFiles import FindFiles as ff 
from SendanSiken import SendanSiken as ss
from Service import Service
import pandas as pd
import os

if __name__ == "__main__" :
    print("good")
    f = ff()
    # f.print_list_files_path()
    for aa in f._list_files_path:
        df : pd.DataFrame
        print(aa)
        print(Service.get_top_level_dir(f._dir_path))
        # df = pd.read_csv(aa, encoding='shift_jis', header=0)
        # if len(df.columns) == 1 :
        #     df = pd.read_table(aa, encoding='shift_jis', header=0)
        # s = ss(df)
        # print(df)
        # s.get_all_max_values()