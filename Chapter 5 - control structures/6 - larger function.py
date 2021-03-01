def larger(a, b):
    if (a < b):
        highest = b
    else:
        highest = a

    print("The highest number is " + str(highest))


a = int(input("Input the first number: "))
b = int(input("Input the second number: "))

larger(a, b)