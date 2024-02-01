from random import randint


def nums_of_player() -> list:
    """
    The function retrieves a list of six original numbers
    from the player.

    Funktion checks whether:
        player entered integer in range of 1-49,
        player has not entered a given number before.

    Funktion return a sorted list of numbers.
    """
    # gettint a list of numbers
    player_nums = []
    while len(player_nums)<6:
        try:
            num = int(input(f"Enter number No. {len(player_nums) +1}: "))
            # check a number
            if num in player_nums:
                print("The number has already been entered. Try again...")
            elif num < 1 or num > 49:
                print("The number is not in range of 1 - 49. Try again...")
            else:
                player_nums.append(num)

        except ValueError:
            print("Value is not whole number. Try again...")
    
    player_nums.sort()
    return player_nums


def winning_nums() -> list:
    """
    The function uses randint (Random library) and gets a list 
    of six original numbers from the range 1-49.
    """
    draw_nums = []
    while len(draw_nums) < 6:
        draw_nums.append(randint(1, 50))

    return draw_nums


def main():
    """
    The function uses the "nums_of_player()" function and gets the list
    numbers from a player. Then uses the "winning_nums()" function and gets
    list of drawn numbers. 
    The function dislays lists of numbers and compares them. Then
    displays how many numbers the player guessed.
    """
    print(f"WELCOME TO THE PYTHON LOTTERY!\n{'=' * 30}\nWe draw "
          "sixt numbers in range of 1-49. Try to guess them...")
    
    # getting numbers of player
    player_nums = nums_of_player()
    print(f"Your numbers:\n{', '.join(map(str, player_nums))}")

    # getting winning numbers
    draw_nums = winning_nums()
    print(f"Winning numbers:\n{', '.join(map(str, draw_nums))}")

    # evaluation of results
    hits = 0
    for num in player_nums:
        if num in draw_nums:
            hits += 1
    separator = "=" * 25
    print(f"{separator}\nSUM OF GUESSED NUMBERS: {hits}\n{separator}")


main()
