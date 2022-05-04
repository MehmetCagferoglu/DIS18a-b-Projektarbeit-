import re
with open(r"data\index_of_works_v1-4", "r",encoding='utf-8') as a:
     RawText = a.read()

Ident = re.findall('id="([\d"]*?)"',RawText)
Creator = re.findall('creator">([^"]*?)<',RawText) 
Name = re.findall('name">([^"]*?)<',RawText)
Erstellt = re.findall('dateCreated">([^"]*?)<',RawText)
Maße = re.findall('>([^>]*?cm)<|>0<', RawText)
length = re.findall('(\d+\s+x|\d+,\d+\s+x)|>0<', RawText)
height = re.findall('(\d+\s+cm|\d+,\d+\s+cm)', RawText)
    

           
for x in range(len(length)):
    length[x] = str(length[x])[:-2]+'cm'
    

for x in range(len(Creator)):
    if Creator[x] == "Fantin":
        Creator[x] = "Henri Fantin-Latour"
    else:
        Creator[x] = "Otto Scholderer"
        
"""
for x in range(len(Name)):
    if Creator[x] == "Scholderer":
        Creator[x] = "Otto Scholderer"
    else:
        Creator[x] = "Henri Fantin-Latour"
"""


"""
for x in Text4:
    for y in x:
        if y:
            TempList.append(y)
Text4 = TempList

for x in Text6:
    x = x[4:-1]
    try:
        structure.append(int(x))
    except:
        structure.append(x)
        """
"""Error='17720',17670
Error2='17476'"""