n=int(input())
temp=n
sum=0
while n>0:
  r=n%10
  sum+=r
  n=n//10
if temp%sum==0:
  print("Arshad number")
else:
  print("not")
