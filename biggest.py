x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
z=int(input("Enter the third number:"))
if(x>y):
  if(x>z):
    print(x,"is BIG")
  else:
      print(y,"is BIG")
else:
      if(y>z):
          print(y,"is BIG")
      else:
           print(z,"is BIG")