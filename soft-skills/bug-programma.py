name= print('voer je naam') #hier moet een Input

for i in name # hier moet nog (:)
    print('hallo {name}') # moet een (f) voor de ('')

Leeftijd= input('wat is je leeftijd') #moet nog een (int) voor de input
Leeftijd += 5 # hier krijg je een erorr 
print('je leeftijd na 5 jaar is {leeftijd}') # moet een (f) voor de ('')

# import random
choice= input('kies een random nummer tussen 1 en 10  ') #moet nog een (int) voor de input
random_nummer = random.choice(1,10) #hier moet een random.randint en niet choice + moet nog (import random)
if choice == random_nummer # hier moet nog (:)
    print('Dat is goed')
    else: #else moet onder de (if) !
        print('prober nog een keer')