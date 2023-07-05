from FindFiles import FindFiles as ff 
from SendanSiken import SendanSiken as ss
from Service import Service

if __name__ == "__main__" :
    print("good")
    f = ff()
    # f.print_list_files_path()
    for aa in f.list_files_path:
        try:
            s = ss(aa)
            s.get_all_max_values()
        except Exception as e:
            print(e)
            