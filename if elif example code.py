name=input()
marks=int(input())
amount=int(input())
if marks>=90:
  grade="A"
elif marks>80:
  grade="B"
elif marks>70:
  grade="C"
elif marks>40:
  grade="D"
else:
  grade="F"
if grade=="A":
  disc=0
elif grade=="B":
  disc=20
elif grade=="C":
  disc=15
elif grade=="D":
  disc=10
else :
  disc= amount

tot1=(disc*amount/100)
total=50000-tot1
print(f"Name:{name}\nmarks:{marks}\nGrade:{grade}\nAmount_To_Be_paid :{total}")
