import turtle

class Gra():
    def __init__(self):
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
        de = "i value is "
        if i == 360:
            de = de + str(i)
            self.contents.set(de)
        else:
            self.contents.set(de)

    def drawGra(self):
        turtle.bgcolor('black')
        t = turtle.Pen()
        t.pencolor('red')
        r = 1
        i = 0
        while i < 180:
            self.drawCircle(t, r)
            r = r + 0.1
            t.left(6)
            i = i + 1
        t.bye()
    
    def drawCircle(self, t_pen, r_num):
        i_circle = 0
        t_pen.down()
        while i_circle < 36:
            t_pen.left(10)
            t_pen.forward(r_num)
            i_circle = i_circle + 1
        t_pen.up()

    def drawFlower(self, flowerNum, jiaodu, r):
        pen_flower = turtle.Pen()
        pen_flower.down()
        while r > 2:
            i_n = 0
            while i_n < flowerNum:
                i_t = 0
                while i_t < 18:
                    pen_flower.forward(r)
                    pen_flower.right(jiaodu / 18)
                    i_t = i_t + 1
                pen_flower.right(180 - jiaodu)
                i_t = 0
                while i_t < 18:
                    pen_flower.forward(r)
                    pen_flower.right(jiaodu / 18)
                    i_t = i_t + 1
                pen_flower.right(180 - jiaodu)
                pen_flower.right(360 / flowerNum)
                i_n = i_n + 1
            r = r - 0.5
        pen_flower.bye()

    def drawNum(self, num):
        pass

class Num():
    def hUnit(n):
        pen = turtle.Pen()
        for i in range(n)
            pass
            

if __name__ == '__main__':
    gra = Gra()
    turtle.mainloop()    
