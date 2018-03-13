#coding:utf-8
import urllib2
import os
import codecs
import sys
import re
import requests
import io
from PIL import Image
import cStringIO
# import matplotlib.image as img
# import matplotlib.pyplot as plt
reload(sys)
sys.setdefaultencoding("utf-8")
req = urllib2.Request("http://image.baidu.com/search/index?ct=201326592&cl=2&st=-1&lm=-1&nc=1&ie=utf-8&tn=baiduimage&ipn=r&rps=1&pv=&fm=rs1&word=%E7%BE%8E%E5%A5%B3%E5%9B%BE%E7%89%87&oriquery=%E5%9B%BE%E7%89%87&ofr=%E5%9B%BE%E7%89%87&sensitive=0")
response = urllib2.urlopen(req)
path = "/Users/qijie/Documents/lxl/test/"
p = re.compile(r"\"ObjURL\":\".+?(?=,\")")
lst = p.findall(response.read())
lst2 = []

for i in range(len(lst)):
    s = lst[i].replace('"ObjURL":', '')
    s = s.replace('"', '').replace('\/','/')
    imgType = s[-4 : ]
    if imgType.find(".") == -1:
        continue
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER'  } 
    try:
        r = urllib2.Request(s, headers=headers)
        f = urllib2.urlopen(r)
    except urllib2.HTTPError:
        continue
    except urllib2.URLError:
        continue
    try:
        img = Image.open(cStringIO.StringIO(f.read()))
    except IOError:
        continue
    lst2.append(s)
    # img.save(path + "img" + str(i) + imgType)
try:
    file = "image.txt"
    fh = codecs.open(path + file, "w", 'utf-8')
except IOError:
    os.mkdir(path)
    fh = codecs.open(path + file, "w", 'utf-8')
finally:
    fh.writelines(["原始数据共" + str(len(lst)) + "条, 导出" + str(len(lst2)) + "条"])
    fh.write(str(lst2))
    fh.close()
    print "写入成功"

