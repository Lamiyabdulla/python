x=int(input("enter the limit of fibanoceseries to print:"))
a=0
b=1
print(a)
print(b)
for i in range(1,x-1):
    a,b=b,a+b
    print(b)
