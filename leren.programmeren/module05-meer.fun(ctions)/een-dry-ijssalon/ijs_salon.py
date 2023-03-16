from functions import *

print(welcome_message())

# variable :
bolletjes = 0
bakjes = 0 
hoorntjes = 0

extra_bestellen = True
while extra_bestellen:
    aantal_bolletjes = hoeveelheid_vragen()
    bolletjes += aantal_bolletjes 
    if aantal_bolletjes <= 8:
        if aantal_bolletjes <= 3:
            keuze = keuze_maken(aantal_bolletjes)
            if keuze == "hoorntje":
                hoorntjes += 1
            else:
                bakjes += 1
        else:
            print(f"Dan krijgt u van mij een bakje met {aantal_bolletjes} bolletjes\n")
            bakjes += 1

        meer_bestellen = buy_more()
        if meer_bestellen.lower() in ( "stop" , "nee"):
            print("Bedankt en tot ziens! ")
            #print(bonnetje(bolletjes , hoorntjes, bakjes))
            bon = bonnetje(bolletjes , hoorntjes, bakjes)
            print("--------------['Papi Gelato']--------------")
            for itmes in bon:
                print(itmes)
            extra_bestellen = False
    
    elif aantal_bolletjes > 8:
        print('Sorry, zulke grote bakken hebben we niet')
    
    else:
        print('Sorry dat snap ik niet!' )