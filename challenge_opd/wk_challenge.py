import random

LANDEN_GROEP_A = []
TEGEN_GROEP = []
WEDSTRIJD = {}

# namen van landen
for num in range (1,4):
    groep_A = input(f"Wat is land {num} die mee speelt in groep A?  ")
    LANDEN_GROEP_A.append(groep_A)
    TEGEN_GROEP.append(groep_A)

# verdelen van landen :
for landen in LANDEN_GROEP_A:
    keuze= random.choice(TEGEN_GROEP)
    if len(TEGEN_GROEP) == 1 and keuze == landen:
        TEGEN_GROEP.clear()
        for landen in LANDEN_GROEP_A:
            TEGEN_GROEP.append(landen)
        for landen in LANDEN_GROEP_A:
            keuze= random.choice(TEGEN_GROEP)
            while landen == keuze:
                keuze = random.choice(TEGEN_GROEP)
            WEDSTRIJD[landen] = keuze
            TEGEN_GROEP.remove(keuze)
    else:
        while landen == keuze:
            keuze = random.choice(TEGEN_GROEP)
        WEDSTRIJD[landen] = keuze
        TEGEN_GROEP.remove(keuze)

# DOELPUNTEN:
for key , value in WEDSTRIJD.items():
    land_1 = int(input(f'score van land {key}:  '))
    land_2 = int(input(f'score van land {value}:  '))
    if land_1 > land_2:
        winnaar = 'land 1'
    elif land_1 < land_2 :
        winnaar = 'land 2'
    elif land_1 == land_2 :
        winnaar = 'Gelijk speel'
    print("\n{:<20} {:<20} {:<30} {:<20} {:<30}".format('Thuis', 'Uit' , 'Doelpunten land 1' , 'Doelpunten land 2' , 'Winnaar')) 
    print ("{:<20} {:<20} {:<30} {:<20} {:<30} ".format( key, value , land_1 , land_2 , winnaar))
