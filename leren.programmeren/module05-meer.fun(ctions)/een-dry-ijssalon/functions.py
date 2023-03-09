def welkom_message():
    welkom_message = "Welkom bij Papi Gelato. Je mag alle smaken kiezen zolang het maar vanille ijs is\n"
    return welkom_message

def vraag_naar_aantal(aantal_bolletjes):
    try:
        aantal_bolletjes = int(input("Hoeveel bolletjes wilt u?   "))
        if aantal_bolletjes <= 3:
            return_variable = keuze_maken(aantal_bolletjes)
        elif aantal_bolletjes >= 4 and aantal_bolletjes <= 8:
            return_variable =  meer_bestellen(aantal_bolletjes)
        elif aantal_bolletjes > 8:
            print('Sorry, zulke grote bakken hebben we niet')
            return_variable =  vraag_naar_aantal()
    except ValueError:
        print('Sorry dat snap ik niet!' )
        return_variable =  vraag_naar_aantal()
    return return_variable

def keuze_maken(aantal):
    keuze= input(f'Wilt u deze {aantal} bolletjes in een hoorntje of een bakje?  ')
    if keuze.lower() in ('bakje' , 'hoorntje') :
       return_variable = meer_bestellen(aantal)
    else:
        print('Sorry dat snap ik niet!' )
        return_variable =  keuze_maken(aantal)
    return return_variable 

def meer_bestellen(aantal):
    extra = input(f'Dan krijgt u van mij een bakje met {aantal} bolletjes\nWilt u nog meer bestellen?  ')
    if extra.lower() in ("stop" , "nee"):
        print("Bedankt en tot ziens! ")
        exit()
    else:
        return_variable = vraag_naar_aantal()
    return return_variable 