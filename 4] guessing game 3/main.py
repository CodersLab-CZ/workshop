from flask import Flask, request, render_template

app = Flask(__name__)


def calculation(mnimum=int, mximum=int) -> int:
    """
    Fukce se základním vzorcem pro výpočet 
    tipu čísla.
    """
    return (mximum-mnimum) // 2 + mnimum


@app.route("/", methods=["GET", "POST"])
def game():
    """
    Aplikace pro hádání čísla hráče v rozsahu 0-1000.
    Funkce získá vstupní hodnoty mn a mx, díky kterým
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
        # získání hodnot mn/mx/guess
        mn = int(request.form.get("mn", default=0))
        mx = int(request.form.get("mx", default=1000))
        guess = 0

        # úprava hodnot podle vstupu uživatele
        answer = request.form.get("button")
        if answer == "low":
            mn = int(request.form.get("guess"))
            print(mn, mx)
            guess = calculation(mn, mx)
            return render_template("guessing.html", guess=guess, mn=mn, mx=mx)
        
        elif answer == "high":
            mx = int(request.form.get("guess"))
            print(mn, mx)
            guess = calculation(mn, mx)
            return render_template("guessing.html", guess=guess, mn=mn, mx=mx)
        
        # zobrazení výherní stránky
        elif answer == "win":
            return render_template("i_win.html")
        
        # první zobrazení hrací stránky (bez vstupu uživatele)
        else:
            guess = calculation(mn, mx)
            return render_template("guessing.html", guess=guess, mn=mn, mx=mx)  


if __name__ == "__main__":
    app.run(debug=True)