# Python Opdrachten

## Python Opdracht 1 (Bibliotheek database)

Maak een database aan door gebruik te maken van de library tinyDB (doe hier opzoekwerk over hoe je deze gebruikt). 

De database gaat gebruikt worden om nieuwe boeken die zijn aangekocht door de bib in een database te steken. 
Maar ook boeken verwijderen omdat ze te oud zijn.

### 1. Maak een database aan genaamd boeken

### 2. Maak een input veld aan om te kiezen welk commmando je wilt uitvoeren:

Mogelijke antwoorden:

#### i -> nieuwe boek toevoegen

Als de gebruiker 'i' heeft gekozen toon je 3 input velden waar hij de naam van het boek, de auteur en een omschrijving kan ingeven.

Voeg nu dit nieuw boek toe aan de database
(tip: insert)

#### r -> verwijder een boek
Als de gebruiker 'i' heeft gekozen toon je 1 input velden waar hij de naam van het boek kan ingeven doormiddel van deze naam gaan we dit boek uit de database wissen

Verwijder dit boek nu uit de database
(tip: delete)



### 3. Boek toevoegen

Voeg het boek Oorlogswinter toe met auteur Jan Terlouw en omschrijving 'Oorlogs Thriller' toe aan de database.

### 4. Boek verwijderen

Verwijder het boek Oorlogswinter.


## Python Opdracht 2 (Leren werken met ccxt)

Maak api keys aan voor je binance account (opzoeken indien nodig) en haal data op met deze api keys doormiddel van ccxt.

Installeer ccxt met pip

Print elke halve seconde de OHLCV data met de library ccxt (candle waarden) af voor BTC/USDT van Binance Futures (verschil tussen binance en binance futures).

Tips:
- Maak gebruik van de wiki pagina op de github pagina van ccxt
- Je kan ook zoeken in de issues bijvoorbeeld wanneer je iets niet vind in de wiki. Hier kan je meestal specifieke antwoorden vinden zoals hoe je kan gebruik maken van binance futures ipv binance (hier posten mensen hun problemen / mogelijke bugs / vragen / ...).