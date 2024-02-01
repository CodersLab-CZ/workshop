# this problem is classical application of binary search algorithm but add some more complexity because of the user inputs
# here is the version without user inputs (user is automated)

from random import randint as ri

def binary_search():
    low, high = 1, 1000
    user_number = ri(1, 1000)
    print(f"I am the user, and I am thinking of the number {user_number}")

    while low <= high:
        mid = (low + high) >> 1
        
        if user_number < mid:
            print(f"You guessed {mid}, and it is too big")
            high = mid - 1
        elif user_number > mid:
            print(f"You guessed {mid}, and it is too small")
            low = mid + 1
        else:
            print(f"You guessed {mid}, and it is correct!")
            return mid

if  __name__ == "__main__":
    binary_search()
