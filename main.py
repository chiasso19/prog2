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

    veggieverg = 0  #Vergleiche
    sweetsverg = 0  #Vergleiche
    alcoholverg = 0  #Vergleiche


    for key, alles in datenhabits.items():
        if alles["Sport"][0]["Workout"] != "":
            workoutgesamt= workoutgesamt + float(alles["Sport"][0]["Workout"])
        if alles["Sport"][0]["Walk"] != "":
            walkgesamt= walkgesamt + float(alles["Sport"][0]["Walk"])
        if alles["Sport"][0]["Stretching"] != "":
            stretchinggesamt= stretchinggesamt + float(alles["Sport"][0]["Stretching"])

        if alles["Haushalt"][0]["Vacuum"]:
            vacuumgesamt = vacuumgesamt + 1
        if alles["Haushalt"][0]["Tidy"]:
            tidygesamt = tidygesamt + 1
        if alles["Haushalt"][0]["Bed"]:
            bedgesamt = bedgesamt + 1

        if alles ["Nahrung"][0]["Veggies"]:
            veggiegesamt = veggiegesamt + 1
            if alles["Nahrung"][0]["Veggies"] == "viel":#Vergleiche
                veggieverg = veggieverg + 3
            if alles["Nahrung"][0]["Veggies"] == "mittel":#Vergleiche
                veggieverg = veggieverg + 2
            if alles["Nahrung"][0]["Veggies"] == "wenig":#Vergleiche
                veggieverg = veggieverg + 1

        if alles ["Nahrung"][0]["Sweets"]:
            sweetsgesamt = sweetsgesamt + 1
            if alles["Nahrung"][0]["Sweets"] == "viel":#Vergleiche
                sweetsverg = sweetsverg + 3
            if alles["Nahrung"][0]["Sweets"] == "mittel":#Vergleiche
                sweetsverg = sweetsverg + 2
            if alles["Nahrung"][0]["Sweets"] == "wenig":#Vergleiche
                sweetsverg = sweetsverg + 1

        if alles ["Nahrung"][0]["Alcohol"]:
            alcoholgesamt = alcoholgesamt + 1
            if alles["Nahrung"][0]["Alcohol"] == "viel":#Vergleiche
                alcoholverg = alcoholverg + 3
            if alles["Nahrung"][0]["Alcohol"] == "mittel":#Vergleiche
                alcoholverg = alcoholverg + 2
            if alles["Nahrung"][0]["Alcohol"] == "wenig":#Vergleiche
                alcoholverg = alcoholverg + 1




    satz_workoutgesamt = "Du hast " + str(workoutgesamt) + " Minuten Workout gmacht."
    satz_walkgesamt = "Du bist " + str(walkgesamt) + " Minuten gelaufen."
    satz_stretchinggesamt = "Du hast " + str(stretchinggesamt) + " Minuten Stretching gmacht."
    satz_vacuumgesamt = "Du hast " + str(vacuumgesamt) + " Mal gestaubsaugt."
    satz_tidygesamt = "Du hast " + str(tidygesamt) + " Mal aufgeräumt."
    satz_bedgesamt = "Du hast " + str(bedgesamt) + " dein Bett gemacht."
    satz_veggiegesamt = "Du hast " + str(veggiegesamt) + " Mal Gemüse gegessen."
    satz_sweetsgesamt = "Du hast " + str(sweetsgesamt) + " Mal Süsses gegessen."
    satz_alcoholgesamt = "Du hast " + str(alcoholgesamt) + " Mal Alkohol getrunken."
    return render_template('statistik.html', satz_workoutgesamt=satz_workoutgesamt, satz_walkgesamt=satz_walkgesamt,satz_stretchinggesamt=satz_stretchinggesamt,satz_vacuumgesamt=satz_vacuumgesamt,satz_tidygesamt=satz_tidygesamt,satz_bedgesamt=satz_bedgesamt,satz_veggiegesamt=satz_veggiegesamt,satz_sweetsgesamt=satz_sweetsgesamt,satz_alcoholgesamt=satz_alcoholgesamt)












    """for key, value in dicthabits.items():
        return(key,value)"""

    """for ins_workout in habits.value([['Workout']):
        ins_workout = "Du hast insgesamt "+ str(ins_workout) + "Minuten Workouts gemacht."""
    return render_template('statistik.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)

