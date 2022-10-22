from fruitmand import fruitmand

fruitmand.remove(fruitmand[4])
newList= []

for color in range (0,6):
    colorr= fruitmand[color]['color']
    if colorr not in newList:
        newList.append(colorr)

print ('Alle unieke kleuren in de fruitmand ' , newList)







