# sollicitatie.py
naam = input ("wat is je naam?")
print ("welkom" , naam )
print (" we gaan nu paar vragen aan je stellen. en met behulp van deze vragen ...")
print (" bepalen we of je mag gaan solliciteren naar deze functie")

dierendressuur = input (" ben je meer dan 4 jaar praktijkervaring met dieren-dressuur? ") 
if dierendressuur == 'nee':
     jongeleren= input (" ben je meer dan 5 jaar ervaring met jongleren? ")
     if jongeleren == 'nee':
        acrobatiek= input (" ben je meer dan 3 jaar praktijkervaring met acrobatiek? ")
if dierendressuur or jongeleren or acrobatiek == 'ja':
    heeft_ervaring = True 

diploma = input (" ben je bezit van een Diploma MBO-4 ondernemen? ")
if diploma == 'ja':
    heeft_diploma = True

rijbewijs = input ("ben je bezit van een geldig Vrachtwagen rijbewijs? ")
if rijbewijs == 'ja':
    heeft_rijbewijs = True

hoed = input (" ben je bezit van een hoge hoed? ")
if hoed == 'ja':
    heeft_hoed = True

man = input (" ben je een man en heeft Snor breder dan 10 cm? ")
if man == 'nee':
    vrouw = input ('ben je dan een vrouw en draagt rood krulhaar langer dan 20 cm? ')
    if man or vrouw == "ja":
        haar_snor = True

lengte = int ( input ("wat is je lengte") ) 
if lengte >= 150:
    goed_lengte = True

gewicht = int ( input ("wat is je lichaamsgewicht? " ) )
goede_gewicht= gewicht > 90

gevaarlijkPersoon = input (" heb je Overleven met gevaarlijk personeel? ")
if gevaarlijkPersoon == 'ja': 
    goede_persoon = True


# extra vragen
English =  input ('spreek je goed English?')
jas = ( input ("ben je bezit van een rode jas? "))
dieren = input ('vind je leuk om met lionleeuws te werken ?')
antwoorden = input ("heb je alle vragen eerlijk beantwoordt? ")

# controleren
geslaagd = heeft_diploma and heeft_ervaring and heeft_rijbewijs and heeft_hoed and haar_snor and goed_lengte and goede_gewicht and goede_persoon

if geslaagd:
    print ("je bent geslaagd met de test, we wachten op je voor een gesprek," , naam )
else:
  print ("sorry, je voldaat niet aan de eisen")






