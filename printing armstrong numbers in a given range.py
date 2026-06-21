lower=int(input())
upper=int(input())

for num in range(lower,upper+1):
    temp =num
    sum=0
    while num>0:
        r=num%10
        sum+=r**3
        num=num//10
    if temp == sum:
        print(sum)
