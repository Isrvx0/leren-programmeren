from functions import *

print(welcome_message())

# variable :
bakjes = 0
hoorntjes = 0
topping_price = 0

smaken_lijst = []

extra_bestellen = True
while extra_bestellen:
    # kiezen hoeveel bolletjes :
    soort_klant = particulier_or_zakelijk()
    hoeveelheid = hoeveelheid_vragen(soort_klant)
    
    # kiezen tussen hoorntje or bakje :
    keuze = keuze_maken(hoeveelheid ,soort_klant)
    if keuze == "hoorntje":
        hoorntjes += 1
    elif keuze == "bakje":
        bakjes += 1

    # kiezen van een smaak :
    smaken_lijst += smaak_kiezen(hoeveelheid , soort_klant)

    # kiezen van topping :
    topping = topping_kiezen(soort_klant)
    topping_price += topping_prijs(topping,hoeveelheid,keuze)

    # vragen of ze meer willen bestellen :
    meer_bestellen = buy_more(soort_klant)
    if meer_bestellen.lower() in ( "stop" , "nee"):
        extra_bestellen = False

print("Bedankt en tot ziens! ")
                        
# bonnetje printen : 
bon = bonnetje(smaken_lijst, hoorntjes, bakjes , topping_price , soort_klant)
print("--------------['Papi Gelato']--------------")
for item in bon:
    print(item)