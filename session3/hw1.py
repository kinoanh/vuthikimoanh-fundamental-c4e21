from turtle import*

colors = ['red', 'blue', 'brown', 'yellow', 'grey']

distance = 100

for i in range(5):

    pencolor(colors[i])

    for j in range(i + 3):

        forward(distance)
        a= 360 / (i + 3)
        left(a)

mainloop()