from random import randint


def roll(throw, dice=6, modifier=0):
    """
    Funkce přijímá jeden povinný argument (throw) a dva volitelné
    argumenty. Vypočítá hodnotu jednotlivých hodů, sečte a 
    případně připočítá modifikátor a vrátí výsledek.
    """
    throw_list = list(randint(1, dice+1) for _ in range(throw))
    return sum(throw_list) + modifier


print(roll(5, 7, 2))