from flask import Flask, request, render_template

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

        li = [workout, walk, stretching, vacuum, tidy, bed, veggie, sweets, alcohol]
        return render_template("test.html", listeA=li)   #f"<H1>{workout}, {walk}</H1>"
    else:
        return render_template('index.html')

@ app.route("/statistik")
def statistik():
    return render_template('statistik.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)


"""
dict_habits = {
    "sport":[
        {
            "workout":20,
            "walk":20,
            "stretching":20
        }],
    "haushalt":[
        {"Vacuum": true,
         "tidy": true,
         "make_bed": true
         }],
    "nahrung":[
        { viel mittel wenig?????

        }]

}
"""