def welcome_message():
    welkom_message = "Welkom bij Papi Gelato. Je mag alle smaken kiezen zolang het maar vanille ijs is\n"
    return welkom_message


def hoeveelheid_vragen():
    aantal_bolletjes = " " 
    while type(aantal_bolletjes) != int:
        try:
            aantal_bolletjes = int(input("Hoeveel bolletjes wilt u?  "))
        except ValueError:
            print('Sorry dat snap ik niet!' )
    return aantal_bolletjes

def smaak_kiezen(aantal):
    choice = True
    teller = 0
    smaken_lijst = []
    
    lijst = [{'name' : 'aardbei', 'amount' : 0, 'price' : 1.10},{ 'name' : 'chocolade', 'amount' : 0, 'price' : 1.10},{ 'name' : 'munt', 'amount' : 0, 'price' : 1.10},{'name' : 'vanille', 'amount' : 0, 'price' : 1.10}]

    while choice:
        smaak = input( f"Welke smaak wilt u voor bolletje nummer {teller+1}?\nA) Aardbei, C) Chocolade, M) Munt of V) Vanille? ")
        if smaak.lower() in ("aardbei","chocolade","munt","vanille"):
            teller += 1
            for element in lijst:
                if element['name'] == smaak:
                    element['amount'] += 1 
                           
        else:
            print("Sorry! Dat snap ik niet... ")
        if teller == aantal:
            choice= False

    # check if an items == 0
    for smaak in lijst:
        if smaak['amount'] > 0:
            smaken_lijst.append(smaak) 

    return smaken_lijst



def keuze_maken(aantal):
    choice = True
    while choice:
        if aantal >= 4 and aantal <= 8:
            print(f"Dan krijgt u van mij een bakje met {aantal} bolletjes\n")
            keuze = "bakje"
        elif aantal <= 3:
            keuze = input(f'Wilt u deze {aantal} bolletjes in een hoorntje of een bakje?  ')
            if  keuze.lower() in ("hoorntje" , "bakje"):
                print(f"Dan krijgt u van mij een {keuze} met {aantal} bolletjes\n")
                choice = False
        else:
            print('Sorry dat snap ik niet!' )
    return keuze


def buy_more():
    extra = input('Wilt u nog meer bestellen?  ')
    return extra 


def bonnetje(smaken_lijst , bolletjes , hoorntjes , bakjes):
    totaal_prijs = 0
    bon = []
    lijst = [{ 'name' : 'bakjes', 'amount' : bakjes, 'price' : 0.75},
             { 'name' : 'hoorntjes', 'amount' : hoorntjes, 'price' : 1.25 }]
    
    for element in lijst:
        if element['amount'] == 0:
            lijst.remove(element) 
    bestellen = list(smaken_lijst + lijst)
    space = " "
    for item in bestellen:
        price = item["amount"] * item["price"] 
        totaal_prijs += price
        bon.append(f'{item["name"]}{space*10}:{space*10}{item["amount"]} * €{item["price"]}{space*10}= €{round(price ,2)}')
    
    bon.append(f"totaal ={space*10}€{round(totaal_prijs + (bolletjes * 1.10),2)}")
    return bon












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