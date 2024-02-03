from random import randint

# global count


def mat_rand(dices, wall):

    dots = 0
    if dices == 1:
        dots += randint(1, (int(wall) + 1))
    else:
        for i in range(int(dices)):
            dots += randint(1, (int(wall) + 1))
        return dots


def dic_decode(parse_dice):
    result = 0
    values = list(parse_dice)
    search_index_d = values.index("D")
    if values.index("D") > 0:
        if "+" in parse_dice:
            search_index_plus = values.index("+")
            modification = ''.join(values[search_index_plus + 1:])
            count = ''.join(values[0:search_index_d])
            typ = ''.join(values[search_index_d + 1:search_index_plus])
            result = int((mat_rand(count, typ))) + (int(modification))
        elif "-" in parse_dice:
            search_index_plus = values.index("-")
            modification = ''.join(values[search_index_plus + 1:])
            print(f"mod{modification}")
            count = ''.join(values[0:search_index_d])
            typ = ''.join(values[search_index_d + 1:search_index_plus])
            result = int((mat_rand(count, typ))) - (int(modification))
        else:
            count = ''.join(values[0:search_index_d])
            typ = ''.join(values[search_index_d + 1:])
            result = int((mat_rand(count, typ)))
    elif values.index("D") == 0:
        count = '1'
        if "+" in parse_dice:
            search_index_plus = values.index("+")
            modification = ''.join(values[search_index_plus + 1:])
            typ = ''.join(values[search_index_d + 1:search_index_plus])
            result = int((mat_rand(count, typ))) + (int(modification))
        elif "-" in parse_dice:
            search_index_plus = values.index("-")
            modification = ''.join(values[search_index_plus + 1:])
            print(f"mod{modification}")
            typ = ''.join(values[search_index_d + 1:search_index_plus])
            result = int((mat_rand(count, typ))) - (int(modification))
        else:
            typ = ''.join(values[search_index_d+1:])
            result = int((mat_rand(count, typ)))
    return result


dice_parameter = input("Typ of dice:")
print(f"RESULT={dic_decode(dice_parameter)}")
# todo list:
#    -make exception
#    -only use specific type od dice
#    -review code to many if rewrite tu function
