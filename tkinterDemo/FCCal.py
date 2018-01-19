# -*- coding: UTF-8 -*-
from Tkinter import *


class GUICal:
    def __init__(self, app):
        self.root = Tk()
        self.app = app
        self.root.title("Currency Converter")
        self.qFlag = False
        self.fc = StringVar()
        self.fc.set("USD")
        self.to = "RMB"
        self.amt = 0
        self.aRMB = StringVar()
        self.aRMB.set("0.00")
        self.aFC = StringVar()
        self.aFC.set("0.00")
        Label(self.root, textvariable = self.fc).grid(row = 0, column = 0, sticky = W)
        Label(self.root, text = "RMB").grid(row = 0, column = 2, sticky = W)
        self.e1 = Entry(self.root, textvariable = self.aFC)
        self.e1.grid(row = 1, column = 0, rowspan = 2)
        self.e2 = Entry(self.root, textvariable = self.aRMB)
        self.e2.grid(row = 1, column = 2, rowspan = 2)
        self.b1 = Button(self.root, text = "---->", command = self.toRMB)
        self.b1.grid(row = 1, column = 1)
        self.b2 = Button(self.root, text = "<----", command = self.toFC)
        self.b2.grid(row = 2, column = 1)
        self.f = Frame(self.root)
        self.f.grid(row = 3, column = 0, columnspan = 3)
        self.qb = Button(self.root, text = "Quit", command = self.close)
        self.qb.grid(row = 5, column = 1)
        self.root.mainloop()

    def showInfo(self):
        rStr = "%.2f"
        if self.to == "RMB":
            r = self.app.calRMB(self.fc.get(), self.amt)
            self.aRMB.set(rStr % r)
        else:
            r = self.app.calFC(self.fc.get(), self.amt)
            self.aFC.set(rStr % r)

    def toRMB(self):
        self.to = "RMB"
        self.amt = eval(self.aFC.get())
        self.showInfo()

    def toFC(self):
        self.to = self.fc.get()
        self.amt = eval(self.aRMB.get())
        self.showInfo()

    def close(self):
        self.qFlag = True
        self.root.quit()
        self.root.destroy()

class CCApp:
    def __init__(self):
        self.xRate = {"USD":6.306, "Euro":8.2735, "Yen":0.0775, "Pound":10.0486}

    def calRMB(self, fc, amt):
        return amt * self.xRate[fc]

    def calFC(self, fc, amt):
        return amt / self.xRate[fc]


if __name__ == '__main__':
    cc = CCApp()
    inter = GUICal(cc);
