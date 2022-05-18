import re
with open(r"C:\Users\FurkanPC\Documents\GitHub\DIS18a-b-Projektarbeit-\data\index_of_works_v1-5", "r",encoding='utf-8') as a:
     RawText = a.read()
     
# Es werden leere Listen für die jeweiligen Sprachen definiert.

Deutsch = []
Franzoesisch = []
Englisch = []

# Mit diesem Regex-Befehl suchen wir die Namen heraus unterteilt in drei verschiedenen Sprachkriterien

Name = re.findall('name">([^"]*?)<',RawText)
a = re.compile(r'\(')
b = re.compile(r'\/')

# Englisch, Deutsch und Franzoesisch

for x in range(len(Name)):
   # if b.search(Name[x]):
   #     print(Name[x])

# Franzoesisch

    if not a.search(Name[x]) and not b.search(Name[x]):
        Deutsch.append(Name[x])
    
# Deutsch und Franzoesisch        

    if a.search(Name[x]) and not b.search(Name[x]):
         Franzoesisch.append(str(re.findall('\(.*?\)', Name[x])[-1]))
      
      
      
