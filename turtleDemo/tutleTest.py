import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "gray", "brown", "sea green"]
your_name = raw_input("what is your name:")
sides = int(raw_input("how many sides do you want(1-10):"))
for x in range(100):
    t.pencolor(colors[x % sides % 10])
    t.penup()
    t.forward(x * 4)
    t.pendown()
    t.width(20)
    t.write(your_name, font=("Arial", 8, "normal"))
    t.left(360/sides + 2)
turtle.done()