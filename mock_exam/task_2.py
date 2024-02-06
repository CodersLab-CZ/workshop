def singulars_and_plurals(word_list: list) -> dict:
    """
    Funkce přijme list slov, rozdělí je na jednotná
    a množná a vráti slovník, který obsahuje seznamy
    těchto slov.
    """
    shorted_words = {"singulars": [], "plurals": []}
    for word in word_list:
        if word[-1] != "s":
            shorted_words["singulars"].append(word)
        else:
            shorted_words["plurals"].append(word)

    return shorted_words


test_list = [
    "tomato", "tomatoes",
    "potato", "potatoes",
    "cars", "unicorns",
    "horse", "cow"
]

print(singulars_and_plurals(test_list))
