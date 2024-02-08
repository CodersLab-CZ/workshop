import random
def lotto_game():
    user_numbers = set()

    while len(user_numbers) < 6:
        try:
            user_input = int(input("Zadejte číslo (1-49): "))
            if 1 <= user_input <= 49 and user_input not in user_numbers:
                user_numbers.add(user_input)
            else:
                print("Neplatný vstup, zadejte platné číslo v rozsahu 1-49.")
        except ValueError:
            print("Neplatný vstup, zadejte platné číslo v rozsahu 1-49.")

    sorted_user_numbers = sorted(user_numbers)
    print("Vaše vybraná čísla:", sorted_user_numbers)

    drawn_numbers = set(random.sample(range(1, 50), 6))
    print("Vylosovaná čísla:", drawn_numbers)

    matched_numbers = set(sorted_user_numbers).intersection(drawn_numbers)
    print("Počet shodných čísel:", len(matched_numbers))

if __name__ == "__main__":
    lotto_game()
