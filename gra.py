import turtle
import math
import string
import time
import Tkinter
import json

class Gra():
    def __init__(self):
        self.pen = turtle.Pen()
        self.rgb_r = 0
        self.rgb_g = 0
        self.rgb_b = 0

    def drawAniCircle(self):
        self.pen.pencolor((self.rgb_r, self.rgb_g, self.rgb_b))
        self.pen.pensize(4)
        self.pen.speed(0)
        while True:
            # self.pen.clear()
            self.drawCir()


    def drawCir(self):
        self.pen.down()
        r = 0
        
        while r < 6:
            self.pen.forward(r)
            self.pen.right(5)
            r = r + 0.01
            self.rgb_r = (self.rgb_r + 1) % 10
            self.rgb_g = (self.rgb_g + 1) % 10
            self.rgb_b = (self.rgb_b + 1) % 10
            self.pen.pencolor((self.rgb_r/10.0, self.rgb_g/10.0, self.rgb_b/10.0))
        self.pen.up()
        

    def drawGra3(self):
        colors = ['red', 'yellow', 'blue', 'green']
        turtle.bgcolor('black')
        t = turtle.Pen()
        t.pencolor('red')
        for i in range(1, 100):
            t.forward(i)
            t.pencolor(colors[i % 4])
            t.left(92)

    def drawGra2(self):
        turtle.bgcolor('black')
        t = turtle.Pen()
        t.pencolor('red')
        i = 0
        for i in list(range(0, 4)):
            t.up()
            t.forward(10)
            t.down()
            t.forward(30)
            t.up()
            t.forward(10)
            t.left(90)
            i = i + 1
        t.reset()
        while i < 6:
            t.backward(100)
            t.up()
            t.right(90)
            t.forward(20)
            t.left(90)
            t.down()
            t.forward(100)
            i = i + 1
        while i < 360:
            t.down()
            t.right(1)
            t.forward(1)
            i = i + 1
        t.up()

    def drawGra(self):
        turtle.bgcolor('black')
        t = turtle.Pen()
        t.pencolor('red')
        r = 1
        i = 0
        while i < 180:
            self._drawCircle(t, r)
            r = r + 0.1
            t.left(6)
            i = i + 1
        t.bye()
    
    def _drawCircle(self, t_pen, r_num):
        i_circle = 0
        t_pen.down()
        while i_circle < 36:
            t_pen.left(10)
            t_pen.forward(r_num)
            i_circle = i_circle + 1
        t_pen.up()

    def drawFlower(self, flowerNum, jiaodu, r = 5):
        pen_flower = turtle.Pen()
        pen_flower.down()
        while r > 2:
            i_curFlowerNum = 0
            while i_curFlowerNum < flowerNum:
                i_size = 18
                i_curSize = 0
                while i_curSize < i_size:
                    pen_flower.forward(r)
                    pen_flower.right(jiaodu / i_size)
                    i_curSize = i_curSize + 1
                pen_flower.right(180 - jiaodu)
                i_curSize = 0
                while i_curSize < i_size:
                    pen_flower.forward(r)
                    pen_flower.right(jiaodu / i_size)
                    i_curSize = i_curSize + 1
                pen_flower.right(180 - jiaodu)
                pen_flower.right(360 / flowerNum)
                i_curFlowerNum = i_curFlowerNum + 1
            r = r - 0.5
        pen_flower.bye()

    def drawNum(self, num):
        self.pen.pensize(2)
        n = Num(self.pen)
        n.drawNum(num)

    def clearPen(self):
        self.pen.reset()


