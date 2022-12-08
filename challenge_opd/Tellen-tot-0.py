nummer= int(input('Voer een getal  '))

if nummer < 0:
    for num in range (nummer,1,+1):
        print (num)
else:
    for numb in range (nummer,-1,-1):
        print (numb)