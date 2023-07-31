from FindFiles import FindFiles as ff 
from SendanSiken import SendanSiken as ss
import ExcelControl
import pandas as pd
import os
from pathlib import Path
import glob


if __name__ == "__main__" :

    f = ff()

    all_values : list = []
    for aa in f.list_files_path:
    
        try:
            s = ss(aa)
            for amv in s.get_all_max_values():
                all_values.append(amv)
        except Exception as e:
            print(e)
            
    print("all values:" , len(all_values))
    df_w = pd.DataFrame(all_values)
    df_w = df_w.drop(["col"], axis=1)

    df_w_dupl = df_w.drop_duplicates(subset=["path"], keep="first")
    df_w_average = df_w_dupl[["path", "n" , "strength", "tension_s200_ave", "elon_ave"]]

    with pd.ExcelWriter("result.xlsx") as writer:
        df_w.to_excel(writer, sheet_name="all")
        df_w_average.to_excel(writer, sheet_name="average")
    
    ExcelControl.freeze_pane()
    
    print("Done")

    
    
    