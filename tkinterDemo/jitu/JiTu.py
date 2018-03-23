#coding:utf-8
import Tkinter
from PIL import ImageTk, Image
from enum import Enum
# import Block as b
import random, math
import EventManager

class Type(Enum):
    Ji = 0
    Tu = 1
    Spider = 2
    Wing = 3

contentList = []
tl = Tkinter.Toplevel()
class JiTu:
    def __init__(self, logic=None):
        self.root = Tkinter.Tk()
        self.root.geometry("1136x640")
        self.logic = logic
        self.root.title("鸡兔同笼")
        bg = ImgPlus('../../jitu/bg_mengWuZhiDuoShaoYouXi.png')
        btnTu = ImgPlus('../../jitu/img_tuZiFangKuai.png')
        btnJi = ImgPlus('../../jitu/img_xiaoJiFangKuai.png')
        bg.createWidget("Label", self.root, 0, 0)
        btnTu.createWidget("Button", self.root, 130, 500, self.tuziClick)
        btnJi.createWidget("Button", self.root, 1030, 380, self.jiClick)
        # self.eventManager = EventManager.EventManager()
        # self.eventManager.AddEventListener(b.Block.CLICK, self._blockClickHandler)
        # self.eventManager.Start()
        self.manager = JiTuManager()
        self.root.mainloop()

    def tuziClick(self):
        pass
        # tuzi = b.Block(self.eventManager)
        # self.manager.calCount("jian", Type.Tu)
        # contentList.append(tuzi)
    
    def jiClick(self):
        pass
        # ji = b.Block(self.eventManager)
        # self.manager.calCount("jian", Type.Ji)
        # contentList.append(ji)

    def addBlock(self, args):
        pass
        # contentList[len(contentList) -  1].setPos(200, 100)

    def _blockClickHandler(self, e):
        tar = e.dict["target"]
        # self.manager.calCount("jia", e.dict["type"])


class ImgPlus:
    def __init__(self, args):
        self._setPath(args)

    def _setPath(self, path):
        self._img = ImageTk.PhotoImage(Image.open(path))

    def createWidget(self, cls, root, imgx=None, imgy=None, command=None):
        exec("wii = Tkinter." + cls + "(root, image = self._img)")
        if imgx != None:
            self.setPos(wii, imgx, imgy)
        return wii

    def setPos(self, obj, imgx, imgy):
        obj.place(relx=0, rely=0, x=imgx, y=imgy)

class JiTuManager:
    def __init__(self):
        self.curLevel = 0
        self.countArr = []

    def getTarget(self):
        arr = []
        if self.curLevel == 0:
            count = math.floor(random.random() * 5) + 10
            for i in range(count):
                arr.append(Type.Tu) if i == 10 else arr.append(Type.Ji)
        elif self.curLevel == 1:
            count = math.floor(random.random() * 5) + 15
            for i in range(count):
                arr.append(Type.Ji) if i > 15 else (arr.append(Type.Tu) if i > 10 else arr.append(Type.Spider))
        elif self.curLevel == 2:
            count = math.floor(random.random() * 5) + 20
            for i in range(count):
                arr.append(Type.Ji) if i > 20 else (arr.append(Type.Tu if i > 15 else arr.append(Type.Spider) if i > 10 else arr.append(Type.Wing)))
        for i in range(len(arr)):
            if arr[i] == Type.Ji:
                if self.curLevel == 2:
                    tempCount3 += 2
                else:
                    tempCount2 += 2
            elif arr[i] == Type.Tu:
                tempCount2 += 4
            elif arr[i] == Type.Spider:
                tempCount2 += 8
            else:
                tempCount2 += 6
                tempCount3 += 4
        arr = [len(arr), tempCount2, tempCount3]
        self.countArr = arr

    def calCount(self, fun, type):
        if type == Type.Wing:
            if fun == "jian":
                self.countArr[1] -= 6
                self.countArr[2] -= 4
            else:
                self.countArr[1] += 6
                self.countArr[2] += 4
        elif type == Type.Spider:
            if fun == "jian":
                self.countArr[1] -= 8
            else:
                self.countArr[1] += 8
        elif type == Type.Tu:
            if fun == "jian":
                self.countArr[1] -= 4
            else:
                self.countArr[1] += 4
        else:
            if fun == "jian":
                if self.curLevel == 2:
                    self.countArr[2] -= 2
                self.countArr[1] -= 2
            else:
                if self.curLevel == 2:
                    self.countArr[2] += 2
                self.countArr[1] += 2
        if fun == "jian":
            self.countArr[0] -= 1
        else:
            self.countArr[0] += 1

        
def main():
    jt = JiTu()

if __name__ == '__main__':
    main()
