a1=int(input())
a2=int(input())
a3=int(input())
if a1==a2==a3:
  print("Equilateral traingle")
elif a1==a2 or a2==a3 or a1==a3:
  print("Isosceles triangle")
elif a1*a1+a2*a2==a3*a3 or a2*a2+a3*a3==a1*a1 or a1*a1+a3*a3==a2*a2:
  print("Right angled triangle")
else:
  print("Scalene triangle")
