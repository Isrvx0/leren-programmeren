#opdracht 1.

for nummer in range (1,14):
    print (f'Tafel van {nummer}:')
    for multiplier in range (1,11):
        print(f'{nummer} x {multiplier} =  ' , nummer * multiplier)

#opdarcht 2 t/m 12:
#opgave 2:
getalen_lijst = ['5','12','19','27','3']

#opgave 3:
getalen_lijst.append('25')

#opgave 4:
print(len(getalen_lijst))

#opgave 5:
print (getalen_lijst)
getalen_lijst.remove('12')
print(getalen_lijst)
