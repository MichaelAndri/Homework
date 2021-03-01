def magic_number():
    number = 7
    guesses = False
    while guesses == False:
        guess = int(input("Guess the magic number:\n"))
        if number < guess:
            print("too high")
        if number > guess:
            print("too low")
        if number == guess:
            print("\nWell done!")
            True
            break


magic_number()