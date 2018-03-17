# -*- coding:utf-8 -*-
import turtle
import random
pen = turtle.Pen()
pen.pensize(5)
pen.pencolor(1,1,0)
pen.fillcolor(1,0,0)

for j in range(4):
    pen.fillcolor(j*0.2, 0, 0)
    pen.begin_fill()
    pen.tracer(1.8)
    for i in range(5):
        pen.pencolor(i * 0.2, i * 0.1, i  * 0.1)
        pen.forward(200)
        pen.right(144)
    pen.end_fill()
turtle.mainloop()