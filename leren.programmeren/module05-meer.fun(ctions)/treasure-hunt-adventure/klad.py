from data import friends
from functions import copper2gold , silver2gold , platinum2gold

testList3 = [{
    'name' : 'Diamand',
    'amount' : 1,
    'unit' : '',
    'price' : {
        'amount' : 7,
        'type' : 'platinum'
    }
}]


def getItemsValueInGold(items:list) -> float:
    value= 0
    for key in range (len(items)):
        if items[key]['price']['type'] =='gold':
            amount = items[key]['price']['amount']
            value += amount
        elif items[key]['price']['type'] =='copper':
            amount = items[key]['price']['amount']
            copper2gold(amount)
            value += amount
        elif items[key]['price']['type'] =='silver':
            amount = items[key]['price']['amount']
            silver2gold(amount)
            value += amount
        elif items[key]['price']['type'] =='platinum':
            amount = items[key]['price']['amount']
            platinum2gold(amount)
            value += amount
    return (value)


print(getItemsValueInGold(testList3))

if getItemsValueInGold(testList3) != 175:
    print("foute")
else:
    print('goed')