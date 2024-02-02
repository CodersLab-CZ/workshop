from flask import Flask, request, render_template

app = Flask(__name__)

minimum = 0
maximum = 1000


@app.route("/", methods=["GET", "POST"])
def game():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":

        # used_button = request.form("button")
        # if used_button == "too_low":
        #     minimum = request.form["guess"]

        # elif used_button == "too_high":
        #     maximum == request.form["guess"]

        # elif used_button == "you_win":
        #     return render_template("i_win.html")

        guess = int((maximum-minimum) / 2) + minimum
        return render_template("guessing.html", guess=guess)            
        


if __name__ == "__main__":
    app.run(debug=True)