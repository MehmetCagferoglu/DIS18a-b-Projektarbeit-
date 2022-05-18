import re

with open(r"C:\Users\janni\OneDrive\Uni\Förstner\DIS18a-b-Projektarbeit-\data\index_of_works_v1-5", "r",encoding='utf-8') as a:
     RawText = a.read()
     
# Mit dem Regex Befehl werden die Maße der Bilder extrahiert, die genau 368 entsprechen. 
# Danach werden zwei leere Listen erstellt für die Länge und Breite.

Maße = re.findall('>([^>]*?cm)<|>0<', RawText)
länge  = []
breite = []


# Bei dieser Funktion wird geprüft, wenn der Datensatz mehr als 3 Zeichen hat, wird in der Variable a die Maße in einer Liste gespeichert. 
# In der ,,länge" Liste wird der erste Indexwert 0 und in ,,breite" der Indexwert 1 eingefügt und mit cm angehangt.
# Andernfalls, wenn es weniger als 3 Zeichen sind, fügt die Funktion ein Leereichen ein, damit alle Datensätze richtig geordnet bleiben.  

for x in range(len(Maße)):
    if len(Maße[x]) > 3:
        a = re.findall('([0-9,]+)', Maße[x])
        länge.append(a[0]+"cm") 
        breite.append(a[1]+"cm")
        
    if len(Maße[x]) < 3:
        länge.append("") 
        breite.append("")
        
print(x)





