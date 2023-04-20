EASY_TEXT = """Ik hou van programmeren. Programmeren is leuk. 
Ik kan veel dingen maken met programmeren. Ik kan een website maken. 
Ik kan een spel maken. Ik kan een chatbot maken. 
Programmeren is niet moeilijk. Ik moet alleen de juiste code schrijven. 
De code moet logisch zijn. De code moet foutloos zijn. Werkende code maakt mij blij. 
Niet-werkende code chagerijnig. Programmeren is een avontuur. Ik leer elke dag iets nieuws met programmeren."""

DIFFICULT_TEXT = """Programmeren is een geweldige activiteit, die je in staat stelt om je creativiteit, 
logica en probleemoplossend vermogen te gebruiken, om allerlei soorten applicaties te maken, 
die nuttig, vermakelijk of zelfs levensveranderend kunnen zijn, afhankelijk van je doel en publiek. 
Het is ook een uitdagende bezigheid, die je voortdurend leert om nieuwe talen, technieken en concepten te leren, 
die je helpen om je code efficiënter, eleganter en robuuster te maken, zonder dat je je ooit hoeft te vervelen of te herhalen. 
Bovendien is het een leuke hobby, die je veel voldoening en plezier kan geven, als je ziet hoe je ideeën tot leven komen op het scherm, als je de interactie met je gebruikers ziet of 
als je de reacties van je vrienden en familie ziet, als je ze verrast met je eigen creaties.
"""

ALLOWED_IN_WORD = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-"

# depending on the type of text you wish you get an easy, difficult or text from file.
def getText(choice: str) -> str:
    if choice == 'easy':
        return EASY_TEXT
    elif choice == 'difficult':
        return DIFFICULT_TEXT
    else:
        return getFileContentAsString(choice)

def getFileContentAsString(textFile: str) -> str:
    with open(textFile, 'r') as file:
        content = file.read()
    return content

# opdracht 1
def getNumberOfCharacters(text: str) -> int:
    aantal_karakters = 0
    for karakter in text: 
        if karakter in ALLOWED_IN_WORD:
            aantal_karakters +=1
    return aantal_karakters


# opdracht 2

def getNumberOfSentences(text: str) -> int:
    aantal_zinnen = 0
    testen = False
    for sentence in text:
        if sentence  in ['.','!','?']:
           testen = True
        else :
            testen = False 
        if testen:  # If testen is True -> betekent dat de letter gelijk is aan  '.','!' of'?'  en dus de zin is klaar. 
            aantal_zinnen += 1
    
    return aantal_zinnen 


# opdracht 3
#Ga er vanuit dat een woord alleen bestaat uit: 
# “0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-” en minimaal 2 karakters lang is.
def getNumberOfWords(text: str) -> int:
    testen = False
    aantal = 0
    for karakter in text:
        if karakter == " ":
            testen = True
        else:
            testen = False
        if testen:
            aantal += 1
    aantal += 1
    return aantal

print(getNumberOfWords("""1Programmeren 2is 3het 4proces 5van 6het 7creëren 8van 9instructies 10die 11een 12computer 13kan 14uitvoeren 15om 16een 17bepaald 18doel 19te 20bereiken, 21zoals 22het 23maken 24van 25een 26website, 27een 28spel 29of 30een 31app.
32Programmeren 33vereist 34logisch 35denken, 36creativiteit 37en 38kennis 39van 40verschillende 41programmeertalen, 42die 43elk 44hun 45eigen 46syntaxis, 47functies 48en 49toepassingen 50hebben.
51Programmeren 52kan 53leuk, 54uitdagend 55en 56lonend 57zijn, 58maar 59ook 60frustrerend, 61complex 62en 63tijdrovend, 64afhankelijk 65van 66de 67moeilijkheidsgraad 68van 69het 70project, 71de 72kwaliteit 73van
 74de 75code 76en 77de 78beschikbaarheid 79van 80hulpmiddelen 81en 82bronnen."""))