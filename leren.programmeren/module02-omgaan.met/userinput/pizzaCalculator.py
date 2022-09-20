#pizzaCalculator.py
# Israa Almahmoud

print (" Feeling Hungry? Order now ")
x = input ('what is your name')
print ('hello,' + x ) 
errormessage = "No valid integer! Please try again ..."

# order
menukaart = print (" small pizza (€7) , medium pizza (€8.50) , large pizza (€12.50)" )

print (" Hoeveel pizza's wil je ? ")
while True:
    try:
        smallpizza = input("aantal small pizaa's ")
        smallpizza= int(smallpizza)
        break
    except ValueError:
        print(errormessage)
while True:
    try:
        mediumpizza = input("aantal medium pizaa's ")
        mediumpizza= int(mediumpizza)
        break
    except ValueError:
        print(errormessage)

while True:
    try:
        largepizza = input("aantal large pizaa's ")
        largepizza= int(largepizza)
        break
    except ValueError:
        print(errormessage)

# kosten 
smallpizza1 = 7
smallpizzakosten = smallpizza * smallpizza1
mediumpizza1 = 8.50
mediumpizzakosten = float ( mediumpizza * mediumpizza1 )
largepizza1 = 12.50
largepizzakosten = float ( largepizza + largepizza1 )

kosten = mediumpizzakosten + smallpizzakosten + largepizzakosten

print ('subtotaal' ,  kosten )
print ('bezorgkosten €2 ')
totaalkosten =  float ( kosten + 2 ) 
print ('totaal kosten ' , totaalkosten )
print ("    Thanks for your order ! ")

