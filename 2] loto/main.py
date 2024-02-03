from random import choice

def collect_user_picks() -> set[int]:
    print("Please pick 6 numbers. Each in range between 1-49\n")

    picks = set()
    count = 1
    while count != 7:
        try: 
            pick = int(input(f"Please pick {count}. number: "))
            if not (1 <=  pick <= 49):
                print(f"Number {pick} has to be within 1-49 range, try again")
                continue
            if pick in picks:
                print(f"Number {pick} can be picked only once, try again")
                continue
        except ValueError as e:
            print("This is not a number, try again")
            continue

        count +=1
        picks.add(pick)

    return picks


def get_winning_numbers() -> set[int]:
    all_numbers = [i for i in range(1, 50)]
    winning_numbers = {choice(all_numbers) for _ in range(6)}

    return winning_numbers


def run():

    user_picks = collect_user_picks()
    print(f"User picked: {sorted(user_picks)}")

    winnig_numbers = get_winning_numbers()
    print(f"Winning numbers are: {winnig_numbers}")

    intersection = user_picks & winnig_numbers
    print(f"user picked {len(intersection)} numbers that were in winning numbers.")



if __name__ == "__main__":
    run()