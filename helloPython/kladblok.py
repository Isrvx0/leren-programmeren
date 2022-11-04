nummerr= int(input('voer een nummer:  '))
def tafelVanNummers (nummer):
    print (f'tafel van {nummer} is:')
    for i in range (1,11):
        print (f'{nummer} x {i} = ', nummer*i)

print(tafelVanNummers(nummerr))