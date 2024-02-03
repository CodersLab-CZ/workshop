from random import shuffle

def user_turn():
  user_list = []
  x = 0
  while x < 6:
    try:
       user = int(input("Choose a number: "))
       if user <= 49 and user not in user_list:
         user_list.append(user)
         x += 1
       else:
         print("you have duplicity number or bigger that 49")
         return None
    except:
        print("You must write numbers!")
        return None
  user_list.sort()   
  return user_list 


def turn_parse(list):
    return ', '.join(map(str, list))


def pc_turn():
  pc_list = list(range(1,49))
  shuffle(pc_list)
  return sorted(pc_list[:6])
 
def hit(a,b):
    intersection_set = set(a) & set(b)
    return("You hit", len(intersection_set), "number!.")


def lotto():
    user = user_turn()
    if user is None:
        return
    pc = pc_turn()
    
    print("Your numbers: ")
    parse_user = turn_parse(user)
    print(parse_user)

    print("Lotto numers: ")
    parse_pc = turn_parse(pc)
    print(parse_pc)

    result = hit(user,pc)
    print(result)
    

lotto()

