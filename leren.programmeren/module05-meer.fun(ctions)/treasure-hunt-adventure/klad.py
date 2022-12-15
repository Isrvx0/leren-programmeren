from functions import copper2silver, silver2gold, copper2gold, platinum2gold, getPersonCashInGold


lestDictionairy2 = {
    'platinum' : 22,
    'gold' : 38,
    'silver' : 12,
    'copper' : 3120
}

coin = 0
for key , value in lestDictionairy2.items():
    if key == 'platinum':
        coin += platinum2gold(value)
    elif key == 'gold':
        coin += value
    elif key == 'silver':
        coin += silver2gold(value)
    elif key == 'copper':
        coin += copper2gold(value)
print(coin)

