# name of student: Israa
# number of student:
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))) #
paid = int(float(input('Paid amount: '))) #
change = paid - toPay #

if change > 0: 
  coinValue = 5 #
  
  while change > 0 and coinValue > 0: #
    nrCoins = change // coinValue #

    if coinValue == 5:
      print('return maximal ', nrCoins, ' banknotes of ', coinValue, ' euro' ) 
      nrCoinsReturned = int(input('How many banknotes of ' + str(coinValue) +  ' euro did you return? ')) 
      change -= nrCoinsReturned * coinValue 
    elif coinValue == 3 and coinValue == 2:
        print('return maximal ', nrCoins, ' coins of ', coinValue, ' euro' ) 
        nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' euro did you return? ')) 
        change -= nrCoinsReturned * coinValue 
    elif coinValue <=0.50:
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents' ) 
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cent did you return? ')) 
      change -= nrCoinsReturned * coinValue 


# comment on code below: 
    if coinValue == 5:
      coinValue = 3
    elif coinValue == 3:
      coinValue= 2
    elif coinValue == 2:
      coinValue = 0.5
    elif coinValue == 0.5:
      coinValue = 0.2
    elif coinValue == 0.2:
      coinValue = 0.1
    elif coinValue == 0.1:
      coinValue = 0.05
    elif coinValue == 0.05:
      coinValue = 0.02
    elif coinValue == 0.02:
      coinValue = 0.01
    else:
      coinValue = 0
  
if change > 0: #
  print('Change not returned: ', str(change) + ' cents')
  
else:
  print ('returned coins: ..  of 5 euro and ..  of 3/1 euro and  .. of cents')
  print('done')