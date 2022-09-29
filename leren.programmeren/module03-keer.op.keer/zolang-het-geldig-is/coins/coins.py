# name of student: 
# number of student:
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) # you enter the number in euros (And here *100 to change It to cents)
paid = int(float(input('Paid amount: ')) * 100) #
change = paid - toPay #bereken the difference between the two numbers
if change > 0: # if change greater than 0 , the coin value is 50
  coinValue = 50 #
  
  while change > 0 and coinValue > 0: #while the change and coin value greater than 0
    nrCoins = change // coinValue #continues to give the number of coins

    if nrCoins > 0: # if number of coins greater than 0, print the follow :
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

if change > 0: # at the end, if the change greater than 0, it means you haven't returned ** cents
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')