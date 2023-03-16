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
    nummer = 1
    smaken_list = [{ 'name' : 'aardbei', 'amount' : 0},{ 'name' : 'chocolade', 'amount' : 0},{ 'name' : 'munt', 'amount' : 0},{ 'name' : 'vanille', 'amount' : 0}]

    while nummer <= aantal: 
        smaak = input( f"Welke smaak wilt u voor bolletje nummer {nummer}?\nA) Aardbei, C) Chocolade, M) Munt of V) Vanille? ")
        if smaak.lower() in ("aardbei","chocolade","munt","vanille"):
            nummer += 1
            for index in range (len(smaken_list)):
                if smaken_list[index]['name'] == smaak:
                    smaken_list[index]['amount'] += 1            
        else:
            print("Sorry! Dat snap ik niet... ")

    # check if an items == 0
    for smaak in smaken_list:
        if smaak['amount'] == 0:
            smaken_list.remove(smaak) 

    return smaken_list


def keuze_maken(aantal):
    choice = True
    while choice:
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


def bonnetje(smaken_lijst , bolletjes , hoorntjes , bakjes):
    lijst = [{ 'name' : 'bakjes', 'amount' : bakjes, 'price' : 1.70},
             { 'name' : 'hoorntjes', 'amount' : hoorntjes, 'price' : 1.70 }]
    for item in lijst:
        if item['amount'] == 0:
            lijst.remove(item) 
    bon = smaken_lijst + lijst



















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