from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/movies", methods=["GET", "POST"])
def movies():
    """
    Aplikace umožní uživateli zadat název filmu a následně
    prohledá uložený seznam a zobrazí uživateli informaci, 
    jestli film patří mezi oblíbené či nikoliv.
    """
    movies = {
    "favourite": ["A New Hope", "Empire Strikes Back", "Return of the Jedi",
                  "The Force Awakens", "Jaws", "Predator", "Mad Max",
                  "Back to the Future", "2001: A Space Odyssey", "Robocop",
                  "The Hitchhiker's Guide to the Galaxy", "Doctor Who",
                  "Aliens", "Alien", "Terminator", "Blade Runner", "Matrix"],

    "hated": ["The Phantom Menace", "Attack of the Clones", "Star Trek",
              "Alien Resurrection", "Twilight"]

    }
    if request.method == "POST":
        ask_movie = request.form["name_movie"]
        if ask_movie in movies["favourite"]:
            answer = "The movie is FAVOURITE!"
        elif ask_movie in movies["hated"]:
            answer = "The movie is HATED!"
        else:
            answer = "No such movie."
        
        return render_template("index.html", answer=answer)
    else:
        return render_template("index.html")
        

if __name__ == "__main__":
    app.run(debug=True)