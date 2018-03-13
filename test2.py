#-*- coding:utf-8 -*-
import fileinput
import os
import sys
import glob

def printFilelist(args):
    if(os.path.isfile(str(args))):
        for line in fileinput.input(args):
            print fileinput.filename() + ":", fileinput.lineno(), line,
    else:
        for f in os.listdir(str(args)):
            print '\n'
            printFilelist(args + f)

printFilelist(sys.argv[1])
print '\n输出成功\n如果需要再次使用，请重新执行命令'

