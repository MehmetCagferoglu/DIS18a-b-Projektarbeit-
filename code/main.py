# Importieren der Libraries.
import re
from pathlib import Path
import json

# Mithilfe der Pathlib-Library der aktuellen Workingdirectory finden und zwei Ordnerpfade zurückgehen.
cwd = Path(__file__).resolve().parent.parent

# Temporäres Öffnen der Datei mit den Rohdaten.
with open(str(cwd) + "\data/index_of_works_v1-7", "r", encoding="utf-8") as a:
    RawText = a.read()
# Regexabfrage zum Auslesen des Erstellers der Werke.
Creator = re.findall('creator">([^"]*?)<', RawText)

for x in range(len(Creator)):
    if Creator[x] == "Fantin":
        Creator[x] = "Henri Fantin-Latour"
    else:
        Creator[x] = "Otto Scholderer"
# Leere Listen für die Titel in verschiedenen Sprachen erzeugen.
titel_de = []
titel_fr = []
titel_en = []

# Regexabfrage, die alle Titel in einer Liste heraussucht.
Name = re.findall('name">([^"]*?)<', RawText)

# Definition von a und b mit Regex. Für a = "\(" und für b = "\/".
a = re.compile(r"\(")
b = re.compile(r"\/")


for x in range(len(Name)):
    # Wenn eine Klammer und ein Slash enthalten sind, gibt es Titel in drei Sprachen (titel_de, titel_en und titel_fr).
    if a.search(Name[x]) and b.search(Name[x]):
        en = re.findall(".*\/", Name[x])
        for y in en:
            titel_en.append(y[:-3])
        de = re.findall("\/.*\/|\/.*\(", Name[x])
        for y in de:
            titel_de.append(y[2:-2])
        fr = re.findall("\(.*?\)", Name[x])
        for y in fr:
            titel_fr.append(y[2:-2])
    # Wenn nichts enthalten ist, ist der Titel französisch (titel_fr).
    if not a.search(Name[x]) and not b.search(Name[x]):
        titel_fr.append(Name[x])
        titel_en.append("")
        titel_de.append("")
    # Wenn eine Klammer und kein Slash enthalten ist, dann ist der Titel französisch und deutsch (titel_de und titel_fr).
    if a.search(Name[x]) and not b.search(Name[x]):
        titel_fr.append(str(re.findall("\(.*?\)", Name[x])[-1])[1:-1])
        titel_de.append(str(re.findall(".*\(", Name[x])[-1])[:-2])
        titel_en.append("")
# Regexabfrage zum Finden der Maße (Länge und Breite) und Erstellung der leeren Listen zur Speicherung der Werte.
Maße = re.findall(">([^>]*?cm)<|>0<", RawText)
länge = []
breite = []

# Regexabfrage, um Länge und Breite der Maße vorher zu extrahieren. Zudem wird geprüft, ob überhaupt Maße enthalten sind.
for x in range(len(Maße)):
    if len(Maße[x]) > 3:
        a = re.findall("([0-9,]+)", Maße[x])
        länge.append(a[0] + "cm")
        breite.append(a[1] + "cm")
    if len(Maße[x]) < 3:

        länge.append("")
        breite.append("")
# Regexabfrage zum Auslesen des Erstellungsjahres
Release = re.findall('dateCreated">([^"]*?)<', RawText)

# Erstellung des Dictionarys zur Speicherung.
Dict = {}

# Eintragen der extrahierten Daten in das Dictionary.
for x in range(len(Creator)):
    y = x + 1

    # Funktion des Erstellers (Creator)
    Dict[y] = {
        "Creator": Creator[x],
        "titel": {"titel_de": "null", "titel_de": "null", "titel_en": "null"},
    }

    # Befüllen der Titel.
    # Deutscher Titel
    if len(titel_de[x]) > 3:
        Dict[y]["titel"]["titel_de"] = titel_de[x]
    if len(titel_de[x]) < 3:
        Dict[y]["titel"]["titel_de"] = titel_fr[x]
    # Französischer Titel
    if len(titel_fr[x]) > 3:
        Dict[y]["titel"]["titel_fr"] = titel_fr[x]
    if len(titel_fr[x]) < 3:
        Dict[y]["titel"]["titel_fr"] = titel_de[x]
    # Englischer Titel
    if len(titel_en[x]) > 3:
        Dict[y]["titel"]["titel_en"] = titel_en[x]
    if len(titel_en[x]) < 3:
        if Creator[x] == "Henri Fantin-Latour":
            Dict[y]["titel"]["titel_en"] = titel_fr[x]
            if titel_fr[x] == "":
                Dict[y]["titel"]["titel_en"] = titel_de[x]
        if Creator[x] == "Otto Scholderer":
            Dict[y]["titel"]["titel_en"] = titel_de[x]
            if titel_de[x] == "":
                Dict[y]["titel"]["titel_en"] = titel_fr[x]
    # Release
    Dict[y]["Release"] = Release[x]

    # Maße
    Dict[y]["Maße"] = Maße[x]
# Speichern des Dictionarys im Ordner "data".
cwd2 = Path(__file__).resolve().parent.parent
with open(str(cwd2) + "\data\Data.json", "w") as outfile:

    # Umwandlen des Dictionarys in json.
    json.dump(Dict, outfile)
