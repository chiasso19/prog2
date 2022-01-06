import json


def speichern(datei, key, value):
    try:
        with open('habits.json') as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[str(key)] = value

    with open('habits.json', "w") as open_file:
        json.dump(datei_inhalt, open_file, indent=2)


def habit_speichern(datum, dicthabits):
    datei_name = "habits.json"
    speichern(datei_name, datum, dicthabits)
    return datum, dicthabits


def habits_laden():
    datei_name = "habits.json"

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt