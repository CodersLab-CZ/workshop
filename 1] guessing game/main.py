from random import randint


def num_guessing_game():
    """
    The function uses randint() and generates a number in
    the range 1-100. Then it uses "while loop" and it gets
    number tip from the player. The functions says the player
    if is his tip higher or lower until the player guesses 
    the number. 
    """
    print("Welcome to our guessing game! "
          "Can you guess the number between 1 and 100?")
    
    # getting a random number
    wanted_num = randint(1, 101)

    # getting a number of player
    while True:
        try:
            player_num = int(input("Enter whole number: "))

        # wrong value entery check    
        except ValueError:
            print("You entered the wrong value, try again...")
            continue

        # testing a player's number
        if player_num < wanted_num:
            print("Too small number...")
            continue
        elif player_num > wanted_num:
            print("Too big number...")
            continue
        else: 
            return "!!! YOU WIN !!!"




print(num_guessing_game())
