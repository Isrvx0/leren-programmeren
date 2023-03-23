def welcome_message():
    welkom_message = "Welkom bij Papi Gelato\n"
    return welkom_message

def particulier_or_zakelijk():
    choice_maken = True
    while choice_maken:
        soort_klant = input("Bent u 1) een particuliere klant of 2) een zakelijke klant?  ")
        if soort_klant.lower() in ('1','2'):
            choice_maken = False
    return soort_klant

def hoeveelheid_vragen(soort_klant):
    hoeveelheid_vragen = True
    while hoeveelheid_vragen:
        try:
            if soort_klant == "1":
                hoeveelheid = int(input("Hoeveel bolletjes wilt u?  "))
                if hoeveelheid > 8:
                    print("Sorry, zulke grote bakken hebben we niet")
                elif hoeveelheid <= 8:
                    hoeveelheid_vragen = False
            
            elif soort_klant == "2":
                hoeveelheid = int(input("Hoeveel liter wilt u?  "))
                hoeveelheid_vragen = False

        except ValueError:
            print('Sorry dat snap ik niet!' )
    
    return hoeveelheid

def smaak_kiezen(aantal , soort_klant):
    choice = True
    teller = 0
    smaken_lijst = []
    
    hoveelheid = "bolletjes"
    if soort_klant == '2':
        hoveelheid = "liter"
    
    while choice:
        smaak = input( f"Welke smaak wilt u voor {hoveelheid} {teller+1}?\nA) Aardbei, C) Chocolade, M) Munt of V) Vanille? ")
        if smaak.lower() in ("aardbei","chocolade","munt","vanille"):
            teller += 1
            smaken_lijst.append(smaak.lower()) 
        else:
            print("Sorry! Dat snap ik niet... ")
        if teller == aantal:
            choice= False

    return smaken_lijst

def keuze_maken(aantal , soort_klant):
    choice = True
    keuze = " "
    
    while choice:
        if soort_klant == "1":
            if aantal <= 3:
                keuze = input(f'Wilt u deze {aantal} bolletjes in een hoorntje of een bakje?  ')
                if  keuze.lower() in ("hoorntje" , "bakje"):
                    print(f"Dan krijgt u van mij een {keuze} met {aantal} bolletjes\n")
                    choice = False
                else:
                    print('Sorry dat snap ik niet!' )
            elif aantal >= 4 and aantal <= 8:
                print(f"Dan krijgt u van mij een bakje met {aantal} bolletjes\n")
                keuze = "bakje"
                choice = False
        elif soort_klant == "2":
            choice = False
    return keuze

def topping_kiezen(soort_klant):
    topping = True

    while topping:
        if soort_klant == "1":
            choice = input("Wat voor topping wilt u: \nA) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus? ")
            if choice.lower() in ("a","b","c","d"):
                topping = False
            else:
                print("sorry dat snap ik niet")
        elif soort_klant == "2":
            choice = "a"
            topping = False
    return choice.lower()

def topping_prijs(gekozen_topping , bolletjes , hoorntje_bakje):
    if gekozen_topping == "a":
        price = 0
    elif gekozen_topping == "b":
        price = 0.50
    elif gekozen_topping == "c":
        price = 0.30 * bolletjes
    elif gekozen_topping == "d":
        if hoorntje_bakje == "bakje":
            price = 0.90
        elif hoorntje_bakje == "hoorntje":
            price = 0.60
    return round(price,2)

def buy_more(soort_klant):
    if soort_klant == "1":
        extra = input('Wilt u nog meer bestellen?  ')
    elif soort_klant == "2":
        extra = "stop"
    return extra 


