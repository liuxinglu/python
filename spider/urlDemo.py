#!/usr/bin/env Python
# coding=utf-8
import urllib2
import urllib
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
content = raw_input("content?:\n")
content = urllib.quote(content.decode(sys.stdin.encoding).encode('utf-8'))
url = "http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=" + content + "&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=000000"
req = urllib2.Request(url)
response = urllib2.urlopen(req)
path = "/Users/star_xlliu/Documents/lxl/test/"
# fh = ''
# try:
#     file = "imageSrc.txt"
#     fh = codecs.open(path + file, "w", 'utf-8')
# except IOError:
#     os.mkdir(path)
#     fh = codecs.open(path + file, "w", 'utf-8')
# finally:
#     fh.write(response.read())
#     fh.close()
#     print "写入成功"

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
    try:
        img = img.convert('RGB')
        img.save(path + "img" + str(i) + imgType)
    except IOError:
        try:
            os.mkdir(path)
        except OSError, e:
            if e.errno != os.errno.EEXIST:
                raise
            pass
        img = img.convert('RGB')
        img.save(path + "img" + str(i) + imgType)
fh = ''
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

