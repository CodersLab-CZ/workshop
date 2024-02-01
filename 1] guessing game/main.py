from random import randint as ri

def run():
    hidden_number = ri(1, 100)

    while True:
        try:
            user_number = int(input("Guess the number: "))
        except ValueError as err:
            print(f"Your input: {user_number} is not a real number. Try again")
            continue
        
        if user_number < hidden_number:
            print("too small")
        elif user_number > hidden_number:
            print("too big")
        else:
            print("you won")
            return


if __name__ == "__main__":
    run()