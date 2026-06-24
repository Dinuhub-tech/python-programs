def mcq1():
  count=0
  print("Today is MCQ Quiz")
  print("ALL THE BEST and DO WELL")
  print("Q1.which data type is used for decimal\n")
  print("1.int\n2.float\n3.string\n4.numbers")
  n=int(input("select the answer\n"))
  if n==2:
    count+=1
  print("Q2.what is the output for print(9/3.0)\n")
  print("1.3\n2.none\n3.error\n4.3.0")
  n=int(input("select the answer\n"))
  if n==4:
    count+=1
  print("Q3.what is the factorial of 3\n")
  print("1.3\n2.6\n3.9\n4.1")
  n=int(input("select the answer\n"))
  if n==2:
    count+=1
  print("Q4.What is the output of print(2+3)")
  print("1.23\n2.Error\n3.5\n4.32")
  n=int(input())
  if n==3:
    count+=1
  print("Q5.Which keyword is used to create a function in Python")
  print("1.func\n2.function\n3.def\n4.eval")
  n=int(input("Enter your answer\n"))
  if n==3:
    count+=1
  print(f"YOUR SCORE IS {count} out of 5 ")
def mcq2():
  score = 0
  print("\n1. What is 25% of 200?")
  print("A) 25")
  print("B) 50")
  print("C) 75")
  print("D) 100")
  ans = input("Enter your answer (A/B/C/D): ").upper()
  if ans == "B":
    score += 1
# Question 2
  print("\n2. If a train travels 60 km in 1 hour, how far will it travel in 3 hours?")
  print("A) 120 km")
  print("B) 150 km")
  print("C) 180 km")
  print("D) 240 km")
  ans = input("Enter your answer (A/B/C/D): ").upper()
  if ans == "C":
    score += 1
  print("\n3. The average of 10, 20, and 30 is:")
  print("A) 15")
  print("B) 20")
  print("C) 25")
  print("D) 30")
  ans = input("Enter your answer (A/B/C/D): ").upper()
  if ans == "B":
    score += 1
  print("\n4. What is the next number in the series?")
  print("2, 4, 8, 16, __")
  print("A) 18")
  print("B) 24")
  print("C) 30")
  print("D) 32")
  ans = input("Enter your answer (A/B/C/D): ").upper()
  if ans == "D":
    score += 1
  print("\n5. A shopkeeper buys an item for ₹500 and sells it for ₹600. What is the profit?")
  print("A) ₹50")
  print("B) ₹75")
  print("C) ₹100")
  print("D) ₹150")
  ans = input("Enter your answer (A/B/C/D): ").upper()
  if ans == "C":
    score += 1
  print(f"YOUR SCORE IS {score} out of 5 ")

print("WHICH QUIZ YOU WANT TO WRITE 1.APTITUDE  OR 2.PYTHON")
k=int(input())
if k==1:
  mcq2()
if k==2:
  mcq1()
