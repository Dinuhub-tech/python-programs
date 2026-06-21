print("1.Balance\n2.Deposit\n3.Withdraw")
x=int(input())
Balance=10000
default_pin=1234

pin=int(input("enter the pin"))
if pin==default_pin:
  if x==1:
    print("The balance amount in your bank is ",Balance)
  elif x==2:
    print("Enter the amount you want to deposit :")
    deposit=int(input())
    print("The amount after deposit is: ",(deposit+Balance))
  elif x==3:
    withdraw=int(input("Enter the amount you want to withdraw"))
    if withdraw <=Balance :
      print("The amount after withdrawl is ",(Balance-withdraw))
    else:
      print("Insufficient balance in your account")
  else:
    print("enter the data from 1-3 only")
else:
  count=0
  while count<2:
    print("enter the correct pin")
    pin=int(input())
    count+=1
  if count==2:
    print("Your account is blocked")
