from functions import *
from data import *

testGearList3 = [{
    'amount' : 1,
    'price' : {
        'amount' : 2,
        'type' : 'platinum'
    }
},{
    'amount' : 5,
    'price' : {
        'amount' : 7,
        'type' : 'silver'
    }
},{
    'amount' : 19,
    'price' : {
        'amount' : 10,
        'type' : 'copper'
    }
}]


testInverstorsList3 = [{
    'profitReturn' : 5,
    'adventuring' : True
},{
    'profitReturn' : 9,
    'adventuring' : True
},{
    'profitReturn' : 1,
    'adventuring' : False
}]


print(getAdventuringInvestors(testInverstorsList3))
print(getTotalInvestorsCosts(testInverstorsList3,testGearList3))
print(getItemsValueInGold(testGearList3))

copper = copper2gold(10) * 19
silver = silver2gold(7) * 5
platinum = platinum2gold(2) * 1
totaal = platinum + silver + copper

paarden = getNumberOfHorsesNeeded (2)
tent = getNumberOfTentsNeeded(2)
rent = getTotalRentalCost(paarden,tent)
food = getJourneyFoodCostsInGold(2,paarden)
cost = food + rent + totaal

print(cost)