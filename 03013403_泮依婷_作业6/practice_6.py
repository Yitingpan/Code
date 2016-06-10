# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt    # 导入matplotlib.pyplot模块用于作图
import numpy as np    # 导入numpy模块用于矩阵运算
import math    # 导入math模块用于数字处理
import xlrd    # 导入xlrd模块用于读取excel表格中的数据
from statistics import mean, stdev, pstdev, variance, pvariance
# 直接导入statistics模块中的mean, stdev, pstdev, variance, pvariance等函数
from prettytable import PrettyTable    # 导入prettytable模块使输出的表格整齐


def getData(filename):     # 定义一个函数从excel表格中获取数据
    excel = xlrd.open_workbook(filename)
    sheet = excel.sheets()[0]     # 获取第一个sheet
    ncols = sheet.ncols    # 列数
    nrows = sheet.nrows    # 行数
    x_data = 0
    y_data = 0
    xygroups = []    # 定义一个列表来存放表格的数据
    xy = {'x': [], 'y': []}    # 定义一个有个对象的列表

    for i in range(0, ncols, 2):    # 用嵌套的for循环语句将excel中第1，3，5，7列和2，4，6，8列
        for j in range(0, nrows):   # 的数分别赋给x_data, y_data
            x_data = sheet.cell_value(j, i)
            y_data = sheet.cell_value(j, i + 1)

            xy['x'].append(float(x_data))
            xy['y'].append(float(y_data))    # 向列表末尾依次添加x，y的值

        xygroups.append(xy)    # 将列表xy中的元素添加到列表xygroups
        xy = {'x': [], 'y': []}    # 初始化列表xy，进入下一个循环继续赋值

    return xygroups


def staData(x, y):    # 定义一个函数统计数据
    xsta = {'avg': None, 'stdev': None, 'pstdev': None, 'var': None, 'pvar': None}
    # 定义一个字典来存放x轴数据的统计结果
    ysta = {'avg': None, 'stdev': None, 'pstdev': None, 'var': None, 'pvar': None}
    # 定义一个字典来存放y轴数据的统计结果

    xsta['avg'] = mean(x)
    ysta['avg'] = mean(y)

    xsta['stdev'] = stdev(x)
    ysta['stdev'] = stdev(y)

    xsta['pstdev'] = pstdev(x)
    ysta['pstdev'] = pstdev(y)

    xsta['var'] = variance(x)
    ysta['var'] = variance(y)

    xsta['pvar'] = pvariance(x)
    ysta['pvar'] = pvariance(y)    # 调用已从statistics模块导入的函数对数据进行统计

    r = np.corrcoef(x, y)[0, 1]    # 调用函数计算相关系数，但显示numpy模块中没有此函数

    return xsta, ysta, r


def plot(xygroups):    # 定义一个函数绘制数字点图及线性回归

    figcount = len(xygroups)
    figcol = 2
    figrow = math.ceil(figcount/figcol)
    fig = plt.figure(figsize=(12.0, 8.0))    # 创建绘图对象
    fig.subplots_adjust(left=0.05, right=0.95, bottom=0.05, top=0.95)

    for i in range(0, len(xygroups)):
        a, b = np.polyfit(xygroups[i]['x'], xygroups[i]['y'], 1)    # 调用ployfit拟合曲线，但显示numpy模块中无此函数
        predictedY = a*np.array(xygroups[i]['x']) + b
        fig.add_subplot(figrow, figcol, i+1)     # 子图
        plt.plot(xygroups[i]['x'], xygroups[i]['y'], 'bo')

        plt.title("Group "+str(i))    #设置图表标题
        plt.xlabel('x')
        plt.ylabel('y')    # 设置x，y轴的名字

        plt.plot(xygroups[i]['x'], predictedY,
                   label='Y by\nlinear fit, y = '
                   + str(round(a, 5))+'*x+'+str(round(b, 5)))    # 给绘制的曲线命名

        plt.legend(loc='best')


def draw_table(xygroups):    # 定义一个函数绘制统计结果的表格
    table = PrettyTable(["data set",
                         "x-avg", "x-std", "x-pstd", "x-var", "x-pvar",
                         "y-avg", "y-std", "y-pstd", "y-var", "y-pvar",
                         "pearson_r"])    # 表头
    for i in range(len(xygroups)):    # 利用for循环依次输出统计结果
        xsta, ysta, r = staData(xygroups[i]['x'], xygroups[i]['y'])

        table.add_row(["file" "%.0f" % i,
                   "%.3f" % xsta['avg'],    # 数据保留三位小数
                   "%.3f" % xsta['stdev'],"%.3f" %xsta['pstdev'],
                   "%.3f" % xsta['var'],"%.3f" % xsta['pvar'],
                   "%.3f" % ysta['avg'],
                   "%.3f" % ysta['stdev'],"%.3f" % ysta['pstdev'],
                   "%.3f" % ysta['var'],"%.3f" % ysta['pvar'],
                   "%.3f" % r])
    return table


xygroups = getData('practice6_data.xlsx')
print(draw_table(xygroups))
plot(xygroups)
plt.show()
