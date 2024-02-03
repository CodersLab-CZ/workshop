
print("Image a number between 0 and 1000!")
input("Press 'Enter' to continue \n")


min = 0
max = 1000

x = 0
while x < 10:
  x += 1
  
  answer = ["low","high","win"] 
  guess = int((max-min) // 2 ) + min
  print(f"Your number: {guess}")
  user = input()
  
 
  if x == 10:
    print("Don't cheat!")
  if user in answer:   
    if user == "low":
      min = guess
    elif user == "high":
      max = guess
    elif user == "win":
      print("You won!")
      break
  else:
    print(f"Only allow: {', '.join(answer)}") 
    x -= 1
  
