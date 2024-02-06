from random import randint


def calculation(x: int, y: int) -> int:
    """
    Vnořená funkce obsahující základní vzorec 
    pro výpočet hodu kostkou bez modifikátoru.
    """
    return x * (randint(1, y+1))


def dice_calculation(entered_value: str):
    """
    Funkce pro výpočet hodu kostkou. Funkce zkontroluje
    jestli byla zadána povolená kostka a správné hodnoty.
    Pokud ano, vrátí hodnotu hodu za použití funkce 
    calculation(). Pokud ne, vrátí chybové hlášení. 
    """
    error_dice = "WRONG DICE: a correct dice - D3, D4, D6, D8, D10, D12, D20, D100"
    error_value = "WRONG VALUE: a correct value is in format xDy+z."
    correct_dice = ("D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100")

    rolls = 0
    dice = 0
    modifier = 0
    math_mark = ""

    # získání typu kostky + kontrola
    for correct_dice in correct_dice:
        if correct_dice in entered_value:
            dice = int(correct_dice.strip("D"))
            first_cut = entered_value.split(correct_dice)
            break
    if dice == 0:
        return error_dice
    
    # získání počtu hodů + kontrola
    if first_cut[0]:
        try: 
            rolls = int(first_cut[0])
        except ValueError:
            return error_value
    else:
        rolls = 1

    # získání případného modifikátoru + kontrola
    if first_cut[1]:
        correct_mark = ("+", "-")
        for mark in correct_mark:
            if mark in first_cut[1]:
                math_mark = mark
                try:
                    modifier = int(first_cut[1].strip(mark))
                    break
                except:
                    return error_value
        if not math_mark:
            return error_value

    # výpočet hodu s modifikátorem
    if modifier:
        return eval(str(calculation(rolls, dice)) + math_mark + str(modifier))

    # výpočet hodu bez modifikátoru
    else:
        return calculation(rolls, dice)
        

print(dice_calculation("2D10+5"))