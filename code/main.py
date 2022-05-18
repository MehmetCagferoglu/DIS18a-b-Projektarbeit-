
import re
from pathlib import Path
cwd = Path(__file__).resolve().parent.parent

with open(str(cwd)+"\data/index_of_works_v1-5", "r",encoding='utf-8') as a:
     RawText = a.read()

# ERsteller

Creator = re.findall('creator">([^"]*?)<',RawText) 

for x in range(len(Creator)):
    if Creator[x] == "Fantin":
        Creator[x] = "Henri Fantin-Latour"
    else:
        Creator[x] = "Otto Scholderer"

#Titel

titel_de = []
titel_fr = []
titel_en = []

Name = re.findall('name">([^"]*?)<',RawText)
a = re.compile(r'\(')
b = re.compile(r'\/')


# titel all

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
        
# titel_fr

    if not a.search(Name[x]) and not b.search(Name[x]):
        titel_fr.append(Name[x])
        titel_en.append("")
        titel_de.append("")
    
# titel_de und titel_fr         

    if a.search(Name[x]) and not b.search(Name[x]):
         titel_fr.append(str(re.findall('\(.*?\)', Name[x])[-1])[1:-1])
         titel_de.append(str(re.findall('.*\(', Name[x])[-1])[:-2])
         titel_en.append("")
        
#Maße   
    
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


#Ersteluings jahr
Release = re.findall('dateCreated">([^"]*?)<',RawText)
   
#Speicehrung

Dict = {}


for x in range(len(Creator)):
    y = x + 1 
#Creator    
    Dict[y] = {     "Creator" : Creator[x],
                    "titel" : {"titel_de" : "null",
                               "titel_de" : "null",
                               "titel_en" : "null"
                                            }
              }      
#titel_de Titel   
    if len(titel_de[x]) > 3:
        Dict[y]["titel"]["titel_de"] = titel_de[x]
    if len(titel_de[x]) < 3:
            Dict[y]["titel"]["titel_de"] = titel_fr[x]
#Französicher Titel
    if len(titel_fr[x]) > 3:
        Dict[y]["titel"]["titel_fr"] = titel_fr[x]
    if len(titel_fr[x]) < 3:
        Dict[y]["titel"]["titel_fr"] = titel_de[x]         
#englsicher Titel
    if len(titel_en[x]) > 3:
       Dict[y]["titel"]["titel_en"] = titel_en[x] 
    if len(titel_en[x]) < 3:
        if Creator[x] == "Henri Fantin-Latour":
            Dict[y]["titel"]["titel_en"] = titel_fr[x] 
        if Creator[x] == "Otto Scholderer":
            Dict[y]["titel"]["titel_en"] = titel_de[x]    
#Release           

    Dict[y]["Release"] = Release[x]
#Maße   
    Dict[y]["Maße"] = Maße[x]



        

