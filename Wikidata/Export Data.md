
### Wikidata Query Service
##### Durch das Wikidata Query Service ist es den angemeldeten Nutzern möglich, durch die Datenbanksprache __SQL__ gewünschten Informationen zu downloaden und so unser Informationsbedarf zu decken.  Durch die SQL Abfrage erhalten wir eine CSV Datei mit den gewünschten Informationen.


#Scholderer
SELECT ?item ?itemLabel 
WHERE 
{
?item wdt:P31 wd:Q5 .
?item wdt:P27 wd:Q27306 . 
?item wdt:P106 wd:Q1028181 .
?item wdt:P19 wd:Q1794 .
?item wdt:P20 wd:Q1794 . 
?item wdt:P136 wd:Q170571 .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". } # <span lang="en" dir="ltr" class="mw-content-ltr">Helps get the label in your language, if not, then en language</span>

#Fatin
SELECT ?item ?itemLabel 
WHERE 
{
?item wdt:P31 wd:Q5 .
?item wdt:P27 wd:Q142 . 
?item wdt:P106 wd:Q1028181 .
?item wdt:P22 wd:Q3526419

  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". } # <span lang="en" dir="ltr" class="mw-content-ltr">Helps get the label in your language, if not, then en language</span>
}

