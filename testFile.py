#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys

file = "/Users/star_xlliu/save.txt"
# exist = os.access(file, os.F_OK) #是否存在
# readabled = os.access(file, os.R_OK) #是否可读
# writeabled = os.access(file, os.W_OK) #是否可写
# exeabled = os.access(file, os.X_OK) #是否可执行
# print exist, readabled, writeabled, exeabled

path = "/Users/star_xlliu/Documents/work/tmp"
# retPath = os.getcwd() #当前工作目录
# print retPath
# try:
#     os.removedirs(path)
#     os.chdir(path)
# except OSError:
#     os.mkdir(path)
#     os.chdir(path)
#     print os.listdir(os.getcwd())



try:
    fh = open(file, "w")
    fh.write("测试测试测试")
except IOError:
    print "写入错误"
else:
    print "写入成功"
    fh.close()