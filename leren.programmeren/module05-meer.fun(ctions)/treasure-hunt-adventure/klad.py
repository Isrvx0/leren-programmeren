from data import friends
from functions import copper2gold , silver2gold , platinum2gold

def getCashInGoldFromPeople(people:list) -> float:
    value= 0
    for key in range (len(people)):
        if people[key]['price']['type']=='gold':
            amount = people[key]['cash']['gold'] * people[key]['price']['amount']
            value += amount
        if people[key]['price']['type']=='copper': 
            amount = copper2gold( people[key]['cash']['copper'] ) * people[key]['price']['amount']
            value += amount
        if people[key]['price']['type'] =='silver':
            amount = silver2gold (people[key]['cash']['silver']  * people[key]['price']['amount'])
            value += amount
        if people[key]['price']['type'] == 'platinum':
            amount =  platinum2gold(people[key]['cash']['platinum']) * people[key]['price']['amount']
            value += amount
    totaal = round(value,2)
    return totaal
