x=input()
a=""
for ch in x:
    if ch in "aeiou":
        a+="@"
    else:
        a+=ch
print(a)
