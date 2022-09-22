# smartphone challlenge 
print ("keuzprogramma")
()
()
samsung = int (input ('Hoe duur de samsung telefoon is?  '))
iphone = int (input ('Hoe duur de Iphone telefoon is?  '))

# duurste mobiel bepalen
if samsung > iphone:
     print ('Samsung is duurder dan de Iphone')
     ()
     ()
     print (f'de samsung is het duurste, de telefoon kost {samsung} euro ')
     print (f"de iphone is het goedkoopste, de telefoon kost {iphone} euro")
     mingetal = iphone 
     maxgetal = samsung
     verschil= maxgetal - mingetal
     advies= print (f'"het advies is dus de Iphone te kopen. Deze is namelijk {verschil} goedkoper dan de samung"')
        
elif iphone > samsung:
    print ('iphone is duurder dan de samsung')
    ()
    ()
    print (f"de iphone is het duurste, de telefoon kost {iphone} euro")
    print (f'de samsung is het goedkoopste, de telefoon kost {samsung} euro ')
    mingetal = samsung
    maxgetal = iphone
    verschil= maxgetal - mingetal
    if verschil <= 50:
        print (f'"het advies is dus de Iphone te kopen. Deze is namelijk {verschil} goedkoper dan de samung"')
    else:
        advies= print (f'"het advies is dus de samsung te kopen. Deze is namelijk {verschil} goedkoper dan de Iphone"') 

else: 
    iphone == samsung
    print ('de twee telefonen zijn even duur. het advies is de Iphone te kopen, want je hebt een voorkeur voor')
