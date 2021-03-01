def higher_num(a, b):
  if a<b:
    highest = b
  else: 
    highest = a
  
  print("The highest number is " + str(highest))

a = int(input("Input the first number: "))
b = int(input("Input the second number: "))

higher_num(a, b)