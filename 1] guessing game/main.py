import random

def guess_the_number():

    number_to_guess = random.randint(1, 100)

    while True:

        user_input = input("Guess the number: ")

        try:
            guess = int(user_input)
        except ValueError:
            print("It's not a number!")
            continue


        if guess < number_to_guess:
            print("Too small!")
        elif guess > number_to_guess:
            print("Too big!")
        else:
            print("You win!")
            break


guess_the_number()
print("Thanks for playing!")


