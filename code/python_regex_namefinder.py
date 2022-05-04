import re
with open(r"C:\Users\FurkanPC\OneDrive - TH Köln\Förstner\Foerstner.txt", "r",encoding='utf-8') as a:
     RawText = a.read()

Deutsch = []
Franzözisch = []
Englisch = []

Name = re.findall('name">([^"]*?)<',RawText)
a = re.compile(r'\(')
b = re.compile(r'\/')

# Englisch, Deutsch und Franzözisch

for x in range(len(Name)):
   # if b.search(Name[x]):
   #     print(Name[x])

# Franzözisch

    if not a.search(Name[x]) and not b.search(Name[x]):
        Deutsch.append(Name[x])
    
# Deutsch und Franzözisch        

    if a.search(Name[x]) and not b.search(Name[x]):
         Franzözisch.append(str(re.findall('\(.*?\)', Name[x])[-1]))
      
      
      
