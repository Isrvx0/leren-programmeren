import random

num = random.randint(1, 10)
guess = None
guess1= random.randint (1,5)
print ("guess a number between 1 and 10: ")
print (f"Je hebt allen {guess1} kansen om het gehele getal te raden!")

count = 0
while count < guess1:
	count += 1

	guess = int(input("raad de nummer:- "))
	if guess == num:
		print("Gefeliciteerd het is je gelukt in ",
			count, " keer")
		quit
		break
	elif guess > num:
		print("You guessed too high!")
	elif guess < num:
		print("You Guessed too small!")
	
if count >= guess1:
	print("De nummer is", num)
	print("Better Luck Next time!")
	quit

