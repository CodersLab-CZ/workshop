from random import randint


def num_guessing_game() -> int:
    """
    The function of guessing a random number between 1 and 100.

    The function using randint will generate a number, and using
    while loop accepts number tips from the user. once
    the user guesses the number, the program ends.
    """
    print("Welcome to our guessing game! "
          "Can you guess the number between 1 and 100?")
    
    # getting a random number
    wanted_num = randint(1, 101)

    # getting a number of player
    while True:
        try:
            player_num = int(input("Enter whole number: "))

            # testing a player's number
            if player_num < wanted_num:
                print("Too small number...")
                continue
            elif player_num > wanted_num:
                print("Too big number...")
                continue
            else: 
                return "!!! YOU WIN !!!"

        # wrong value entery check    
        except ValueError:
            print("You entered the wrong value, try again...")


print(num_guessing_game())
