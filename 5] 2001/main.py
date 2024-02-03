from random import randint


def calculation(x: int, y: int) -> int:
    """
    Vnořená funkce obsahující základní vzorec 
    pro výpočet hodu kostkou bez modifikátoru.
    """
    return x * (randint(1, y+1))


def second_cut_check(first_cut_1: str, math_mark_str: int):
    """
    Vnořená funkce pro vyhodnocení druhé části zadané 
    hodnoty, pokud byl použit modifikátor. 
    Pokud byla hodnota zadáná správně, funce vrátí tuple
    obsahující druh kostky a modifikátor jako int.
    Pokud byla hodnota zadána špatně, funkce vrátí None.
    """
    second_cut = first_cut_1.split(math_mark_str)
    if len(second_cut) != 2:
        return

    try:
        dice = int(second_cut[0])
        modifier = int(second_cut[1])
        return dice, modifier  
    except ValueError:
        return
    

def dice_calculation(entered_value: str):
    """
    Funkce pro vyhodnocení hodů kostkou, který uživatel zadá
    ve formátu xDy+z kde:
    x = roll (počet hodů)
    y = dice (kolikastěnná je kostka)
    z = modifier (hodnota pro mat. operaci, která se má
                    s výsledkem hodů provést)

    Fukce zkontroluje správnost zadané hodnoty a následně 
    pomocí funkce calculation() vypočítá a vrátí výsledek
    ve formátu int.
    Pokud bude hodnota zadána špatně, vrátí uživateli chybovou
    hlášku.
    """
    error_allert = "WRONG VALUE: a correct value is in format xDy+z."
    roll = 0
    dice = 0
    modifier = 0
    math_mark = ""

    # first format check
    if "D" not in entered_value:
        return error_allert

    # first split + additional check
    first_cut = entered_value.split("D")
    if len(first_cut) != 2:
        return error_allert
    
    if first_cut[1] == False:
        return error_allert
    
    # getting value roll
    if first_cut[0]:
        try: 
            roll = int(first_cut[0])
        except ValueError:
            return error_allert
    else:
        roll = 1
    
    # getting value dice
    if (first_cut[1]).isdigit():
        dice = int(first_cut[1])
    else:
        #getting value modifier
        if "+" in first_cut[1]:
            math_mark = "+"
            second_cut = second_cut_check(first_cut[1], math_mark)
            if second_cut == None:
                return error_allert
            else:
                dice = second_cut[0]
                modifier = second_cut[1]

        elif "-" in first_cut[1]:
            math_mark = "-"
            second_cut = second_cut_check(first_cut[1], math_mark)
            if second_cut == None:
                return error_allert
            else:
                dice = second_cut[0]
                modifier = second_cut[1]

        elif "*" in first_cut[1]:
            math_mark = "*"
            second_cut = second_cut_check(first_cut[1], math_mark)
            if second_cut == None:
                return error_allert
            else:
                dice = second_cut[0]
                modifier = second_cut[1]

        elif "/" in first_cut[1]:
            math_mark = "/"
            second_cut = second_cut_check(first_cut[1], math_mark)
            if second_cut == None:
                return error_allert
            else:
                dice = second_cut[0]
                modifier = second_cut[1]

        else:
            return error_allert

    # calculation for rolls of a dice without a modifier
    if not modifier:
        return calculation(roll, dice)
    
    # calculation for rolls of a dice with a modifier
    else:
        return eval(str(calculation(roll, dice)) + math_mark + str(modifier))



print(dice_calculation("2D4+5+5"))