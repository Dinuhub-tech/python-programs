a=int(input())
b=int(input())
print("PRESS THE NUMBER TO PERFORM WHICH OPERATION YOU WANT TO PERFOM")
print("1.Addition         2.Subtraction\n3.Multiplication   4.Division\n5.square           6.cube")
x=int(input())
if x==1:
  print("Addition of a and b is :",a+b)
elif x==2:
  print("Subtraction of a and b is :",a-b)
elif x==3:
  print("Multiplication of and b is :",a*b)
elif x==4:
  print("Division of a and b is :",a/b)
elif x==5:
  print("Squares of a and b is :",a**2,b**2)
elif x==6:
  print("Cubes of a and b is :",a**3,b**3)
else:
  print("enter a valid number from the above data")
