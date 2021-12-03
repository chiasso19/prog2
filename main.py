from flask import Flask, request
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/meine-habits", methods=['GET', 'POST'])
def meine_habits():
    if request.method == 'POST':
        ziel_person = request.form['vorname']
        rueckgabe_string = "Hello " + ziel_person + "!"
        return rueckgabe_string

    return render_template('meine_habits.html')

@ app.route("/statistik")
def statistik():
    return render_template('statistik.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)

"""
sport = {
    "Workout": workout_mins,
    "Walk": walk_mins,
    "Stretching": stretching_mins
       }
haushalt = {
    "Vaccum": vaccum,
    "Tidy": tidy,
    "Make Bed": make_bed
       }
nahrung = {
    "Veggies/Fruits": ,
    "Sweets": ,
    "Alcohol":
       }

