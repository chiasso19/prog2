from flask import Flask, request, render_template
import daten

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        workout = request.form.get("workout")
        walk = request.form.get("walk")
        stretching = request.form.get("stretching")

        vacuum = request.form.get("vacuum")
        tidy = request.form.get("tidy")
        bed = request.form.get("bed")

        veggie = request.form.get("veggie")
        sweets = request.form.get("sweets")
        alcohol = request.form.get("alcohol")

        habits = {
            "Sport": [
                {
                    "Workout": workout,
                    "Walk": walk,
                    "Stretching": stretching
                }],
            "Haushalt": [
                {"Vacuum": vacuum,
                 "Tidy": tidy,
                 "Bed": bed
                 }],
            "Nahrung": [
                {"Veggies": veggie,
                 "Sweets": sweets,
                 "Alcohol": alcohol
                 }]
        }

        habits = daten.habit_speichern(habits)
    return render_template('index.html')

@app.route("/statistik")
def statistik():
    return render_template('statistik.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)

