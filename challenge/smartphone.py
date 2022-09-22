print ("keuzprogramma")

samsung = int (input ('Hoe duur de samsung telefoon is?  '))
iphone = int (input ('Hoe duur de Iphone telefoon is?  '))
zenFone= int (input ('Hoe duur de Asus Zenfone telefoon is?  '))

maxgetal= max(samsung , iphone , zenFone)
mingetal= min(samsung , iphone , zenFone)

def middle(samsung, iphone, zenFone) : 
    return min(max(samsung,iphone),max(iphone,zenFone),max(samsung,zenFone))

# verschil
verschil= iphone - samsung #if iphone niet duurder dan 50 euro van samsung
verschil1= samsung - zenFone #if zenfone 100 euro goedkoper dan samsung
verschil2= iphone - zenFone #if zenfone 100 euro goedkoper dan Iphone

#duurste
()
if iphone == maxgetal:
     duurste= print ('Iphone is duurder dan de samsung en de ZenFone')
     print (f"de iphone is dus het duurste, de telefoon kost {iphone} euro")
elif samsung == maxgetal:
     duurste= print ('samsung is duurder dan de Iphone en de ZenFone')
     print (f'de samsung is dus het duurste, de telefoon kost {samsung} euro ')
else:
     duurste= print ('ZenFone is duurder dan de Iphone en de samsung ')
     print (f' deZenFone is dus het duurste, de telefoon kost {zenFone} euro')

# goedkoopste  
()   
if iphone == mingetal:
     goedkoopste= print ('Iphone is goedkoopste dan de samsung en de ZenFone')
     print (f"de iphone is dus het goedkoopste, de telefoon kost {iphone} euro")
     
elif samsung == mingetal:
     goedkoopste= print ('samsung is goedkoopste dan de Iphone en de ZenFone') 
     print (f'de samsung is dus het goedkoopste, de telefoon kost {samsung} euro ')
else:
     goedkoopste= print ('ZenFone is goedkoopste dan de Iphone en de samsung ')
     print (f'de ZenFone is dus het goedkoopste, de telefoon kost {zenFone} euro')
#gelijk
()
if iphone == samsung and iphone == zenFone and samsung == zenFone:
     gelijk= print ('prijzen zijn gelijk')
elif samsung == iphone:
     gelijk= print ('samsung en iphone zijn gelijk')
elif samsung == zenFone:
     gelijk= print ('samsung en zenFone zijn gelijk')
elif iphone == zenFone:
     gelijk= print ('ZenFone en Iphone zijn gelijk')

#tussen
()
if iphone == middle(samsung, iphone, zenFone):
     print (f"de iphone zit er tussen met {iphone} euro")
elif samsung == middle(samsung, iphone, zenFone):
     print (f'de samsung zit er tussen met {samsung} euro ')
else:
     print (f' de ZenFone zit er tussen met {zenFone} euro')

#advies
if samsung > 900 or iphone > 900 or zenFone > 900:
     print ("het advies is dus geen telefoon te kopen, ze zijn te duur!")
elif verschil1 >= 100 and verschil2 >= 100:
     print (f'het advies is dus om ZenFone te kopen. Deze is namelijk {verschil1} goedkoper dan samsung en {verschil2} goedkoper dan Iphone ')
elif verschil >= 50:
     print (f'"het advies is dus de Iphone te kopen. Deze is namelijk {verschil} goedkoper dan de samsung en {verschil2} goedkoper dan de Zenphone!"')
elif iphone == mingetal:
     print (f'"het advies is dus de iphone te kopen. Deze is namelijk {verschil} goedkoper dan de samsung en {verschil2} goedkoper dan de zenPhone"') 
elif samsung == mingetal:     
     print (f'"het advies is dus de samsung te kopen. Deze is namelijk {verschil} goedkoper dan de Iphone en {verschil1} goedkoper dan de zenPhone"') 