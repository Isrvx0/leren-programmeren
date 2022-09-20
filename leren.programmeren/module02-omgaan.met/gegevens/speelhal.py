 # speelhal.py
print ('speelhal.py')
print ('totaal kosten van speelhal')

aantalpersonen = input ("aantal personen")
aantalpersonen1 = int ( aantalpersonen )

prijsperpersonen = 745
toegangsticketkosten = prijsperpersonen * aantalpersonen1

prijsgamesit = 39
gamesitkosten = prijsgamesit * aantalpersonen1 

minuten = 9
totaalprijsvipvr = minuten * gamesitkosten 

totaalkosten = int (toegangsticketkosten + totaalprijsvipvr )

print ( 'prijs VIP VR-gamesit ' , totaalprijsvipvr )
print ( 'prijs toegang tickt ' , toegangsticketkosten )
print ( 'totaal kosten' , totaalkosten )
print ( 'Dit geweldige dagje-uit met' , aantalpersonen1 , 'in de speelhal met 45 minuten VR kost me maar' , totaalkosten , 'euro')

