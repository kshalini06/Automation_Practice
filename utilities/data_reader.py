import xlrd


def excel_to_dict(file_path):
    # To open Workbook
    wb = xlrd.open_workbook(file_path)
    sheet = wb.sheet_by_index(0)
    test_data = []
    for i in range(1, sheet.nrows):
        temp = {}
        for j in range(sheet.ncols):
            temp.update({sheet.cell(0, j).value: sheet.cell(i, j).value})
        test_data.append(temp)
    return test_data