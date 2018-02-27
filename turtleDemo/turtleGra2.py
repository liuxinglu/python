# -*- coding:utf-8 -*-
from turtle import Turtle, mainloop

def tree(plist, length, radius, f):
    if length > 5:
        lst = []
        for p in plist:
            p.forward(length)
            q = p.clone()
            p.left(radius)
            q.right(radius)
            lst.append(p)
            lst.append(q)
        tree(lst, length * f, radius, f)

def main():
    p = Turtle()
    p.color('green')
    p.pensize(5)
    p.hideturtle()
    p.speed(10)
    p.left(90)
    p.penup()
    p.goto(0, -200)
    p.pendown()
    t = tree([p], 200, 65, 0.6375)
    mainloop()

if __name__ == '__main__':
    main()
        
