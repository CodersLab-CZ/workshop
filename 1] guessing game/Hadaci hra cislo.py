import random
def guess_the_number():
    secret_number = random.randint(1, 100)

    while True:
        try:
            user_guess = int(input("Hádej číslo: "))

            if user_guess < secret_number:
                print("Příliš malé!")
            elif user_guess > secret_number:
                print("Příliš velké!")
            else:
                print("Vyhráváte!")
                break

        except ValueError:
            print("Není to číslo!")

if __name__ == "__main__":
    guess_the_number()
