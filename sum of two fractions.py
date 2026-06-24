n1=int(input())
d1=int(input())
n2=int(input())
d2=int(input())
NR=n1*d2+n2*d1
DR=d1*d2
if NR%DR!=0:
  print(f"{n1}/{d1} + {n2}/{d2}= {NR}/{DR}")
else:
  print(f"{n1}/{d1} + {n2}/{d2}= {NR/DR}")
