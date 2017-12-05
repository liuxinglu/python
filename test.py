#!/usr/bin/python
# -*- coding: UTF-8 -*-
# print "你好";
# raw_input("\n\nPress the Enter key to exit");
# count = 0
# while count < 5 :
#     print count, "is less than 5"
#     count = count + 1
# else :
#     print count, "is not less than 5"

import random
import sys
import time

result = []
while True :
    result.append(int(random.uniform(1, 7)))
    result.append(int(random.uniform(1, 7)))
    result.append(int(random.uniform(1, 7)))
    print result
    count = 0
    index = 2
    pointStr = ""
    while index >= 0:
        currPoint = result[index]
        count += currPoint
        index -= 1
        pointStr += " "
        pointStr += str(currPoint)
    if count <= 11:
        sys.stdout.write(pointStr + " -> " + "小" + "\n")
        time.sleep(1)
    else:
        sys.stdout.write(pointStr + " -> " + "大" + "\n")
        time.sleep(1)
    result = []

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

# from Tkinter import *
# root = Tk()

# li = ['C', 'python', 'php', 'html', 'typeScript', 'SQL', 'java']
# movie = ['CSS', 'jQ', 'exml']
# listb = Listbox(root)
# listb2 = Listbox(root)
# btn = Button(root)
# canvas = Canvas(root)
# checkBtn = CHECKBUTTON(root)
# entry = Entry(root)
# frame = Frame(root)
# label = Label(root)
# menuBtn = Menubutton(root)
# menu = Menu(root)
# msg = Message(root)
# radio = Radiobutton(root)
# scale = Scale(root)
# scrollbar = Scrollbar(root)
# text = Text(root)
# toplvl = Toplevel(root)
# spinbox = Spinbox(root)


# for item in li:
#     listb.insert(0, item)

# for item in movie:
#     listb2.insert(0, item)

# listb.pack()
# listb2.pack()
# root.mainloop()