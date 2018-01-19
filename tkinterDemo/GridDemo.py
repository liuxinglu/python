# -*- coding: UTF-8 -*-
from Tkinter import *
root = Tk()
root.title("My GUI Grid")  # 设置窗口标题
Label(root, text = "ID Number:").grid(sticky = E)
Label(root, text = "Name:").grid(sticky = E)
Entry(root).grid(row = 0, column = 1)
Entry(root).grid(row = 1, column = 1)
Checkbutton(root, text = "Registered User").grid(columnspan = 2, sticky = W)
Label(root, text = "X").grid(row = 0, column = 2, columnspan = 2, rowspan = 2, sticky = W + E + N + S)
Button(root, text = "Zoom In").grid(row = 2, column = 2)
Button(root, text = "Zoom Out").grid(row = 2, column = 3)
root.mainloop()
