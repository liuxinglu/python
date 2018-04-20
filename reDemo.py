#coding:utf-8
import re
# key = r"<html><body><h1>hello world<h1></body></html>"#这段是你要匹配的文本
# p1 = r"(?<=<h1>).+?(?=<h1>)"#这是我们写的正则表达式规则，你现在可以不理解啥意思
# pattern1 = re.compile(p1)#我们在编译这段正则表达式
# matcher1 = re.search(pattern1,key)#在源文本中搜索符合正则表达式的部分
# print matcher1.group(0)#打印出来
# key = r"<h1>hello world<h1>"#源文本
# p1 = r"<h1>.+<h1>"#我们写的正则表达式，下面会将为什么
# pattern1 = re.compile(p1)
# print pattern1.findall(key)#发没发现，我怎么写成findall了？咋变了呢？

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
p = re.compile(r"(?<=\[).+?(?=\])") #
p2 = re.compile(r"(?<=\().+?(?=\))")
s = u"#词语#[这|那]#词语字数#个(字|汉字)(怎么|咋|如何|怎样)写"
s2 = u"春天"
lst = p.findall(s)
lst2 = p2.findall(s)
arr = []
arr2 = []
for i in lst:
    arr.append(i.split("|"))
    print i
for i in lst2:
    arr2.append(i.split("|"))
    print i

arr3 = []
for i in arr:
    for k in i:
        arr3.append(s2 + str(k) + str(len(s2)) + "个")
for num in range(2):
    lengt = len(arr3)
    for i in range(lengt):
        for j in arr2[num]:
            arr3.append(arr3[i] + j)
    arr3 = arr3[lengt:]
for i in range(len(arr3)):
    arr3[i] += "写"
for i in arr3:
    print i