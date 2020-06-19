import xlrd
def get_ip():
    excel=xlrd.open_workbook(r'.\ip_xiugai.xlsx')
    table=excel.sheet_by_index(0)
    ip=table.cell_value(0,0)
    return ip
