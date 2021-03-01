word = str(input("Enter a word: "))

def vowel(word):
    score = 1

    for character in word:
        character = character.lower()
        if character == 'a':
            score += 5
        elif character == 'e':
            score += 4
        elif character == 'i':
            score += 3
        elif character == 'o':
            score += 2
        elif character == 'u':
            score += 1

    print("Your word is worth",score,"points")

vowel(word)