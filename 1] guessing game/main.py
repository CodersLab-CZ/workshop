from random import randint


def guess_num():
    """
    guess_num function take number from user input
    then compare it with chosen random number 1-100
    and react in proper way for tip <, > or ==
    """
    x = input("Guess the number:")
    try:
        x = int(x)
        if x < number:
            print("Too small!")
            return guess_num()
        elif x > number:
            print("Too big!")
            return guess_num()
        elif x == number:
            print("You win!")
    except ValueError:
        print("It's not a number!")
        return guess_num()


number = randint(1, 100)

if __name__ == '__main__':
    guess_num()
