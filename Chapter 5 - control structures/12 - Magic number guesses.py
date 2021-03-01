def magic_number():
    tries = 0
    number = 7
    guessed = False

    while tries <= 4:
        guess = int(input("Guess the magic number: "))
        if number < guess:
            tries += 1
            print("too high")
        elif number > guess:
            tries += 1
            print("too low")
        else:
            tries += 1
            print("Well done!")
            guessed = True
            break
    if guessed == False:
        print("\nYou have gotten your meximum chances.")
        return


magic_number()