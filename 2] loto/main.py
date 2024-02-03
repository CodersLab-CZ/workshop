import random


def get_user_numbers():
    user_numbers = set()
    while len(user_numbers) < 6:
        try:
            user_input = input("Enter a number (1-49): ")
            number = int(user_input)
            if number < 1 or number > 49:
                print("Number must be between 1 and 49.")
            elif number in user_numbers:
                print("You have already entered this number.")
            else:
                user_numbers.add(number)
        except ValueError:
            print("That's not a valid number.")
    return sorted(user_numbers)


def draw_lotto_numbers():
    return sorted(random.sample(range(1, 50), 6))


def compare_numbers(user_numbers, lotto_numbers):
    return len(set(user_numbers).intersection(set(lotto_numbers)))


def main():
    print("Welcome to the LOTTO Simulator!")
    user_numbers = get_user_numbers()
    print("\nYour numbers: ", user_numbers)

    lotto_numbers = draw_lotto_numbers()
    print("LOTTO draw: ", lotto_numbers)

    matches = compare_numbers(user_numbers, lotto_numbers)
    if matches >= 3:
        print(f"Congratulations! You have matched {matches} number(s).")
    else:
        print("Unfortunately, you did not match enough numbers to win a prize.")


if __name__ == "__main__":
    main()
