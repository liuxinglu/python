# -*- coding: UTF-8 -*-
from Tkinter import *

def btnClickHandler():
    print "clicked"

root = Tk()
root.title("My GUI Button")  # 设置窗口标题
root.geometry("400x400")  # 设置窗口尺寸
btnClick = Button(root, text="Click Me", command=btnClickHandler)
btnClick.pack()
btnQuit = Button(root, text="Quit", command=root.quit)
btnQuit.pack()
root.mainloop()
