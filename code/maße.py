import re

with open(r"C:\Users\janni\OneDrive\Uni\Förstner\DIS18a-b-Projektarbeit-\data\index_of_works_v1.4", "r",encoding='utf-8') as a:
     RawText = a.read()

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


