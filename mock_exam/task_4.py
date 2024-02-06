def div(num1: int, num2: int) -> list:
    """
    Funkce přijme dvě čísla jako začátek a konec řady
    a vrátí seznam těchto čísel, kterou jsou dělitelná
    dvěma, ale ne třema.
    """
    num_list = list(num for num in range(num1, num2 + 1) if num % 2 == 0 and num % 3 != 0)
    return num_list

print(div(0, 20))
    