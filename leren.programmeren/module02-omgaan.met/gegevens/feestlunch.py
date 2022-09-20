# feestlunch.py 
print ('feestlunch.py')
print ('totaal prijs van producten')

procuten = input ('wat zijn de producten')

product1 = input ('hoeveel stukken criossantjes')
aantalproduct1 = int ( product1 )
croissantjesperstuk = 39
croissantjesprijs = aantalproduct1 * croissantjesperstuk

product2 = input ('hoeveel stukken stockborden')
aantalproduct2 = int ( product2 )
stockbordperstuk = 278
stockbordprijs = stockbordperstuk * aantalproduct2 

kortingbon = 150

totaalprijs = int  (croissantjesprijs + stockbordprijs) - kortingbon


print ( 'crossantjes prijs' , croissantjesprijs )
print ('stockbord prijs' , stockbordprijs )
print ('totaalprijs', totaalprijs)
print ('de feestluch kost me bij de bakker' , totaalprijs , ' cent voor' , aantalproduct1 , ' croissantjes en' , aantalproduct2 , ' stockborden  als de kortingsbonen nog geldig zijn')
