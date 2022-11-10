from fruitmand import fruitmand


fruit = filter (lambda fruit: fruit['name'] == 'druif' , fruitmand)
for f in fruit:
    fruitmand.remove(f)

newList= []

for color in range (0,len(fruitmand)):
    colorr= fruitmand[color]['color']
    if colorr not in newList:
        newList.append(colorr)

print ('Alle unieke kleuren in de fruitmand ' , newList)