def bonnetje(smaken_lijst,hoorntjes,bakjes,topping_price,soort_klant):
    totaal_prijs = 0
    winkel_elements = [
             { 'name' : 'aardbei', 'amount' : 0, 'price' : 1.10},
             { 'name' : 'chocolade', 'amount' : 0, 'price' : 1.10},
             { 'name' : 'vanille', 'amount' : 0, 'price' : 1.10 },
             { 'name' : 'munt', 'amount' : 0, 'price' : 1.10 },
             { 'name' : 'hoorntjes', 'amount' : hoorntjes, 'price' : 1.25 },
             { 'name' : 'bakjes', 'amount' : bakjes, 'price' : 0.75}]
    
    bon = []
    lijst = []
    
    #smaken vullen :
    for item in winkel_elements:
        for smaak in smaken_lijst:
            if smaak == item['name']:
                item['amount'] += 1
    
    # Voegen van elements die als amount > 0 hebben:
    for element in winkel_elements:
        if element['amount'] > 0:
            lijst.append(element) 
    
    space = " "
    
    #prijs bereken :
    for item in lijst:
        item_price = item["price"]
        
        if soort_klant == '2':
            price = item["amount"] * 9.80
            item_price = 9.80
        elif soort_klant == '1':
            price = item["amount"] * item_price 
        
        totaal_prijs += price
        bon.append(f'{item["name"]}{space*10}:{space*10}{item["amount"]} X {item_price}{space*10}= €{price}')

    # checken als topping worden gekozen :
    if topping_price > 0:
        bon.append(f'topping  {space*10}:{space*29} €{round(topping_price ,2)}')
    
    totaal_prijs += topping_price
    bon.append(f"Totaal   {space*10}={space*29} €{round(totaal_prijs,2)}")
    
    if soort_klant == '2':
        bon.append(F"BTW (9%) ={space*10}€2.43")
    
    return bon


# print("{:<10} {:<10} ".format('ITEMS', 'HOEVEELHEID')) #namen van de kolommen.
# for key, value in boodschappen_lijst.items(): # print elk gegevens-item.
#     print("{:<10} {:<10}".format(key, value))  # (:<10) = Hoe ver uit elkaar.  



# def bonnetje(bolletjes , hoorntjes , bakjes):
#     bon = [{
#         "Bolletjes  " : f"{bolletjes}  * €1.10 = €{round(bolletjes * 1.10 , 2)}"
#     },{
#         "Hoorntjes  " : f"{hoorntjes}  * €1.25 = €{round(hoorntjes * 1.25 ,2)}"
#     },{
#         "Bakjes     " : f"{bakjes}  * €0.75 = €{round(bakjes * 0.75 ,2)}"
#     },{
#         f"Totaal      = € {round(bolletjes * 1.10 + hoorntjes * 1.25 + bakjes * 0.75 ,2)}"
#     }]
    
#     # check if an items == 0
#     if bakjes == 0:
#         bon.remove(bon[2])
#     elif hoorntjes == 0:
#         bon.remove(bon[1])
    
#     return bon


# for index in range (0,len(smaken_list)):
#     name.append(smaken_list[index]['name'])

# for index in range (0,len(smaken_list)):
#     aantal.append(smaken_list[index]['amount'])

# for index in range (0,len(smaken_list)):
#     price.append(smaken_list[index]['price'])

# for name,aantal,price in zip(name,aantal,price):
#     print('{:10} {:10} {:5}'.format(name,aantal,price))

















#     bon = []
#     for index in range (len(lijst)):
#         bon.append(f'{lijst[index]["name"]}' + f'{lijst[index]["amount"]} * 1,10 = €{round(lijst[index]["amount"] * 1.10 , 2)}')
        
#     bon = [{
#         "Hoorntjes  " : f"{hoorntjes}  * €1.25 = €{round(hoorntjes * 1.25 ,2)}"
#     },{
#         "Bakjes     " : f"{bakjes}  * €0.75 = €{round(bakjes * 0.75 ,2)}"
#     },{
#         f"Totaal      = € {round(bolletjes * 1.10 + hoorntjes * 1.25 + bakjes * 0.75 ,2)}"
#     }]

    
#     # check if an items == 0
#     if bakjes == 0:
#         bon.remove(bon[-2])
#     elif hoorntjes == 0:
#         bon.remove(bon[-2])
    
#     return bon