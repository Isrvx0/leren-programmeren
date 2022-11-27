#opdracht 1.

for nummer in range (1,14):
    print (f'Tafel van {nummer}:')
    for multiplier in range (1,11):
        print(f'{nummer} x {multiplier} =  ' , nummer * multiplier)

#opdarcht 2 t/m 12:
#opgave 2:
getalen_lijst = [5,12,19,27,3]

#opgave 3:
getalen_lijst.append(25)

#opgave 4:
print(len(getalen_lijst))

#opgave 5:
print (getalen_lijst)
getalen_lijst.remove(12)
print(getalen_lijst)

#opgave 6:
print (getalen_lijst)
getalen_lijst.pop(0)
print(getalen_lijst)

#opgave 7:
getalen_lijst.insert(0,36)
print (getalen_lijst)

#opgave 8:
print(sum(getalen_lijst))

#opgave 9:
getalen_lijst.clear()
print(getalen_lijst)

#opdagve 10:
for getalen in range (1,4):
    getalen_lijst.append(getalen)

#opgave 11:
for num in range(4,51):
    getalen_lijst.append(num)

#opgave 12:
print(getalen_lijst[25])

#opgave 13:
getalen_lijst[0], getalen_lijst[-1] = getalen_lijst[-1], getalen_lijst[0] 