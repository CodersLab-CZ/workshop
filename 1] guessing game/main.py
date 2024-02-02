from random import randint
number = randint(1, 100)
win = False
while win == False:
    #system generates a number in range 1-100 and user tries to guess it
    #system provides clues Too small/too big and validates whether input is a number
    try:
        user_input = int(input("Guess a number between 1 and 100: "))
        if user_input < number:
            print("Too small")
        elif user_input > number:
            print("Too big")
        else:
            print("You win!")
            win = True
    except ValueError:
        print("It's not a number!")