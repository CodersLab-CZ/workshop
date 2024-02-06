def check_palindrome(entered_str: str) -> bool:
    """
    Funkce přijme řetězec a očistí ho o mezery a speciální
    znaky a zkontroluje, jestli se jedná o palindrom. 
    """
    ## VERZE, KDE SE NEZOHLEĎNUJÍ ZNAMÉNKA VE VĚTÁCH
    # cls_string = (entered_str.lower()).replace(" ", "")
    # if cls_string == cls_string[::-1]:
    #     return True
    # else:
    #     return False

    illegal_char = (" ", ",", ";", ".", "!", "?")
    entered_str = entered_str.lower()

    for char in illegal_char:
        if char in entered_str:
            entered_str = entered_str.replace(char, "")

    if entered_str == entered_str[::-1]:
        return True
    else:
        return False
    

print(check_palindrome("racecar"))
print(check_palindrome("level"))
print(check_palindrome("Was it a car or a cat I saw?"))
print(check_palindrome("return"))