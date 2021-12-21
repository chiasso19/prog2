from datetime import datetime
import json


def speichern(datei, key, value):
    try:
        with open('habits.json') as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[str(key)] = value

    # print(datei_inhalt)

    with open('habits.json', "w") as open_file:
        json.dump(datei_inhalt, open_file, indent=2)


def habit_speichern(habits):
    datei_name = "habits.json"
    zeitpunkt = datetime.now()
    speichern(datei_name, zeitpunkt, habits)
    return zeitpunkt, habits


def habits_laden():
    datei_name = "habits.json"

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt