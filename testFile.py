#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import os, sys

# file = "/Users/star_xlliu/save.txt"
# exist = os.access(file, os.F_OK) #是否存在
# readabled = os.access(file, os.R_OK) #是否可读
# writeabled = os.access(file, os.W_OK) #是否可写
# exeabled = os.access(file, os.X_OK) #是否可执行
# print exist, readabled, writeabled, exeabled

# path = "/Users/star_xlliu/Documents/work/tmp"
# retPath = os.getcwd() #当前工作目录
# print retPath
# try:
#     os.removedirs(path)
#     os.chdir(path)
# except OSError:
#     os.mkdir(path)
#     os.chdir(path)
#     print os.listdir(os.getcwd())


# try:
#     fh = open(file, "w")
#     fh.write("测试测试测试")
# except IOError:
#     print "写入错误"
# else:
#     print "写入成功"
#     fh.close()

# def xlsx2json_1():
#     data = xlrd.open_workbook('/Users/star_xlliu/Documents/test2.xlsx')
#     tblsh = data.sheets()[0]
#     rownum = tblsh.nrows
#     colnum = tblsh.ncols
#     totalArray = []
#     arr = []
#     for i in range(0, colnum):
#         arr.append(tblsh.cell(1, i).value)

#     for row_index in range(2, rownum):
#         dic = {}
#         for col_index in range(0, colnum):
#             s = tblsh.cell(row_index, col_index).value
#             dic[arr[col_index]] = s
#         totalArray.append(dic)
#     a = json.dumps(totalArray, ensure_ascii=False)
#     file = codecs.open('/Users/star_xlliu/Documents/file.json', "w", "utf-8")
#     file.write(a)
#     file.close()

import xlrd
import json
import codecs
from collections import OrderedDict

def xlsx2json_2():
    wb = xlrd.open_workbook('/Users/star_xlliu/Documents/test2.xlsx')
    shArr = wb.sheet_names()
    for shname in shArr:
        convert_list = []
        sh = wb.sheet_by_name(shname)
        title = sh.row_values(1)
        for rownum in range(2, sh.nrows):
            rowvalue = sh.row_values(rownum)
            single = OrderedDict()
            for colnum in range(1, len(rowvalue)):
                single[title[colnum]] = rowvalue[colnum]
            convert_list.append(single)

        j = json.dumps(convert_list, ensure_ascii=False)

        with codecs.open('/Users/star_xlliu/Documents/' + shname + '.json', "w", "utf-8") as f:
            f.write(j)
            f.close()

xlsx2json_2()
