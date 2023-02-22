def start_function():
    welkom_message = "Welkom bij Papi Gelato. Je mag alle smaken kiezen zolang het maar vanille ijs is"
    return welkom_message

def stap_1():
    try:
        aantal_bolletjes = int(input("\nHoeveel bolletjes wilt u?   "))
        if aantal_bolletjes <= 3:
            stap_2(aantal_bolletjes)
        elif aantal_bolletjes >= 4 and aantal_bolletjes <= 8:
            print(f"Dan krijgt u van mij een bakje met {aantal_bolletjes} bolletjes")
            stap_3()
        elif aantal_bolletjes > 8:
            print('Sorry, zulke grote bakken hebben we niet')
            stap_1()
    except ValueError:
        print('Sorry dat snap ik niet!' )
        stap_1()
    

def stap_2(aantal):
    keuze= input(f'\nWilt u deze {aantal} bolletjes in een hoorntje of een bakje?  ')
    if keuze.lower() in ('bakje' , 'hoorntje') :
       print(f"Hier is uw {aantal} bolletjes in een {keuze}")
       stap_3()
    else:
        print('Sorry dat snap ik niet!' )
        stap_2(aantal)

def stap_3():
    extra = input('\nWilt u nog meer bestellen?  ')
    if extra.lower() in ("stop" , "nee"):
        print("Bedankt en tot ziens! ")
        exit()
    else:
        stap_1()

