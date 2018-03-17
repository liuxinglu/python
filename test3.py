#coding:utf-8
import re
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