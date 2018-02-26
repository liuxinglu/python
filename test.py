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

class MyClass:
    abb = 1
    def __init__(args):
        pass

    @staticmethod
    def smeth():
        print '静态方法'

    @classmethod
    def cmeth(cls):
        print 'this is a class method of ', cls
        del cls.abb

    def fun1(self):
        try:
            self.ab = self.abb + 1
        except TypeError:
            self.ab = 0
        print self.ab
        del self.abb

    def __delattr__(self, name):
        print "删除" + name;

    def __getattr__(self, name):
        print "访问" + name
    
    def __setattr__(self, name, value):
        print "设置" + name + "=" + str(value)

    def __str__(self):
        print "字符串"
    

# m = MyClass()
# m.fun1()

# def flatten(nested):
#     try:
#         try:
#             nested + ""
#         except TypeError:
#             print nested
#             pass
#         else:
#             print "主动生成异常"
#             raise TypeError
#         for sublist in nested:
#             for element in flatten(sublist):
#                 yield element
#     except TypeError:
#         print "外层" + str(nested)
#         yield nested

# print list(flatten(nested))

import time
import functools

def log1(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'call %s():'% func.__name__
        return func(*args, **kw)
    return wrapper

def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

def log3(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print '%s begin call %s():'% (time.asctime(), func.__name__)
        func(*args, **kw)
        print '%s end call %s()'% (time.asctime(), func.__name__)
    return wrapper

def log4(text):
    if isinstance(text, str) == False:
        @functools.wraps(text)
        def wrapper(*args, **kw):
            print '%s begin call %s():' % (time.asctime(), text.__name__)
            text(*args, **kw)
            print '%s end call %s()' % (time.asctime(), text.__name__)
        return wrapper
    else:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print '%s %s():' % (text, func.__name__)
                return func(*args, **kw)
            return wrapper
        return decorator

@log4
def now(num):
    sum = 1
    for i in range(1,num):
        sum = sum * i
    print sum


# now(10)

# fun = log2('exe')(now)
# fun()


# def fun(*l):
    
#     print l

# fun(1,2,3)
__metaclass__ = type
class Bird(object):
    def __init__(self):
        self.hungry = True
    
    def eat(args):
        if args.hungry:
            print 'Aaaah~~'
            args.hungry = False
        else:
            print 'No Thanks'

class SongBird(Bird):
    def __init__(self, *args):
        # super(SongBird,Bird.__init__(self,*args))
        super(SongBird, self).__init__()
        self.sound = 'Squak'
    def sing(args):
        print args.sound


nested = [[[1, "test"]], [3, 4], [5]]
nested1 = [1,2,3]
nested2 = [4,5,6,7,8]
nested3 = [9,10,11]

def main1(nest):
    for sub in nest:
        for item in sub:
            yield item

if __name__ == '__main__':
    # for num in main1(nested):
    #     print type(num)
    # m = main1(nested)
    # print m.next()
    # print m.next()
    for i in nested, nested1, nested2, nested3:
        print i
