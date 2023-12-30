list=[]
n=int(input("enter the number of elements"))
for i in range(n):
     value=int(input("enter the number"))
     list.append(value)
list_even=[x for x in list if x%2==0]
print("the even numbered list:",list_even)
