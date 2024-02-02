from flask import Flask, request, render_template

app = Flask(__name__)

min_num = 0
max_num = 1000
used_button = ""

@app.route("/geussing", methods=["GET", "POST"])
def geussing(button=used_button):
    return used_button == request.form("button")


@app.route("/", methods=["GET", "POST"])
def game(minimum=min_num, maximum=max_num):
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":


        if used_button == "too_low":
            minimum = request.form["guess"]

        elif used_button == "too_high":
            maximum == request.form["guess"]

        elif used_button == "you_win":
            return render_template("i_win.html")
        else: 

            guess = int((maximum-minimum) / 2) + minimum
            return render_template("guessing.html", guess=guess)            
        


if __name__ == "__main__":
    app.run(debug=True)