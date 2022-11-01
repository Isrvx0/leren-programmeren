from fruitmand import fruitmand
#opdracht 1
kleuren_list= ['yellow', 'green', 'orange', 'red', 'brown']
while True:
        kleur = input("kies een kleur uit de beschikbare kleuren: %s   " % kleuren_list)
        if kleur.lower() in kleuren_list:
                print(f'De kleur {kleur} zit in de fruitmand')
                break
        else:
                print (f'De kleur {kleur} zit er niet in de fruitmand') 

#opdracht 2
round_fruits= 0
niet_round_fruits= 0

for fruit in range (0,7):
        if fruitmand[fruit]['round']== True and fruitmand[fruit]['color'] == kleur.lower():
                round_fruits +=1
        elif fruitmand[fruit]['round']== False and fruitmand[fruit]['color'] == kleur.lower():
                niet_round_fruits +=1

verschil= abs(round_fruits - niet_round_fruits)
if round_fruits > niet_round_fruits:
        print(f"Er zijn {verschil} meer ronde vruchten dan niet ronde vruchten in de kleur {kleur}")
elif round_fruits < niet_round_fruits :
        print(f"Er zijn {verschil} minder ronde vruchten dan niet ronde vruchten in de kleur {kleur}")
else:
        print(f"Er zijn {verschil} ronde vruchten en {verschil} niet ronde vruchten in de kleur {kleur}")



