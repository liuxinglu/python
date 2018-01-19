# -*- coding: UTF-8 -*-
from Tkinter import *
root = Tk()
root.title("My GUI Entry")  # 设置窗口标题
root.geometry("400x400")  # 设置窗口尺寸
strVar = StringVar()
e = Entry(root, textvariable = strVar)
e.pack()
print strVar.get()
strVar.set("new text")
print strVar.get()
root.mainloop()
