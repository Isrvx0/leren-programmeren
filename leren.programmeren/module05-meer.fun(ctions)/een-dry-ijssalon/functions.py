import sys

def start_function():
    welkom_message = "Welkom bij Papi Gelato. Je mag alle smaken kiezen zolang het maar vanille ijs is\n"
    return welkom_message

def stap_1():
    try:
        aantal_bolletjes = int(input("Hoeveel bolletjes wilt u?   "))
        if aantal_bolletjes <= 3:
            return stap_2(aantal_bolletjes)
        elif aantal_bolletjes >= 4 and aantal_bolletjes <= 8:
            return stap_3(aantal_bolletjes)
        elif aantal_bolletjes > 8:
            print('Sorry, zulke grote bakken hebben we niet')
            return stap_1()
    except ValueError:
        print('Sorry dat snap ik niet!' )
        return stap_1()
    

def stap_2(aantal):
    keuze= input(f'Wilt u deze {aantal} bolletjes in een hoorntje of een bakje?  ')
    if keuze.lower() in ('bakje' , 'hoorntje') :
       print(f"\nHier is uw {aantal} bolletjes in een {keuze}")
       return stap_3()
    else:
        print('Sorry dat snap ik niet!' )
        return stap_2(aantal)

def stap_3(aantal):
    extra = input(f'Dan krijgt u van mij een bakje met {aantal} bolletjes\nWilt u nog meer bestellen?  ')
    if extra.lower() in ("stop" , "nee"):
        sys.exit("Bedankt en tot ziens! ")
    else:
        return stap_1()

