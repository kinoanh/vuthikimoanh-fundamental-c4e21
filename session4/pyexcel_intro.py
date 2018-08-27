import pyexcel
#1.prepare data
data=[{
    "name":"huy",
    "age":29,   
},
{
    "name":"quan",
    "age":19,   
},
{
    "name":"duc",
    "age":32,   
},]
#2.save
pyexcel.save_as(records=data,dest_file_name="sample.xlsx")