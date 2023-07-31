import openpyxl


def freeze_pane():
    wb = openpyxl.load_workbook('result.xlsx')
    # sheet = wb.active

    
    for sheet_name in wb.sheetnames:
        sheet = wb[str(sheet_name)]
        sheet.freeze_panes = 'A2'
        sheet.column_dimensions['B'].width = 80
    
    
    wb.save('result.xlsx')
    print("saved done")
    

if __name__ == "__main__":
    freeze_pane()