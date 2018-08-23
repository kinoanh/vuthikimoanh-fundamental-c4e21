thislist=["death note" , "netflix", "teaching"]
a=len(thislist)
for i in range(a) :
    print(str(i+1) +"."+ thislist[i])
print("*" *10)
c=int(input("which position do you want to delete?"))
thislist.pop(c-1)

a=len(thislist)
for i in range(a) :
    print(str(i+1) +"."+ thislist[i])