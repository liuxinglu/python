#coding:utf-8
import Tkinter
from PIL import ImageTk, Image

class JiTu:
    def __init__(self, logic=None):
        self.root = Tkinter.Tk()
        self.logic = logic
        self.root.title("鸡兔同笼")
        bg = self.createImg('../jitu/bg_mengWuZhiDuoShaoYouXi.png', 'Label', 0, 0)
        self.root.mainloop()

    def createImg(self, path, cls, imgx, imgy):
        exec('self.bgLabel = Tkinter.' + cls +
             '(self.root, image=ImageTk.PhotoImage(Image.open(path)))')
        self.setPos(self.bgLabel, 0, 0)
        return bg

    def setPos(self, obj, imgx, imgy):
        obj.grid(row = imgx, column = imgy)
        
def main():
    jt = JiTu()

if __name__ == '__main__':
    main()
