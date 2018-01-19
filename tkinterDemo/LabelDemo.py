# -*- coding: UTF-8 -*-
from Tkinter import *
root = Tk()
root.title("My GUI Label") #设置窗口标题
root.geometry("400x400") #设置窗口尺寸
label = Label(root, text = "Hello World, TutorABC Python Class", width=100, fg="red")
#窗口标题也可以通过父子关系设置：父为master 子为children
# label.master.title("My GUI")
label.pack()
root.mainloop()
