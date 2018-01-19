#!/usr/bin/python
# -*- coding: UTF-8 -*-
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

# x = 1;
# scope = vars();
# print scope['x']

# foo = lambda x: x*x
# print foo(2)

# class MyClass:
#     abb = 1
#     def __init__(args):
#         pass

#     @staticmethod
#     def smeth():
#         print '静态方法'

#     @classmethod
#     def cmeth(cls):
#         print 'this is a class method of ', cls
#         del cls.abb

#     def fun1(self):
#         try:
#             self.ab = self.abb + 1
#         except TypeError:
#             self.ab = 0
#         print self.ab
#         del self.abb

#     def __delattr__(self, name):
#         print "删除" + name;

#     def __getattr__(self, name):
#         print "访问" + name
    
#     def __setattr__(self, name, value):
#         print "设置" + name + "=" + str(value)

#     def __str__(self):
#         print "字符串"
    

# m = MyClass()
# m.fun1()

def flatten(nested):
    try:
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested
nested = [[[1, 2]], [3, 4], [5]]
print list(flatten(nested))
