from random import shuffle

def lotto_user():
    """Funkce pro čísla uživatele, které si zadá na klávesnici"""

    print("Zadej unikátní čísla v rozsahu 1 - 49")
    
    try:
        numbers = []
        for x in range(6):
            number = int(input("Zadej číslo:"))
            if 0 < number <= 49 and number not in numbers:
                
                numbers.append(number)
            else:
                print("Číslo není v rozsahu nebo není unikátní")
                return None
        numbers.sort()
        return numbers
            
    except ValueError:
        print("Toto není číslo!")
        return None
         

def lotto_pc():
    """Funkce pro vylosování čísel Lotta"""
    numbers = list(range(1, 49))
    shuffle(numbers)
    lotto = numbers[:6]
    lotto.sort()
    
    return lotto


def lotto_hit(x, y):
    """Funkce pro porovnání listů"""   
    intersection_set = set(x) & set(y)

    if intersection_set:

        print("Seznamy mají společné hodnoty:", intersection_set)
        print("Počet společných hodnot:", len(intersection_set))
    else:
        print("Seznamy nemají žádné společné hodnoty.")


def lotto():
    """Hlavní funkce Lotta, která volá ostatní"""
    x = lotto_user()
    if x is None:
        return
    y = lotto_pc()
    print("Toto jsou tvoje čísla:")
    print(" ,".join(map(str, x)))
    print("Toto jsou vylosovaná čísla:")
    print(" ,".join(map(str, y)))
    return lotto_hit(x, y)

lotto()


