from functions import *

print(welcome_message())

# variable :
bolletjes = 0
bakjes = 0 
hoorntjes = 0

extra_bestellen = True
while extra_bestellen:
    aantal_bolletjes = hoeveelheid_vragen()
    
    if aantal_bolletjes <= 8:
        bolletjes += aantal_bolletjes 
        smaken_lijst = smaak_kiezen(aantal_bolletjes)
        keuze = keuze_maken(aantal_bolletjes)
        if keuze == "hoorntje":
            hoorntjes += 1
        else:
            bakjes += 1

        meer_bestellen = buy_more()
        if meer_bestellen.lower() in ( "stop" , "nee"):
            print("Bedankt en tot ziens! ")
            #print(bonnetje(bolletjes , hoorntjes, bakjes))
            bon = bonnetje(smaken_lijst,bolletjes , hoorntjes, bakjes)
            print("--------------['Papi Gelato']--------------")
            for item in bon:
                print(item)
            extra_bestellen = False
    
    elif aantal_bolletjes > 8:
        print('Sorry, zulke grote bakken hebben we niet')
    
    else:
        print('Sorry dat snap ik niet!' )