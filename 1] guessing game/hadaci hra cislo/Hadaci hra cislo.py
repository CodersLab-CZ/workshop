import random

def hra_hadani_cisel():
    vylosovane_cislo = random.randint(1, 100)

    while True:
        tip = input("Guess the number: ")

        if not tip.isdigit():
            print("It's not a number!")
            continue

        tip = int(tip)

        if tip < vylosovane_cislo:
            print("Too small!")
        elif tip > vylosovane_cislo:
            print("Too big!")
        else:
            print("You win!")
            break

if __name__ == "__main__":
    hra_hadani_cisel()
