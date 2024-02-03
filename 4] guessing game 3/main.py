from flask import Flask, request, render_template

app = Flask(__name__)

min_num = 0
max_num = 1000
guess = 0

def calculation(minimum=int, maximum=int) -> int:
    return (maximum-minimum) // 2 + minimum


@app.route("/too_low", methods=["GET", "POST"])
def too_low():
    global min_num, max_num, guess
    min_num = guess
    guess = calculation(min_num, max_num)
    return render_template("guessing.html", guess=guess)


@app.route("/too_high", methods=["GET", "POST"])
def too_high():
    global min_num, max_num, guess
    max_num = guess
    guess = calculation(min_num, max_num)
    return render_template("guessing.html", guess=guess)


@app.route("/you_win", methods=["GET", "POST"])
def you_win():
    global min_num, max_num, guess
    min_num = 0
    max_num = 1000
    guess = 0

    return render_template("i_win.html") 


@app.route("/", methods=["GET", "POST"])
def game():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        global min_num, max_num, guess
        
        guess = calculation(min_num, max_num)
        return render_template("guessing.html", guess=guess)   


if __name__ == "__main__":
    app.run(debug=True)