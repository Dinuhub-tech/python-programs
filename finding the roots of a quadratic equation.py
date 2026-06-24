import math
a=int(input())
b=int(input())
c=int(input())
t=b*b - 4*a*c
d=math.sqrt(abs(t))

if t>0 :
  r1=(-b+d)/2*a
  r2=(-b-d)/2*a
  print(f"Roots are real and not equal i.e {r1,r2}")
elif  t==0:
  r1=(-b+d)/2*a
  r2=(-b+d)/2*a
  print(f"Roots are real and equal i.e {r1,r2}")
else:
  print(f"Roots are imaginary i.e {-1*b}+j{d} and {-1*b}-j{d}")
