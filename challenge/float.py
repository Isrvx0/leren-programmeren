LIMIT= 0.3

factor_1 = float(input('getal invoeren:  '))
factor_2 = float(input('getal invoeren:  '))
totaal= factor_1 + factor_2

if totaal < LIMIT or totaal == LIMIT:
    print('keep calm!')
else:
    print ('paniek!')