# functies aanmaken:
def addition (number1, number2):
    return number1 + number2
def subtraction	(number1, number2):
    return number1 - number2
def multiplication (number1, number2):
    return number1 * number2
def division (number1, number2):
    return number1 / number2

nummer_1 = -1
twee_getalen = ['a','b','c','d']
extra = True

keuze = input('\nWat wilt u doen? A) getallen optellen, B) getallen aftrekken, C) getallen vermenigvuldigen, D) getallen delen, E) getal ophogen, F) getal verlagen, G) getal verdubbelen of H) getal halveren?” \n kies de letter:   ')

while extra :
    #1 of 2 getalen?
    if nummer_1 >= 0 :
        nummer_1 = antwoord
        if keuze.lower() in twee_getalen:
            nummer_2 = int(input('wat is nummer 2?  '))
    elif keuze.lower() in twee_getalen:
        nummer_1 = int(input('wat is nummer 1?  '))
        nummer_2 = int(input('wat is nummer 2?  '))
    else:
        nummer_1 = int(input('wat is de nummer?  '))

    # function aanroep
    if keuze.lower() == 'a':
       antwoord=  addition(nummer_1 , nummer_2)
    elif keuze.lower() == 'e':
        antwoord=  addition(nummer_1 , 1)
    elif  keuze.lower() == 'b':
        antwoord=  abs(subtraction(nummer_1 , nummer_2))
    elif  keuze.lower() == 'f':
        antwoord=  subtraction (nummer_1 , 1)
    elif keuze.lower() == 'c':
        antwoord=  multiplication (nummer_1 , nummer_2 )
    elif keuze.lower() == 'g':
        antwoord=  multiplication (nummer_1 , 2)
    elif  keuze.lower() == 'd':
        antwoord=  division (nummer_1 , nummer_2)
    elif keuze.lower() == 'h':
        antwoord=  division (nummer_1 , 2)
    print (f"\nDe antwoord is =  {antwoord}")

    # wat wil je met de antwoord?
    keuze = input(f'\n Wil je wat met het antwoord ({antwoord}) doen? A) iets optellen, B) iets aftrekken, C) met iets vermenigvuldigen, D) ergens door delen, E) ophogen, F) verlagen, G) verdubbelen, H) halveren of I) Nee? \n kies de letter:   ')
    if keuze.lower() == 'i':
        extra = False
    else:
        nummer_1 = antwoord