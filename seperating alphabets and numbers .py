x=input().lower()
a1=[]
a2=[]
for i in x:
  if i.isdigit():
    a1.append(i)
  elif i.isalpha():
    a2.append(i)
print(a1)
print(a2)
