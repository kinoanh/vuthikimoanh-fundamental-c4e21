from collections import OrderedDict 
p1={
    "name":"huy",
    "level": 25,
    "hrs": 14,
}
p2={
    "name":"hoa",
    "level": 20,
    "hrs": 7,
}
p3={
    "name":"tam",
    "level": 14,
    "hrs": 20,

}
thislist=[p1, p2, p3]
total_wage=0
wage=0
wage_list=[]
for i in thislist:
    print(i['hrs'])
    h=i["hrs"]
    n=i["name"]
    l=i["level"]
    w=OrderedDict({
        "name":n,
        "wage":h*l,
    })
    wage_list.append(w)
    wage= h*l
    total_wage += wage
    print(n,"wage", wage)
print("total", total_wage)
print(wage_list)
import pyexcel
pyexcel.save_as(records=wage_list,dest_file_name="dict_output.xlsx")
