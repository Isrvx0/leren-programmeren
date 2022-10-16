#boodschappen lijst maken

input ('Om uw boodschappenlijstje te starten, klik op enter! ')
boodschappen_lijst = {}
items_list= []
aantal_list= []

while True:
    items = input('Voeg uw item toe:  ')
    items_list.append(items.lower())
    aantal= int(input(f'Hoeveel {items} wil je?   '))
    aantal_list.append(aantal)
    extra = input("Wil je meer items toevoegen? (ja/nee): \n")
    if extra.lower() != "ja":
      break

zipp_list = zip(items_list,aantal_list) 
boodschappen_lijst = dict(zipp_list) 

if extra.lower() == 'nee':
    print ('[------BOODSCHAPENLIJST------')
print("{:<10} {:<10} ".format('ITEMS', 'HOEVEELHEID')) #namen van de kolommen.
for key, value in boodschappen_lijst.items(): # print elk gegevens-item.
    print("{:<10} {:<10}".format(key, value))  # (:<10) = Hoe ver uit elkaar.  