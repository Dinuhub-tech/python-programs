def fact(r):
  fact=1
  while r>=1:
    fact*=r
    r-=1
  return fact
def split1(n):
  sum=0
  while n>0:
    r=n%10
    sum+=fact(r)
    n=n//10
  return sum
n=int(input())
temp=n
zuu=split1(n)
if temp==zuu:
  print("YES")
else:
  print("NO")
