favs=['net', 'tech','rebull']
for i , item in enumerate(favs):
        print(i,item)
command=input("what do you want (c r u d )?".upper())
while true:
    if command=="c":
        a=input("you want to add:")
        favs.append(str(a))
        print(favs)
    if command=="u":
        b=int(input(" you want to replace :"))
        y=input("change  to :")
        favs[b]=y
        print(favs)
    if command=="r":
        from random import choice   
        c= choice(favs)
        print(c)
    if command=="d":
        d=input(" you want to del:" )
        if d in favs:
            favs.remove(str(d))
            print(favs)


