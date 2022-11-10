from fruitmand import fruitmand
import random

hoeveel_fruit= int(input(f"Hoeveel fruit wil je? max {len(fruitmand)} "))

random.shuffle(fruitmand)
for teller in range (hoeveel_fruit):
    print(fruitmand[teller]['name'])
