from fruitmand import fruitmand
import random

hoeveel_fruit= int(input("Hoeveel fruit wil je? (Max. 7)  "))

random.shuffle(fruitmand)
for fruit in range (hoeveel_fruit):
    print(fruitmand[fruit]['name'])
