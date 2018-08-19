a =  int(input("a="))
b = int(input("b="))
c = int(input("c="))
n = b*b-4*a*c
if n>0 :
    x1=(-b+n**0.5)/(2*a)  
    x2=(-b-n**0.5)/(2*a) 
    print("x1",x1)
    print("x2",x2 )
elif n==0:
    x= -b/(2*a)
    print("x", x )
else:
    print("error")
