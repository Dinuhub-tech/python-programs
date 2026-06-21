print("1.Bike \n2.Auto \n3.Car")
mode=int(input())
print()
if mode==1:
  print("How many kms you want to travel")
  kms=int(input())
  if kms >=1 and kms <=8:
    print("The amount to be paid is ",kms*5)
  else :
    if kms >=9 and kms <=15:
      print("The amount to be paid is ",((kms-8)*6+ 8*5))
    else:
      if kms >=16 and kms <=25:
        print("The amount to be paid is ",8*5+7*6+(kms-15)*8)
      else:

        if kms >=26 and kms <=30:
            print("The amount to be paid is ",8*5+7*6+8*8+(kms-25)*10)
        else:

          if kms >30 :
            print("There is no ride for that distance")
elif mode ==2:
  print("How many kms you want to travel")
  kms=int(input())
  if kms >=1 and kms <=10:
    print("The amount to be paid is ",kms*8)
  else :
    if kms >=11 and kms <=19:
      print("The amount to be paid is ",((kms-10)*10+ 10*8))
    else:
      if kms >=20 and kms <=35:
        print("The amount to be paid is ",10*8+9*10+(kms-19)*12)
      else:

        if kms >=36 and kms <=60:
            print("The amount to be paid is ",10*8+9*10+16*12+(kms-35)*15)
        else:

          if kms >60 :
            print("There is no ride for that distance")
elif mode ==3:
  print("How many kms you want to travel")
  kms=int(input())
  if kms >=1 and kms <=50:
    print("The amount to be paid is ",kms*12)
  else :
    if kms >=51 and kms <=80:
      print("The amount to be paid is ",((kms-50)*15+ 50*12))
    else:
      if kms >=81 and kms <=120:
        toll=int(input("enter the toll amount:\n"))
        tip=int(input("enter the tip amount:\n"))
        print("The amount to be paid is ",50*12+30*15+(kms-80)*17+toll+tip)
      else:

        if kms >=120 and kms <=200:

          toll=int(input("enter the toll amount:\n"))
          tip=int(input("enter the tip amount:\n"))
          food=int(input("enter the amount for food\n"))
          print("The amount to be paid is ",50*12+30*15+40*17+(kms-120)*18+toll+tip+food)
        else:

          if kms >200 :
            print("There is no ride for that distance")

else:
  print("print from the valid data")