class Num():
    def __init__(self, pen):
        self.pen = pen
    unitDis = 2 * math.cos(45) * 10 + 43

    def drawNum(self, num):
        strnum = str(num)
        arrlen = len(strnum)
        for i in range(arrlen):
            self.drawSplitNum(strnum[i])
            self.passUnit("h", 1)
            self.backUnit("v", 2)


    def drawSplitNum(self, num):
        if num == "0":
            self.hUnit(1)
            self.vUnit(2)
            self.reposition()
            self.vUnit(2)
            self.hUnit(1)
        elif num == "1":
            self.passUnit("h", 1)
            self.vUnit(2)
        elif num == "2":
            self.hUnit(1)
            self.vUnit(1)
            self.backUnit("h", 1)
            self.hUnit(1)
            self.backUnit("h", 1)
            self.vUnit(1)
            self.hUnit(1)
        elif num == "3":
            self.hUnit(1)
            for i in range(2):
                self.passUnit("v", 1)
                self.backUnit("h", 1)
                self.hUnit(1)
            self.backUnit("v", 2)
            self.vUnit(2)
        elif num == "4":
            self.vUnit(1)
            self.hUnit(1)
            self.backUnit("v", 1)
            self.vUnit(2)
        elif num == "5":
            self.hUnit(1)
            self.backUnit("h", 1)
            self.vUnit(1)
            self.hUnit(1)
            self.vUnit(1)
            self.backUnit("h", 1)
            self.hUnit(1)
        elif num == "6":
            self.hUnit(1)
            self.backUnit("h", 1)
            self.vUnit(2)
            self.backUnit("v", 1)
            self.hUnit(1)
            self.vUnit(1)
            self.backUnit("h", 1)
            self.hUnit(1)
        elif num == "7":
            self.hUnit(1)
            self.vUnit(2)
        elif num == "8":
            self.hUnit(1)
            for i in range(2):
                self.passUnit("v", 1)
                self.backUnit("h", 1)
                self.hUnit(1)
            self.backUnit("v", 2)
            self.vUnit(2)
            self.backUnit("h", 1)
            self.backUnit("v", 2)
            self.vUnit(2)
        elif num == "9":
            self.hUnit(1)
            self.vUnit(2)
            self.reposition()
            self.vUnit(1)
            self.hUnit(1)
            self.passUnit("v", 1)
            self.backUnit("h", 1)
            self.hUnit(1)
        
    def reposition(self, unitCount = 2):
        self.pen.left(90)
        self.pen.forward(unitCount * self.unitDis)
        self.pen.left(90)
        self.pen.forward(self.unitDis)
        self.pen.right(180)

    def passUnit(self, dir, count):
        self.pen.up()
        if dir == "h":
            self.pen.forward(count * self.unitDis)
        elif dir == "v":
            self.pen.right(90)
            self.pen.forward(count * self.unitDis)
            self.pen.left(90)
    
    def backUnit(self, dir, count):
        self.pen.up()
        if dir == "h":
            self.pen.left(180)
            self.pen.forward(count * self.unitDis)
            self.pen.right(180)
        elif dir == "v":
            self.pen.left(90)
            self.pen.forward(count * self.unitDis)
            self.pen.right(90)

    def hUnit(self, count):
        self.pen.fillcolor('yellow')
        self.pen.begin_fill()
        for i in range(count):
            self.pen.down()
            self.pen.left(45)
            self.pen.forward(10)
            self.pen.right(45)
            self.pen.forward(40)
            self.pen.right(45)
            self.pen.forward(10)
            self.pen.right(90)
            self.pen.forward(10)
            self.pen.right(45)
            self.pen.forward(40)
            self.pen.right(45)
            self.pen.forward(10)
            self.pen.up()
            self.pen.right(135)
            self.pen.forward(self.unitDis)            
        self.pen.end_fill()

    def vUnit(self, count):
        self.pen.fillcolor('yellow')
        self.pen.begin_fill()
        for i in range(count):
            self.pen.down()
            self.pen.right(45)
            self.pen.forward(10)
            self.pen.right(45)
            self.pen.forward(40)
            self.pen.right(45)
            self.pen.forward(10)
            self.pen.right(90)
            self.pen.forward(10)
            self.pen.right(45)
            self.pen.forward(40)
            self.pen.right(45)
            self.pen.forward(10)
            self.pen.fillcolor('yellow')
            self.pen.up()
            self.pen.right(135)
            self.pen.forward(self.unitDis)
            self.pen.left(90)
        self.pen.end_fill()

if __name__ == '__main__':
    gra = Gra()
    # gra.drawAniCircle()
    gra.drawFlower(6, 180)
    # for i in range(10):
    #     gra.drawNum(i*11)
    #     gra.clearPen()
    turtle.mainloop()   


