def shorten(entered_str: str) -> str:
    """
    Funkce přijme libovolně dlouhý řetězec a vrátí 
    řetězec obsahující první písmeno každého slova
    ze zadného stringu.
    """
    cut_str = entered_str.split()
    short_str = list(word[0].upper() for word in cut_str)

    return "".join(short_str)


print(shorten("Don't repeat yourself"))
print(shorten("Read the fine manual"))
print(shorten("All terrain armoured transport"))
