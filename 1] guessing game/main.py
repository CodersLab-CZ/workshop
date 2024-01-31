import random


def game():
    """Start entering the player's numbers and view the result of the guess number from range 1 - 100
    """
    computer_number = random.randint(1, 100)
    while True:
        try:
            player_number = int(input("Guess the number: "))
        except ValueError:
            print("It's not a number!")
            continue
        if player_number < computer_number:
            print("Too small!")
        elif player_number > computer_number:
            print("Too big!")
        else:
            print("You win!")
            break


if __name__ == '__main__':
    game()
