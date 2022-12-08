# Zwembadofferte-tool opdracht

#stap 1:
# inhoud berekenen:
lengte= float(input('Voer aub de lengte van het zwembad in meters:  ')) 
breedte= float(input('Voer aub de breedte van het zwembad in meters:  ')) 
diepte= float(input('Voer aub de diepte van het zwembad in meters:  ')) 
inhoud= lengte * breedte * diepte
print (f'{inhoud} m3 grond in totaal moet afgevoerd worden.\n')

#stap 2:
#uitgraven en afvoer kosten:
Kosten_uitgraven= 25 * inhoud
Kosten_afvoeren_grond= 32.50 * inhoud

#stap 3:
#voorijkosten:
afstand= float(input('Voer aub de afstand van het bedrijf naar waar het zwembad moet worden geplaatst:  ')) 

if afstand < 50 and inhoud < 20:
    vaste_prijs= 100
    prijs_per_km= 1.25 * afstand
    voorrijkosten = vaste_prijs + prijs_per_km
elif afstand >= 50 and inhoud < 20:
    vaste_prijs= 100
    prijs_per_km= 1.15 * afstand
    voorrijkosten = vaste_prijs + prijs_per_km
elif afstand < 50 and inhoud >= 20:
    vaste_prijs= 250
    prijs_per_km= 2.15 * afstand
    voorrijkosten = vaste_prijs + prijs_per_km
elif afstand >= 50 and inhoud >= 20:
    vaste_prijs= 250
    prijs_per_km= 2.05 * afstand
    voorrijkosten = vaste_prijs + prijs_per_km

#stap 4:
# Je kunt het weer zien in Stap 1

#stap 5a:
#vierkant meter berekenen:
bodem= lengte * breedte
eerste_muur= breedte * diepte * 2
tweede_muur= lengte * diepte * 2
oppervlakte= bodem + eerste_muur + tweede_muur
print(f"Uw zwembad is {oppervlakte} vierkante meter grrot. ")

#stap 5b:
#beton en tegels berekene:
kleur = input("Wilt u een rode of gekleurde tegels? (antwoord met rood / gekleurde) ")
if inhoud <20 and kleur == "rood":
    baton_kosten= 250 * oppervlakte
    tegel_kosten= 25 * oppervlakte
elif inhoud <20 and kleur == "gekleurde":
    baton_kosten= 250 * oppervlakte
    tegel_kosten= 100 * oppervlakte
elif inhoud > 20 and kleur == "rood":
    baton_kosten= 200 * oppervlakte #11400
    tegel_kosten= 20 * oppervlakte
elif inhoud >20 and kleur == "gekleurde":
    baton_kosten= 200 * oppervlakte
    tegel_kosten= 125 * oppervlakte

baton_en_tegel_kosten= baton_kosten + tegel_kosten

#totaal kosten:
totaal= Kosten_uitgraven + Kosten_afvoeren_grond + voorrijkosten + baton_en_tegel_kosten
print (f'Offerte voor een zwembad van {lengte} bij {breedte} bij {diepte} meter: (inhoud: {inhoud} m3 \n')
print (f'Uitgraven:                   € {round(Kosten_uitgraven)}')
print (f'Afvoeren grond:              € {round(Kosten_afvoeren_grond)} ')
print (f'Voorrijkosten:               € {round(voorrijkosten)} ')
print (f'Beton+tegel {oppervlakte} m2):        € {round(baton_en_tegel_kosten)} ')
print (f'Totaal:                      € {round(totaal)}\n')