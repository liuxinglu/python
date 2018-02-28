# -*- coding:utf-8 -*-
import turtle
turtle.color("red")
num = 0
while num < 5:
    stamp_id = turtle.stamp()
    turtle.fd(50)
    num += 1
turtle.color("black")
turtle.clearstamp(stamp_id)
turtle.clearstamps(1)
turtle.mainloop()