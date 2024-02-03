### Game ###
import random

def game():
  """
  Number guessing game from range 1-100
  """
  pc = random.randint(1,100)
  while True:
    try:
      user = int(input("Guess the number: "))
      if user < pc:
          print("Too small!")
          continue
      elif user > pc:
          print("Too big!")
          continue
      else:
          print("You win!")
      break
    except:
        print("It's not a number!")
  
if __name__ == '__main__':
    game()