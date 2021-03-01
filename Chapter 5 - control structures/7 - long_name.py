def long_name(n):
    if len(n) > 14:
        print("True")
    else:
        print("False")


name = input("input name: ")

long_name(name)