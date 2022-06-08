# Importieren wichtiger Libraries
import re
from pathlib import Path
import json 

cwd = Path(__file__).resolve().parent.parent

with open(str(cwd)+"\data/index_of_works_v1-7", "r",encoding='utf-8') as a:
     RawText = a.read()

# Ersteller der Werke
Creator = re.findall('creator">([^"]*?)<',RawText) 

for x in range(len(Creator)):
    if Creator[x] == "Fantin":
        Creator[x] = "Henri Fantin-Latour"
    else:
        Creator[x] = "Otto Scholderer"

# Titel in verschiedenen Sprachen
titel_de = []
titel_fr = []
titel_en = []

# Eine Liste, die alle Titeln heraussucht
Name = re.findall('name">([^"]*?)<',RawText)

# Definition von a und b mit Regex. Für a = "\(" und für b = "\/"
a = re.compile(r'\(')
b = re.compile(r'\/')


# Funktion für alle Titeln (titel all)
for x in range(len(Name)):
    if a.search(Name[x]) and b.search(Name[x]):
        en =  re.findall('.*\/',Name[x])
        for y in en:
            titel_en.append(y[:-3])
        de =  re.findall('\/.*\/|\/.*\(',Name[x])
        for y in de:
            titel_de.append(y[2:-2])
        fr =  re.findall('\(.*?\)',Name[x])
        for y in fr:
            titel_fr.append(y[2:-2])
      
# Funktion nur für das französische Titel (titel_fr)
    if not a.search(Name[x]) and not b.search(Name[x]):
        titel_fr.append(Name[x])
        titel_en.append("")
        titel_de.append("")
    
# Funktion für das französische und deutsche Titel (titel_de und titel_fr)         
    if a.search(Name[x]) and not b.search(Name[x]):
         titel_fr.append(str(re.findall('\(.*?\)', Name[x])[-1])[1:-1])
         titel_de.append(str(re.findall('.*\(', Name[x])[-1])[:-2])
         titel_en.append("")

       
# Maße (Länge und Breite) und die Funktion dafür     
Maße = re.findall('>([^>]*?cm)<|>0<', RawText)
länge  = []
breite = []

for x in range(len(Maße)):
    if len(Maße[x]) > 3:
        a = re.findall('([0-9,]+)', Maße[x])
        länge.append(a[0]+"cm") 
        breite.append(a[1]+"cm")
    if len(Maße[x]) < 3:
    
        länge.append("") 
        breite.append("")


# Erstellungsjahr
Release = re.findall('dateCreated">([^"]*?)<',RawText)
   
# Speicherung in einem Dictionary
Dict = {}


for x in range(len(Creator)):
    y = x + 1 
# Funktion des Erstellers (Creator)   
    Dict[y] = {     "Creator" : Creator[x],
                    "titel" : {"titel_de" : "null",
                               "titel_de" : "null",
                               "titel_en" : "null"
                                            }
              }      
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
            if  titel_fr[x] == "":
                Dict[y]["titel"]["titel_en"] = titel_de[x]
        if Creator[x] == "Otto Scholderer":
            Dict[y]["titel"]["titel_en"] = titel_de[x]
            if  titel_de[x] == "":
                Dict[y]["titel"]["titel_en"] = titel_fr[x]
# Release           
    Dict[y]["Release"] = Release[x]
# Maße   
    Dict[y]["Maße"] = Maße[x]

cwd2 = Path(__file__).resolve().parent.parent    
with open(str(cwd2) + "\data\Data.json", "w") as outfile:
    json.dump(Dict, outfile)


"""
    
j = ""
for x in range(1,368):
    j = j + str(Dict[x]["titel"]) + "\n"
        
"""
