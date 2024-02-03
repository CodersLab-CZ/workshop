# here is the version with the user inputs as asked in the course

def user_answer() -> str:
    possible_answers = ["small", "big", "ok"]
    while True:
        answer = input()
        if answer not in possible_answers:
            print(f"You can answer only one of {possible_answers}")
            continue
        else:
            return answer


def run():
    low, high = 1, 1000
    print(f"OK, I (the user) am thinking of number between {low} and {high} and you (the computer) must guess it")
    print("After each guess I will give you answer, if your guess was too small or big\n'\n")

    while low <= high:
        mid = (low + high) >> 1

        print(f"I (the computer) am guessing {mid}. Is it small or big?")

        answer = user_answer() 
        if answer == "big":
            high = mid - 1
        elif answer == "small":
            low = mid + 1
        else:
            return mid
                
if  __name__ == "__main__":
    run()


