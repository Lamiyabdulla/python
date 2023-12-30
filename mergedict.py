dict1={}
dict2={}
n=int(input("number of elements"))
for x in range(n):
    name=input("enter the name")
    salary=int(input("salary"))
    dict1[name]=salary
for x in range(n):
    names=input("enter the name of student")
    mark=int(input("enter the mark"))
    dict2[names]=mark
print("first dict",dict1)
print("second dict",dict2)
dict1.update(dict2)
print(dict1)
