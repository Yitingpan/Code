import xlrd
import numpy as np


def getData(filename):
    excel = xlrd.open_workbook(filename)
    sheet = excel.sheets()[0]
    ncols = sheet.ncols
    nrows = sheet.nrows
    x_data = 0
    y_data = 0
    xygroups = []
    xy = {'x': [], 'y': []}

    for i in range(0, ncols, 2):
        for j in range(0, nrows):
            x_data = sheet.cell_value(j, i)
            y_data = sheet.cell_value(j, i + 1)

            xy['x'].append(float(x_data))
            xy['y'].append(float(y_data))

        xygroups.append(xy)
        xy = {'x': [], 'y': []}

    return xygroups


xygroups = getData('practice6_data.xlsx')
print(np.array(xygroups))
