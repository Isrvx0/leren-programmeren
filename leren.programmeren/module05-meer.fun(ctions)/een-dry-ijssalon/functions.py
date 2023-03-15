def welkom_message():
    welkom_message = "Welkom bij Papi Gelato. Je mag alle smaken kiezen zolang het maar vanille ijs is\n"
    return welkom_message


def bolletjes():
    aantal_bolletjes = " " 
    while type(aantal_bolletjes) != int:
        try:
            aantal_bolletjes = int(input("Hoeveel bolletjes wilt u?"))
        except ValueError:
            print('Sorry dat snap ik niet!' )
    return aantal_bolletjes

def bakjes():
    aantal_bakjes = " " 
    while type(aantal_bakjes) != int:
        try:
            aantal_bakjes= int(input("Hoeveel bakjes wilt u?"))
        except ValueError:
            print('Sorry dat snap ik niet!' )
    return aantal_bakjes

def hoorntjes():
    aantal_hoorntjes = " " 
    while type(aantal_hoorntjes) != int:
        try:
            aantal_hoorntjes = int(input("Hoeveel hoorntjes wilt u?"))
        except ValueError:
            print('Sorry dat snap ik niet!' )
    return aantal_hoorntjes

def buy_more():
    extra = input('Wilt u nog meer bestellen?  ')
    return extra 


def bonnetje(bolletjes , hoorntjes , bakjes):
    bon = [{
        "Bolletjes  " : f"{bolletjes} * €1.10 = {(bolletjes * 1.10)}"
    },{
        "Hoorntjes  " : f"{hoorntjes} * €1.25 = {(hoorntjes * 1.25)}"
    },{
        "Bakjes     " : f"{bakjes} * €0.75 = {(bakjes * 0.75)}"
    },{
        f"Totaal = € {(bolletjes * 1.10 + hoorntjes * 1.25 + bakjes * 0.75 )}"
    }]
    return bon


#     print ('[------BOODSCHAPENLIJST------')
# print("{:<10} {:<10} ".format('ITEMS', 'HOEVEELHEID')) #namen van de kolommen.
# for key, value in boodschappen_lijst.items(): # print elk gegevens-item.
#     print("{:<10} {:<10}".format(key, value))  # (:<10) = Hoe ver uit elkaar.  



# print(myList[0]['bar'])
# bon = {"bier":{naam: "bier",prijs: 2.50, amount: 0} , "wijn":{naam: "wijn",prijs: 3.75,amount: 0},"fris":{naam: "fris",prijs: 1.65,amount: 0}}











# def vraag_naar_aantal(aantal_bolletjes):
#     try:
#         aantal_bolletjes = int(input("Hoeveel bolletjes wilt u?   "))
#         if aantal_bolletjes <= 3:
#             return_variable = keuze_maken(aantal_bolletjes)
#         elif aantal_bolletjes >= 4 and aantal_bolletjes <= 8:
#             return_variable =  meer_bestellen(aantal_bolletjes)
#         elif aantal_bolletjes > 8:
#             print('Sorry, zulke grote bakken hebben we niet')
#             return_variable =  vraag_naar_aantal()
#     except ValueError:
#         print('Sorry dat snap ik niet!' )
#         return_variable =  vraag_naar_aantal()
#     return return_variable

# def keuze_maken(aantal):
#     keuze= input(f'Wilt u deze {aantal} bolletjes in een hoorntje of een bakje?  ')
#     if keuze.lower() in ('bakje' , 'hoorntje') :
#        return_variable = meer_bestellen(aantal)
#     else:
#         print('Sorry dat snap ik niet!' )
#         return_variable =  keuze_maken(aantal)
#     return return_variable 

# def meer_bestellen(aantal):
#     extra = input(f'Dan krijgt u van mij een bakje met {aantal} bolletjes\nWilt u nog meer bestellen?  ')
#     if extra.lower() in ("stop" , "nee"):
#         print("Bedankt en tot ziens! ")
#         exit()
#     else:
#         return_variable = vraag_naar_aantal()
#     return return_variable 