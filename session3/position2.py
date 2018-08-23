thislist=["death note" , "netflix", "teaching"]
a=len(thislist)
for i in range(a) :
    print(str(i+1) +"."+ thislist[i])
print("*" *10)
c=input("which position do you want to get rid of ")
if c in thislist :
    thislist.remove(c)
    print(thislist)
else : print("error")