import turtle

colors = ['red', 'yellow', 'blue', 'green']
turtle.bgcolor('black')
t = turtle.Pen()
t.pencolor('red')
for i in range(1, 100):
    t.forward(i)
    t.pencolor(colors[i % 4])
    t.left(92)
turtle.mainloop()
