thislist=["death note" , "netflix", "teaching"]
a=len(thislist)
for i in range(a) :
    print(str(i+1) +"."+ thislist[i])
print("*" *10)
c=int(input("which position do you want to update?"))

b=input("your replacing favourite:" )
thislist[c-1]=b

for i in range(a) :
    print(str(i+1) +"."+ thislist[i])
    