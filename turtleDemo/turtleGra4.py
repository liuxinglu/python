#coding:utf-8
# lt, arr = [j for j in range(1, 100)], []
# index, countLen = 0, 3
# for i in range(3):
#     arr.append(lt[i * countLen : i * countLen + countLen])
# print arr
import turtle
import math
pen = turtle.Pen()
turtle.colormode(255)
pen.pensize(3)
pen.penup()
pen.goto(-100, -100)
pen.tracer(True)
pen.pendown()
r, g, b = 0, 0, 0
for i in range(1, 50):
    for j in range(1, 6):
        for k in range(1, 50):
            r += i
            g += j
            b += k
            r %= 256
            g %= 256
            b %= 256
            pen.pencolor(r, g, b)
            pen.forward(r)
            pen.left(90)
    pen.left(24)
turtle.mainloop()