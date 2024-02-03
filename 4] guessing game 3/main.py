from flask import Flask, request, render_template
app = Flask(__name__)

def calc():
    """
    calc function takes min and max from web form, calculate and return guess
    :return:
    """
    min = int(request.form['min'])
    max = int(request.form['max'])
    guess = ((max - min) // 2) + min
    return guess
@app.route("/", methods=['GET', 'POST'])
def guessing_from_player():
    """
    guessing_from_player program /w flask ask player to think a number from 0 to 1000
    reacting to POST returned value and calculate new guess
    :return:
    """
    if request.method == "POST":
        answer = request.form['guess_button']
        round = int(request.form['round'])
        if round == 10:
            return render_template("cheater.html")
        if answer == "you guessed":
            return render_template("win.html")
        elif answer == "too high":
            max = calc()
            min = int(request.form['min'])
            guess = ((max - min) // 2) + min
            round += 1
            return render_template("index.html", guess=guess, min=min, max=max, round=round)
        elif answer == "too low":
            min = calc()
            max = int(request.form['max'])
            guess = ((max - min) // 2) + min
            round += 1
            return render_template("index.html", guess=guess, min=min, max=max, round=round)
    else:
        min = 0
        max = 1000
        round = 1
        guess = ((max - min) // 2) + min
        return render_template("index.html", guess=guess, min=min, max=max, round=round)


if __name__ == '__main__':
    app.run(debug=True)
