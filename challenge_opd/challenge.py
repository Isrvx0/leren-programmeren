
zin= input ('Voer een zin of word:   ')
zin2 = ""
for x in zin:
    zin2 += x
    zin2 *= 2
print (zin2)

#----------

# oefenen met for Loop:

for x in range (0,11):
    print (x) #van 1 tot 10

for v in range (1,22,2):
    print (v) #tellen 2 stappen

nummer= input ('voer een nummer:   ')
for i in range (1,11):
    print ( i * nummer ) #tafel van getalen

for i in range (30,-1,-1):
    print (i) #aftellen
# start , stop , stap-getalen

#----------

try:
    if 'Peer' > 'appel':
        print ('Ok')
    else: 
        print ('Not OK ')
except:
    print ('ERROR !')