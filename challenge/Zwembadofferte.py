# Zwembadofferte-tool opdracht

#stap 1:
# inhoud berekenen: lengte * breedte * hoogte
lengte= float(input('Voer aub de lengte van het zwembad in meters:  ')) #8
breedte= float(input('Voer aub de breedte van het zwembad in meters:  ')) #3
diepte= float(input('Voer aub de diepte van het zwembad in meters:  ')) #1.5
inhoud= lengte * breedte * diepte
print (f'{inhoud} m3 grond in totaal moet afgevoerd worden.')

#stap 2
Kosten_uitgraven= 25 * inhoud
Kosten_afvoeren_grond= 32.50 * inhoud
totaal= Kosten_afvoeren_grond + Kosten_uitgraven
print (f'Offerte voor een zwembad van {lengte} bij {breedte} bij {diepte} meter:\n')
print (f'Uitgraven:                   € {Kosten_uitgraven}')
print (f'Afvoeren grond:              € {Kosten_afvoeren_grond} ')
print (f'Totaal:                      € {totaal}\n')
