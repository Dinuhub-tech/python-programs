capital="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small="abcdefghijklkmnopqrstuvwxyz"
numbers="0123456789"
special="~!@#$%^&*()_+?,.;'}]{["
x=input()
count=0
count1=0
count2=0
count3=0
if len(x)>=8:
  for i in x:
    for j in capital:
      if i==j:
        count+=1
  if count>=1:
    for i in x:
      for j in small:
        if i==j:
          count1+=1
  if count1>=1:
    for i in x:
      for j in numbers:
        if i==j:
          count2+=1
  if count2>=1:
    for i in x:
      for j in special:
        if i==j:
          count3+=1
  if count>=1 and count1>=1 and count2>=1 and count3>=1:
    print("Strong Password")
  else:
    print("Give strong password")
else:
  print("Give strong password")
