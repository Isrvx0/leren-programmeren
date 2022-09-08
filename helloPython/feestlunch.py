# feestlunch.py 
print ('feestlunch.py')
print ('totaal prijs van producten')
croissantjes = input ("te berekenen prijs")
aantalcriossantjes1 = int (croissantjes)

croissantjesprijs = 0.39

aantalcriossantjes = 0.39
croissantjes = aantalcriossantjes * aantalcriossantjes1

stockbordperstuk = 2.78
aantalstockborden = 2
stockbordprijs = aantalstockborden * stockbordperstuk

kortingbon = 1.50

totaalprijs = float (croissantjes + stockbordprijs) - kortingbon


print ( 'crossantjes prijs' , croissantjes )
print ('stockbord prijs' , stockbordprijs )
print ('totaalprijs', totaalprijs)
print ('de feestluch kost me bij de bakker' , totaalprijs , 'voor' , aantalcriossantjes1 , ' croissantjes en' , aantalstockborden , ' stockborden  als de kortingsbonen nog geldig zijn')
