from  turtle import*

colors = ['red', 'blue', 'brown', 'yellow', 'grey']
a=100
b= 250

for i in range(len(colors)):
    
    color(colors[i])
    begin_fill()

    for j in range(4):        
        if j % 2 :
            forward(a)
        else: 
            forward(b)
        right(90)
    b -= 50    
    end_fill()

      


mainloop()