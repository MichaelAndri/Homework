score = int(input("What was your score?\n"))

if score>=50:
  print("You passed :)")
  if score>80:
    print("well done")

else:
  print("You failed :(")
  if score<=20:
    print("You need to try harder")