from flask import Flask, request, render_template

app = Flask(__name__)


def calculation(minimum=int, maximum=int) -> int:
    """
    Fukce se základním vzorcem pro výpočet 
    tipu čísla.
    """
    return (maximum-minimum) // 2 + minimum


@app.route("/", methods=["GET", "POST"])
def game():
    """
    Aplikace pro hádání čísla hráče v rozsahu 0-1000.
    Funkce získá vstupní hodnoty min a max, díky kterým
    vypočítává nejpravděpodobnější číslo. Hodnoty jsou na 
    začátku nastavené defaltně a v průběhu hry se upravují
    podle reakce uživatele dokud aplikace nedopočítá správné 
    číslo.
    """
    # zobrazení úvodní stránky hry
    if request.method == "GET":
        return render_template("index.html")
    
    # zobrazení hrací stránky 
    elif request.method == "POST":
        # získání hodnot min/max/guess
        min = int(request.form.get("min", default=0))
        max = int(request.form.get("max", default=1000))
        guess = 0

        # úprava hodnot podle vstupu uživatele
        answer = request.form.get("button")
        if answer == "low":
            min = int(request.form.get("guess"))
            print(min, max)
            guess = calculation(min, max)
            return render_template("guessing.html", guess=guess, min=min, max=max)
        
        elif answer == "high":
            max = int(request.form.get("guess"))
            print(min, max)
            guess = calculation(min, max)
            return render_template("guessing.html", guess=guess, min=min, max=max)
        
        # zobrazení výherní stránky
        elif answer == "win":
            return render_template("i_win.html")
        
        # první zobrazení hrací stránky (bez vstupu uživatele)
        else:
            guess = calculation(min, max)
            return render_template("guessing.html", guess=guess, min=min, max=max)  


if __name__ == "__main__":
    app.run(debug=True)