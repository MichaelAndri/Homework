def largest(a, b, c):
  if(a<b<c):
    highest = c
  if(b<c<a): 
    highest = a
  if(c<a<b):
    highest = b
  print("The highest number is " + str(highest))

a = int(input("Input the first number: "))
b = int(input("Input the second number: "))
c = int(input("Input the third number: "))

largest(a, b, c)