n=int(input())
s=n*n
k=""
count=0
while s>0:
  r=s%10
  k=str(r)+k
  count+=1
  if count<len(str((n))):
    s=s//10
  else:
    break
if k==str(n):
  print("Automorphic")
else:
  print("NOT")
