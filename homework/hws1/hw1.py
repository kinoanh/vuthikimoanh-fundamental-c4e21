from turtle import *
color("red")
left(30)
for i in range(4):
    forward(100)
    right(60)
    forward(100)
    right(120)
    forward(100)
    right(60)
    forward(100)
    right(30)
penup()
forward(300)
pendown()
color("blue")
for j in range(3):
    forward(100)
    left(120)

color("red")
for j in range(4):
    forward(100)
    left(90)

color("blue")
for j in range(5):
    forward(100)
    left(72)

color("red")
for j in range(6):
    forward(100)
    left(60)




mainloop()