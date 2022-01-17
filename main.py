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

        datum = request.form.get("datum")


        dicthabits = {
            "Sport": [
                {
                    "Workout": workout,
                    "Walk": walk,
                    "Stretching": stretching
                }],
            "Haushalt": [
                {
                    "Vacuum": vacuum,
                    "Tidy": tidy,
                    "Bed": bed
                 }],
            "Nahrung": [
                {
                    "Veggies": veggie,
                    "Sweets": sweets,
                    "Alcohol": alcohol
                 }]
        }
        daten.habit_speichern(datum, dicthabits)

    return render_template('index.html')


@app.route("/statistik", methods=['GET'])
def statistik():
    datenhabits = daten.habits_laden()
    workoutgesamt = 0
    walkgesamt = 0
    stretchinggesamt = 0
    vacuumgesamt = 0
    tidygesamt = 0
    bedgesamt = 0
    veggiegesamt = 0
    sweetsgesamt = 0
    alcoholgesamt = 0

    veggieverg = 0 #Vergleichzähler
    sweetsverg = 0  # Vergleichzähler
    alcoholverg = 0  # Vergleichzähler

    anzahlhabits = 0 #wie viel Mal wurde getrackt

    monatworkoutgesamt = 0


    for key, alles in datenhabits.items():
        monat = key.split(".")[1]
        if monat == "01":
            if alles["Sport"][0]["Workout"] != "":
                monatworkoutgesamt = monatworkoutgesamt + int(alles["Sport"][0]["Workout"])

        if alles["Sport"][0]["Workout"] != "":
            workoutgesamt= workoutgesamt + int(alles["Sport"][0]["Workout"])
        if alles["Sport"][0]["Walk"] != "":
            walkgesamt= walkgesamt + int(alles["Sport"][0]["Walk"])
        if alles["Sport"][0]["Stretching"] != "":
            stretchinggesamt= stretchinggesamt + int(alles["Sport"][0]["Stretching"])

        if alles["Haushalt"][0]["Vacuum"]:
            vacuumgesamt = vacuumgesamt + 1
        if alles["Haushalt"][0]["Tidy"]:
            tidygesamt = tidygesamt + 1
        if alles["Haushalt"][0]["Bed"]:
            bedgesamt = bedgesamt + 1

        if alles["Nahrung"][0]["Veggies"]:
            veggiegesamt = veggiegesamt + 1 #insgesamt
            if alles["Nahrung"][0]["Veggies"] == "viel":#Vergleiche
                veggieverg = veggieverg + 6
            if alles["Nahrung"][0]["Veggies"] == "mittel":#Vergleiche
                veggieverg = veggieverg + 3
            if alles["Nahrung"][0]["Veggies"] == "wenig":#Vergleiche
                veggieverg = veggieverg + 1

        if alles["Nahrung"][0]["Sweets"]:
            sweetsgesamt = sweetsgesamt + 1 #insgesamt
            if alles["Nahrung"][0]["Sweets"] == "viel":#Vergleiche
                sweetsverg = sweetsverg + 6
            if alles["Nahrung"][0]["Sweets"] == "mittel":#Vergleiche
                sweetsverg = sweetsverg + 3
            if alles["Nahrung"][0]["Sweets"] == "wenig":#Vergleiche
                sweetsverg = sweetsverg + 1

        if alles["Nahrung"][0]["Alcohol"]:
            alcoholgesamt = alcoholgesamt + 1 #insgesamt
            if alles["Nahrung"][0]["Alcohol"] == "viel":#Vergleiche
                alcoholverg = alcoholverg + 6
            if alles["Nahrung"][0]["Alcohol"] == "mittel":#Vergleiche
                alcoholverg = alcoholverg + 3
            if alles["Nahrung"][0]["Alcohol"] == "wenig":#Vergleiche
                alcoholverg = alcoholverg + 1

        if alles != "":
            anzahlhabits = anzahlhabits + 1

        vergvegsweet = veggieverg / sweetsverg
        vergvegalc = veggieverg / alcoholverg
        vergalcsweet = alcoholverg / sweetsverg


    return render_template('statistik.html', workoutgesamt=workoutgesamt, walkgesamt=walkgesamt,
                           stretchinggesamt=stretchinggesamt, vacuumgesamt=vacuumgesamt,tidygesamt=tidygesamt,
                           bedgesamt=bedgesamt, veggiegesamt=veggiegesamt,sweetsgesamt=sweetsgesamt,
                           alcoholgesamt=alcoholgesamt, vergvegsweet=vergvegsweet, vergvegalc=vergvegalc, vergalcsweet=vergalcsweet,
                           anzahlhabits=anzahlhabits, monatworkoutgesamt=monatworkoutgesamt)
if __name__ == "__main__":
    app.run(debug=True, port=5000)

