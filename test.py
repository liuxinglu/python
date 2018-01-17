#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    s = '中国'
    su = u'中国'

    # #s为unicode先转为utf-8

    # #因为s为所在的.py(# -*- coding=UTF-8 -*-)编码为utf-8

    s_unicode = s.decode('UTF-8')

    print (s_unicode == su)

    # #s转为gb2312,先转为unicode再转为gb2312

    s.decode('utf-8').encode('gb2312')

    #如果直接执行s.encode('gb2312')会发生什么？

    # s.encode('utf-8')
# raw_input("\n\nPress the Enter key to exit");
# count = 0
# while count < 5 :
#     print count, "is less than 5"
#     count = count + 1
# else :
#     print count, "is not less than 5"

# import random
# import sys
# import time

# result = []
# while True :
#     result.append(int(random.uniform(1, 7)))
#     result.append(int(random.uniform(1, 7)))
#     result.append(int(random.uniform(1, 7)))
#     print result
#     count = 0
#     index = 2
#     pointStr = ""
#     while index >= 0:
#         currPoint = result[index]
#         count += currPoint
#         index -= 1
#         pointStr += " "
#         pointStr += str(currPoint)
#     if count <= 11:
#         sys.stdout.write(pointStr + " -> " + "小" + "\n")
#         time.sleep(1)
#     else:
#         sys.stdout.write(pointStr + " -> " + "大" + "\n")
#         time.sleep(1)
#     result = []

# class Employee:
#     '所有员工的基类'
#     empCount = 0

#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1

#     def displayCount(self):
#         print "Total Employee %d" % Employee.empCount

#     def displayEmployee(self):
#         print "Name :", self.name, ", Salary :", self.salary
        
        
# emp1 = Employee("Zara", 2000)
# emp2 = Employee("Mani", 5000)
# emp1.displayCount()

# import re
# line = "Cats are smarter than dogs";

# matchObj = re.match(r'dog', line, re.M|re.I)
# if matchObj:
#     print "match --> matchObj.group() : ", matchObj.group()
# else:
#     print "No match~"

# matchObj = re.search(r'dog', line, re.M|re.I)
# if matchObj:
#     print "search --> matchObj.group():", matchObj.group()
# else:
#     print "No match~"

# def double(matched):
#     value = int(matched.group('values'))
#     return str(value * 2)

# s = 'A23G4GHD567'
# print(re.sub('(?P<values>\d+)', double, s))

# li = ['C', 'python', 'php', 'html', 'typeScript', 'SQL', 'java']
# movie = ['CSS', 'jQ', 'exml']


# for item in li:
#     listb.insert(0, item)

# for item in movie:
#     listb2.insert(0, item)

# listb.pack()
# listb2.pack()

# width = input("please enter width");
# price_width = 10;
# item_width = width - price_width;
# header_format = '%-*s%*s';
# format = '%-*s%*.2f';
# print '=' * width;
# print header_format %  (item_width, 'Item', price_width, 'Price');

# def lookup(data, label, name):
#     return data[label].get(name);

# def store(data, *full_names):
#     for full_name in full_names:
#         names = full_name.split();
#         if len(names) == 2:
#             names.insert(1, " ");
#         labels = 'first', 'middle', 'last';
#         for label, name in zip(labels, names):
#             people = lookup(data, label, name);
#             if people:
#                 people.append(full_name);
#             else:
#                 data[label][name] = [full_name];


# def init(data):
#     data['first'] = {};
#     data['middle'] = {};
#     data['last'] = {};
          
# d = {};
# init(d);
# store(d, 'Han Solo', 'Luke Sky', 'Luke Sky', 'Anake Walker')
# print lookup(d, 'first', 'Luke');


# a, b = 13, 42;
# while a != b:
#     if a > b:
#         a = a - b;
#     else:
#         b = b - a;
# print a;
# str = '''<td></td>, <td></td>, <td style="display: none"></td>, <td class="text - left">
# 总计
# </td > , < td class = "" > 0.00 < /td > , < td class = "" >
# 0.00
# </td >, < td class = "" >
# 0.00
# </td >, < td class = "" >
# 0.00
# </td >, < td class = "" >
# 0.00
# </td >, < td class = "" >
# 0.00
# </td >, < td class = "" >
# 0.00
# </td >, < td class = "" >
# 0.00
# </td >, < td class = " va-bg-com-total" >
# 0.00
# </td >, < td class = " va-bg-com-upper" >
# 0.00
# </td >''';
# x = 1;
# scope = vars();
# print scope['x']

# foo = lambda x: x*x
# print foo(2)

