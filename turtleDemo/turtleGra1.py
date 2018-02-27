# -*- coding:utf-8 -*-
import turtle
pen = turtle.Pen()
pen.pensize(5)
pen.pencolor(1,1,0)
pen.fillcolor(1,0,0)
pen.begin_fill()
for i in range(5):
    pen.forward(200)
    pen.right(144)
pen.end_fill()
turtle.mainloop()