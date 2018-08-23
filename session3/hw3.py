items = ["T-Shirt", "Sweater"]

while True:
    command = input("what do you want (C, R, U, D)? ").upper()
    if command == "C":
        a = input("Enter new item: ")
        items.append(a)
        print("Our items:", end=" ") 
        print(*items, sep=", ")
    x=len(items)
    if command == "R":
        from random import randint
        i= randint(0,3)
        n=items[i]
        print(n)
    if command == "U":
        b = int(input("Update position? "))
        if b in range(1, len(items)+1):
            c = input("New item? ")
            items[b-1] = c
            print("Our items:", end=" ")
        if d in range(1, len(items)+1):
            items.pop(d-1)
            print("Our items:", end=" ") 
            print(*items, sep=", ") 
            print(*items, sep=", ")
        else: 
            print("error")
    if command == "D":
        d = int(input("Delete position? "))
        else:
            print("error")
    