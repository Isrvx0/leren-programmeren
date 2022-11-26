
def persoonlijke_gegevens(dict): 
    for key in dict:
        print(key, "is", dict[key] , "jaar oud.")

vraag = 'ja'
gegevens= {}
while vraag == 'ja':
    naam= input('Wat is de naam van de persoon?  ')
    leeftijd= int(input(f'wat is de leeftijd van {naam}?  '))
    gegevens.update ( { naam : leeftijd})
    vraag = input('Wil je nog namen toevoegen? ')

persoonlijke_gegevens(gegevens)