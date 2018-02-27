# -*- coding:utf-8 -*-
import turtle
import datetime

class Clock(object):
    def __init__(self):
        super(Clock, self).__init__()
        turtle.mode('logo')
        self.pen = turtle.Pen()

    def week(self, t):
        week = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
        return week[t.weekday()]

    def date(self, t):
        y = t.year
        m = t.month
        d = t.day
        return '%s-%d-%d' % (y, m, d)

    def skip(self, step):
        self.pen.up()
        self.pen.forward(step)
        self.pen.down()

    def setupClock(self, radius):
        self.pen.reset()
        self.pen.pensize(7)
        self.pen.pencolor((0.2, 0.6, 0.5))
        for i in range(60):
            self.skip(radius)
            if i % 5 == 0:
                self.pen.forward(20)
                self.skip(-radius - 20)
            else:
                self.pen.dot(5)
                self.skip(-radius)
            self.pen.right(6)
        self.pen.up()

    def mkHand(self, name, length):
        self.pen.reset()
        self.skip(-length * 0.1)
        self.pen.begin_poly()
        self.pen.forward(length * 1.1)
        self.pen.end_poly()
        handForm = self.pen.get_poly()
        turtle.register_shape(name, handForm)

    def tick(self):
        t = datetime.datetime.today()
        second = t.second + t.microsecond * 0.000001
        minute = t.minute + second / 60.0
        hour = t.hour + minute / 60.0
        self.secHand.setheading(6 * second)  # 设置朝向 每秒转6度
        self.minHand.setheading(6 * minute)
        self.hurHand.setheading(30 * hour)
        self.pen.tracer(False)
        self.printer.forward(65)
        self.printer.write(self.week(t), align = 'center', 
                            font = ('Courier', 14, 'bold'))
        self.printer.back(130)
        self.printer.write(self.date(t), align = 'center',
                            font = ('Courier', 14, 'bold'))
        self.printer.back(50)
        self.printer.write('star.DJ', align = 'center', 
                            font = ('Courier', 14, 'bold'))
        self.printer.home()
        self.pen.tracer(True)

        turtle.ontimer(self.tick, 1000)
    
    def plane(self):
        turtle.hideturtle()
        turtle.up()
        turtle.setx(180)
        turtle.speed(0)
        turtle.down()
        turtle.pencolor(0.2, 0.2, 0.3)
        turtle.pensize(3)
        turtle.circle(180, None, 360)
    
    def draw(self):
        self.plane()
        self.pen.hideturtle()
        self.pen.tracer(False)
        self.mkHand('secHand', 135)
        self.mkHand('minHand', 110)
        self.mkHand('hurHand', 90)
        self.secHand = turtle.Pen()
        self.secHand.shape('secHand')
        self.minHand = turtle.Pen()
        self.minHand.shape('minHand')
        self.hurHand = turtle.Pen()
        self.hurHand.shape('hurHand')
        for hand in self.secHand, self.minHand, self.hurHand:
            hand.shapesize(1, 1, 3)
            hand.speed(0)
        self.printer = turtle.Pen()
        self.printer.hideturtle()
        self.printer.up()
        self.setupClock(150)
        self.pen.tracer(True)
        self.tick()
        turtle.mainloop()
        

if __name__ == '__main__':
    clock = Clock()
    clock.draw()
