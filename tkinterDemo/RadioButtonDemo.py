# -*- coding: UTF-8 -*-
from Tkinter import *
root = Tk()
root.title("My GUI Radiobutton")  # 设置窗口标题
root.geometry("400x400")  # 设置窗口尺寸
v = IntVar()
v.set(1)
Radiobutton(root, text = "One", variable = v, value = 1).pack()
Radiobutton(root, text = "Two", variable = v, value = 2).pack()
Radiobutton(root, text = "Three", variable = v, value = 3).pack()
root.mainloop()
