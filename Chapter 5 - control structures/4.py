score = int(input("What was your score?\n"))
if score>=80:
  grade = "A"
elif score>=79:
  grade = "B"
elif score>=40:
  grade = "C"
elif score>=30:
  grade = "D"
elif score<=30:
  grade = "U"
print("Grade:",grade)