while True:
    cijfer = float(input('voer de cijfer in.  '))
    if cijfer <= 10:
        break
    else:
        print('kies een cijfer tussen de 0 en 10.')

if cijfer >= 8.5:
    print('A')
elif cijfer == 7.5 or cijfer == 8:
    print('B')
elif cijfer == 6.5 or cijfer == 7:
    print ('C')
elif cijfer == 5.5 or cijfer == 6:
    print ('D')
elif cijfer <=5:
    print('F') 
