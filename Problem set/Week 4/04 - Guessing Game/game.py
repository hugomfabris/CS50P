import random
#We'll use this first while loop to ask the user for the level. The try/except block inside will catch possible non-integer values and prompt the user again
while True:
    try:
        level = int(input("Level: "))
        random_choose = random.randrange(1, level)
        break
    except ValueError:
        pass
#The second while loop will ensure the value guessed by the user is an integer (again, the try/except purpose) and prompt the user again with the tip(large or small)
while True:
    try:
        guess = int(input("Guess: "))
        if guess < random_choose:
            print("Too small!")
        elif guess > random_choose:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass