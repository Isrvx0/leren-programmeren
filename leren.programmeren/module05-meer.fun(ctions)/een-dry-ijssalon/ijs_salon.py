from functions import *

print(welkom_message())

extra_bestellen = True
while extra_bestellen:
    aantal_bolletjes = hoeveelheid_vragen()
    if aantal_bolletjes <= 8:
        if aantal_bolletjes <= 3:
            keuze = keuze_maken(aantal_bolletjes)
        else:
            print(f"Dan krijgt u van mij een bakje met {aantal_bolletjes} bolletjes\n")
        
        meer_bestellen = buy_more()
        if meer_bestellen.lower() in ( "stop" , "nee"):
            print("Bedankt en tot ziens! ")
            extra_bestellen = False
    elif aantal_bolletjes > 8:
        print('Sorry, zulke grote bakken hebben we niet')
    else:
        print('Sorry dat snap ik niet!' )
