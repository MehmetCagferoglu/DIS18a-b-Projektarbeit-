
### Wikidata Query Service
#### Durch das Wikidata Query Service ist es den angemeldeten Nutzern möglich, durch die Datenbanksprache __SQL__ gewünschten Informationen zu downloaden und so unser Informationsbedarf zu decken.  Durch die SQL Abfrage erhalten wir eine CSV Datei mit den gewünschten Informationen.


#### SQL Scholderer <br />
SELECT ?item ?itemLabel <br />
WHERE <br />
{ <br />
?item wdt:P31 wd:Q5 . <br />
?item wdt:P27 wd:Q27306 . <br />
?item wdt:P106 wd:Q1028181 . <br />
?item wdt:P19 wd:Q1794 . <br />
?item wdt:P20 wd:Q1794 . <br />
?item wdt:P136 wd:Q170571 . <br />
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". } # <span lang="en" dir="ltr" class="mw-content-ltr">Helps get the label in your <br /> language, if not, then en language</span> <br />

# SQL Fatin  <br />
SELECT ?item ?itemLabel 
WHERE 
{
?item wdt:P31 wd:Q5 .
?item wdt:P27 wd:Q142 . 
?item wdt:P106 wd:Q1028181 .
?item wdt:P22 wd:Q3526419

  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". } # <span lang="en" dir="ltr" class="mw-content-ltr">Helps get the label in your language, if not, then en language</span>
}

