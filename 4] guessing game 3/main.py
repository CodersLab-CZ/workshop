from flask import Flask, render_template, request

app = Flask(__name__)

min_value = 0
max_value = 1000
guess = 500

@app.route("/", methods=["GET", "POST"])
def index():
    global min_value, max_value, guess
    if request.method == "POST":

        if "too_small" in request.form:
            min_value = guess 
        elif "too_big" in request.form:
            max_value = guess
        else:
            return render_template("win.html", min_value=min_value, max_value=max_value, guess=guess)
         
    guess = int((max_value - min_value) // 2 ) + min_value
    return render_template("index.html", min_value=min_value, max_value=max_value, guess=guess)

if __name__ == "__main__":
    app.run(debug=True)


