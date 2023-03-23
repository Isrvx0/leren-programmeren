from functions import *

print(welcome_message())

# variable :
bolletjes = 0
bakjes = 0 
hoorntjes = 0
topping_price = 0

smaken_lijst = []

extra_bestellen = True
while extra_bestellen:
    # kiezen hoeveel bolletjes :
    aantal_bolletjes = hoeveelheid_vragen()
    bolletjes += aantal_bolletjes 

    # kiezen tussen hoorntje or bakje :
    keuze = keuze_maken(aantal_bolletjes)
    if keuze == "hoorntje":
        hoorntjes += 1
    else:
        bakjes += 1

    # kiezen van een smaak :
    smaken_lijst += smaak_kiezen(aantal_bolletjes)

    # kiezen van topping :
    topping = topping_kiezen()
    topping_price += topping_prijs(topping,aantal_bolletjes,keuze)

    # vragen of ze meer willen bestellen :
    meer_bestellen = buy_more()
    if meer_bestellen.lower() in ( "stop" , "nee"):
        extra_bestellen = False


print("Bedankt en tot ziens! ")
                        
# bonnetje printen : 
bon = bonnetje(smaken_lijst, hoorntjes, bakjes , topping_price)
print("--------------['Papi Gelato']--------------")
for item in bon:
    print(item)