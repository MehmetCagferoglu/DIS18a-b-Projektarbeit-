Autor = ["Otto Scholderer","Henri Fantin-Latour","Henri Fantin-Latour"]
titel_de = ["Kopie nach Ferdinand Bol, Bildnis eines jungen Herren", "Mona Lisa",""]
titel_fr = ["copie d'après Ferdinand Bol, portrait d'un jeune homme", "","baguette"]
titel_en = ["","football",""]
Release = [1851,1400,1800]
width = ["96cm","","60cm"]
height = ["80cm","","10cm"]
current_location = ["Städelsches Kunstinstitut", "Frankfurt-am-Main","","Pari"]


            
Dict = {}


for x in range(len(Autor)):
    y = x + 1 
#Autor    
    Dict[y] = {     "autor" : Autor[x],
                    "titel" : {"titel_de" : "null",
                               "titel_de" : "null",
                               "titel_en" : "null"
                                            }
              }      
#Deutscher Titel   
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
        if Autor[x] == "Henri Fantin-Latour":
            Dict[y]["titel"]["titel_en"] = titel_fr[x] 
        if Autor[x] == "Otto Scholderer":
            Dict[y]["titel"]["titel_en"] = titel_de[x]    
        
#Release       
    Dict[y]["Release"] = Release[x]
#width
    if len(width[x]) > 0 and len(height[x]) > 0: 
        Dict[y]["dimentions"] = {"width" : width[x],
                                 "height" : height[x]}  
#current_location      
    if len(titel_de[x]) < 3:
        Dict[y]["current_location"] =  current_location[x]     







"""
Dict = {
        "ID" : {  1: {
                    "Autor" : 2,
                    "titel_de" : 3
               },
                 2:{
                    "Autor" : 2,
                    "titel_de" : 3
                    }
                
               }
        }


Dict = {}

for x in range(1,2):

    Autor = "Otto Scholderer"
    titel_de = "Kopie nach Ferdinand Bol, Bildnis eines jungen Herren"
    Titel_fr = "copie d'après Ferdinand Bol, portrait d'un jeune homme"
    Fertigstellungsjahr = 1851
    Technik_fr = "huile sur toile"
    Technik_de = "Öl auf Leinwand"
    Breite = "96cm"
    Höhe = "80cm"
    Aufbewahrungsort = "Städelsches Kunstinstitut, Frankfurt-am-Main"

    
    Dict["ID"] = x

    if titel_de != "":
        Dict[x] = {"Autor" : Autor}


print(Dict)
"""

