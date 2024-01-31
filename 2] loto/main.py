import random


def get_computer_numbers():
    """Get 6 random numbers from the range of 1 – 49

    Returns:
        list: 6 random numbers from the range of 1 – 49
    """
    numbers = []
    while len(numbers) != 6:
        n = random.randint(40, 49)
        if n not in numbers:
            numbers.append(n)
    return sorted(numbers)


def get_player_numbers():
    """Ask player for 6 numbers from the range of 1 – 49

    Returns:
        list: 6 random from the range of 1 – 49
    """
    numbers = []
    while len(numbers) != 6:
        n = input(f"Guess 6 numbers from the range of 1 – 49: ")
        try:
            n = int(n)
        except ValueError:
            print("It's not a number!")
            continue
        if n in numbers:
            print(f"The {n} has already been entered")
            continue
        if n < 1 or n > 49:
            print(f"The {n} is outside range the range of 1-49")
        else:
            numbers.append(n)
    return sorted(numbers)


def game():
    """Start entering the player's numbers and view the result of the LOTTO game
    """
    player_numbers = get_player_numbers()
    print("The numbers you entered:", *player_numbers)
    computer_numbers = get_computer_numbers()
    print("LOTTO drawn:", *computer_numbers)

    match = 0
    for i in player_numbers:
        if i in computer_numbers:
            match += 1

    print("Number of guessed numbers:", match)


if __name__ == '__main__':
    game()
