
# toPay = int(float(input('Amount to pay: '))* 100) #
# paid = int(float(input('Paid amount: ')) * 100) #
# change = paid - toPay #
# if change > 0: #
#   coinValue = 500 #
  
#   while change > 0 and coinValue > 0: #
#     nrCoins = change // coinValue #

#     if nrCoins > 0: #
#       print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #
#       nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
#       change -= nrCoinsReturned * coinValue #
#       totaal= nrCoinsReturned
#       totaal1= coinValue

# for i in [1, 3, 5, 7, 9]:
#     x = i**2 - (i-1)*(i+1)
#     print(x, end=", ") # prints 1, 1, 1, 1, 1, 


correct_guess=9
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess = int(input('Guess a number: '))
    guess_count += 1
    if guess == correct_guess:
        print('Congratulations! You won!')
        break
else:
    print('sorry you lost')