a,b,c =map(int,input().split())
if a<b and a<c:
  print(f"{a} is smaller")
elif b<a and b <c:
  print(f"{b} is smaller")
else :
  print(f"{c} is smaller")
