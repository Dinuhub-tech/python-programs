college=input()
if college=="yes":
  block =input()
  if block=="yes":
    floor =input()
    if floor=="yes":
      room=input()
      if room=="yes":
        print("You are in the room")
      else:
        print("you are in the floor")
    else:
      print("You are in block")
  else:
    print("You are in college")
else:
  print("Holiday is for me")
