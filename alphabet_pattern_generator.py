x=input("Enter your name to covert into pattern format\n").lower()
n=5
for i in x:
    if i=="a":
        print()
        print()
        for i in range(n):
            for j in range(n):
                
                if  (i==0 and j==n//2) or (j==0 and i==n-1) or (j==1 and i ==2) or (i==n//2 and j==n//2) or(j==3 and i ==2) or (j==n-1 and i==n-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="b":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if (i==0 and j!=n-1) or j==0 or (j==n-1 and (i==1 or i==2 or i==3)) or (i==n-1 and j!=n-1)or i==2:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="c":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if i==0 or j==0  or i==n-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="d":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if (i==0 and j!=n-1)or j==0 or (j==n-1 and (i==1 or i==2 or i==3)) or (i==n-1 and j!=n-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="e":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if i==0 or j==0 or i==2 or i==n-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="f":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if i==0 or j==0 or i==2 :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="g":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if i==0 or j==0 or i==2 or i==n-1 or (i==n-2 and j==n-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="h":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if   j==0 or i==2 or j==n-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="i":
        print()
        print()     
        for i in range(n): 
            for j in range(n):
                if i==0 or i==n-1 or j==2:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="j":
        print()
        print() 
        for i in range(n):
            for j in range(n): 
                if i==0 or (i==n-1 and (j==0 or j==1)) or j==2:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="k":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if j==0 or (i==1 and j==2) or (i==0 and j==3) or (i==2 and j==1) or (i==4 and j==3) or (i==3 and j==2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="l":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if j==0 or i==n-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="m":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if j==0 or (i==1 and (j==1 or j==3)) or j==n-1 or (i==2 and j==2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="n":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if j==0 or i==j or j==n-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="o":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if i==0 or j==0 or j==n-1 or i==n-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="p":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if i==0 or j==0 or i==2 or (i==1 and j==n-1) :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="q":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if i==0 or j==n-1 or i==2 or( j==0 and i==1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="r":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if i==0 or j==0 or i==2 or j==n-1 :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="s":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if i==0 or (i==1 and j==0) or i==2 or (i==n-2 and j==n-1) or i==n-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="t":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if i==0 or j==n//2 :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="u":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if i==n-1 or j==0 or j==n-1 :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="v":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if (i==0 and j==0)or (i==2 and j==1) or (j==n//2 and i==(n-1)) or (i==0 and j==n-1) or (i==2 and j ==n-2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="w":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if (i==n//2 and j==n//2) or j==0 or j==n-1 or (i==n-2 and(j==1 or j==n-2)):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="x":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if i==j or i==(n-j-1) :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="y":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if (i==0 and j==0) or (i==1 and j==1)or i==(n-j-1) :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="z":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if i==0 or i==n-1 or i==(n-j-1) :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i==" ":
        print()
        print()
    else:
        print(" Enter Alphabets Only")
