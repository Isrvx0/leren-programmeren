nummerr= int(input('voer een nummer:  '))
def tafelVanNummers (nummer):
    print (f'tafel van {nummer} is:')
    for i in range (1,11):
        print (f'{nummer} x {i} = ', nummer*i)

print(tafelVanNummers(nummerr))

# ______

nummerr= int(input('voer een nummer:  '))

print (f'tafel van nummer {nummerr} : \n')
tafel_van_nummers= lambda nummer : [print(f'{i} * {nummer} =', i*nummer) for i in range (1,11)]

print(tafel_van_nummers(nummerr))
