# -*- coding: UTF-8 -*-
import Tkinter
from PIL import Image, ImageTk

def btnClickHandler():
    print "clicked"

root = Tkinter.Tk()
img = Image.open('../jitu/bg_mengWuZhiDuoShaoYouXi.png')
photo = ImageTk.PhotoImage(img)
root.title("My GUI Button")  # 设置窗口标题
root.geometry("400x400")  # 设置窗口尺寸
btnClick = Tkinter.Button(root, text="Click Me",
                  image=photo, command=btnClickHandler)
btnClick.pack()
btnQuit = Tkinter.Button(root, text="Quit", command=root.quit)
btnQuit.pack()
root.mainloop()
