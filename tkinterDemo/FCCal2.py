# -*- coding: UTF-8 -*-
from Tkinter import *


class GUICal:
    def __init__(self, cal):
        self.root = Tk()
        self.cal = cal
        self.root.title("Currency Converter")
        self.fc = StringVar()
        self.fc.set("USD")
        self.to = "RMB"
        self.amt = 0
        self.aRMB = StringVar()
        self.aRMB.set("0.00")
        self.aFC = StringVar()
        self.aFC.set("0.00")
        Label(self.root, textvariable=self.fc).grid(row=0, column=0, sticky=W)
        Label(self.root, text="RMB").grid(row=0, column=2, sticky=W)
        self.e1 = Entry(
            self.root, textvariable=self.aFC).grid(row=1, column=0, rowspan=2)
        self.e2 = Entry(
            self.root, textvariable=self.aRMB).grid(row=1, column=2, rowspan=2)
        self.b1 = Button(
            self.root, text="---->", command=self.toRMB).grid(row=1, column=1)
        self.b2 = Button(
            self.root, text="<----",command=self.toFC).grid(row=2, column=1)
        self.f = Frame(self.root).grid(row=3, column=0, columnspan=3)
        self.r1 = Radiobutton(
            self.f, text = "USD", variable = self.fc, value = "USD").grid(row = 3, column = 0)
        self.r2 = Radiobutton(
            self.f, text="Euro", variable=self.fc, value="Euro").grid(row=3, column=1)
        self.r3 = Radiobutton(
            self.f, text = "Yen", variable = self.fc, value = "Yen").grid(row = 3, column = 2)
        self.r4 = Radiobutton(
            self.f, text="Pound", variable=self.fc, value="Pound").grid(row=3, column=3)
        self.qb = Button(
            self.root, text="Quit", command=self.close).grid(row=5, column=1)
        self.root.mainloop()

    def showInfo(self):
        rStr = "%.2f"
        if self.to == "RMB":
            r = self.cal.calRMB(self.fc.get(), self.amt)
            self.aRMB.set(rStr % r)
        else:
            r = self.cal.calFC(self.fc.get(), self.amt)
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
        self.root.quit()
        self.root.destroy()


class CCCal:
    def __init__(self):
        self.xRate = {"USD": 6.306, "Euro": 8.2735,
                      "Yen": 0.0775, "Pound": 10.0486}

    def calRMB(self, fc, amt):
        return amt * self.xRate[fc]

    def calFC(self, fc, amt):
        return amt / self.xRate[fc]


if __name__ == '__main__':
    cc = CCCal()
    inter = GUICal(cc)
