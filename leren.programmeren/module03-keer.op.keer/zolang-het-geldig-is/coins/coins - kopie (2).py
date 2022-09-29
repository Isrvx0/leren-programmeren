# name of student: 
# number of student:
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))) #
paid = int(float(input('Paid amount: ')) ) #
change = paid - toPay #

if change > 0: #
  coinValue = 5 #
  
  while change > 0 and coinValue > 0: #
    nrCoins = change // coinValue #

    if nrCoins > 0: #
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
      change -= nrCoinsReturned * coinValue #

# comment on code below: 
    if coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    elif coinValue == 1:
      coinValue = 0.5
    elif coinValue == 0.5:
      coinValue = 0.2
    elif coinValue == 0.2:
      coinValue = 0.1
    else:
      coinValue = 0

if change > 0: #
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')