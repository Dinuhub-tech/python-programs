x=int(input())
if x<0:
    print("enter positive numver")
else:
    sum=0
    for i in range(1,x+1):
        sum+=i
    print(sum)
