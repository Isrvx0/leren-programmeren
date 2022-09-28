# name of student: Israa 
# number of student: 
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) #hier moet je het bedrag die je moet betalen voeren (en *100 is om van euro naar cent te wisselen ).
paid = int(float(input('Paid amount: ')) * 100) # hier moet je het bedrag die je hebt betaalt voeren. 
change = paid - toPay # het verschil tussen wat je hebt betaald en wat moet je nog betalen

if change > 0: #
  coinValue = 50 #hier is voor 50 cent
  
  while change > 0 and coinValue > 0: #
    nrCoins = change // coinValue #

    if nrCoins > 0: #
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
      change -= nrCoinsReturned * coinValue #

# comment on code below: 
    if coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: #
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')