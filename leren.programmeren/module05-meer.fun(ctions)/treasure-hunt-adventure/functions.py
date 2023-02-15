import time
import math
from termcolor import colored
from data import JOURNEY_IN_DAYS , COST_FOOD_HORSE_COPPER_PER_DAY , COST_FOOD_HUMAN_COPPER_PER_DAY , COST_HORSE_SILVER_PER_DAY , COST_TENT_GOLD_PER_WEEK , NUMBER_OF_PEOPLE_FOR_ONE_HORSE , NUMBER_OF_PEOPLE_FOR_ONE_TENT , COST_INN_HORSE_COPPER_PER_NIGHT , COST_INN_HUMAN_SILVER_PER_NIGHT

##################### M04.D02.O2 #####################

def copper2silver(copper:int) -> float:
    answer = 1 / 10 * copper
    return answer

def silver2gold(silver:int) -> float:
    answer = 1 / 5 * silver
    return answer

def copper2gold(copper:int) -> float:
    answer = 1 / 50 * copper 
    return answer

def platinum2gold(platinum:int) -> float:
    answer = 25 * platinum
    return answer

def getPersonCashInGold(personCash:dict) -> float:
    coin = 0
    for key , value in personCash.items():
        if key == 'platinum':
            coin += platinum2gold(value)
        elif key == 'gold':
            coin += value
        elif key == 'silver':
            coin += silver2gold(value)
        elif key == 'copper':
            coin += copper2gold(value)
    return coin

##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    cost_people = people * copper2gold(COST_FOOD_HUMAN_COPPER_PER_DAY)
    coste_horses = horses * copper2gold(COST_FOOD_HORSE_COPPER_PER_DAY)
    totaal = round((cost_people + coste_horses) * JOURNEY_IN_DAYS , 2)
    return totaal

##################### M04.D02.O5 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    newlist = []
    for teller in range (0,len(list)):
        if list[teller][key] == value: 
                newlist.append(list[teller])
    return newlist

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people,'adventuring',True)

def getShareWithFriends(friends:list) -> int:
    return getFromListByKeyIs(friends,'shareWith',True)

def getAdventuringFriends(friends:list) -> list:
    newlist= []
    for teller in range (0,len(friends)):
        if friends[teller]['adventuring'] and friends[teller]['shareWith']: 
            newlist.append(friends[teller])
    return newlist 
        
##################### M04.D02.O6 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    NumberOfHorses = round(people / NUMBER_OF_PEOPLE_FOR_ONE_HORSE)
    return NumberOfHorses

def getNumberOfTentsNeeded(people:int) -> int:
    NumberOfTents = math.ceil(people / NUMBER_OF_PEOPLE_FOR_ONE_TENT)
    return NumberOfTents

def getTotalRentalCost(horses:int, tents:int) -> float:
    paard_gold = silver2gold(COST_HORSE_SILVER_PER_DAY)
    
    paard_kosten = paard_gold * JOURNEY_IN_DAYS * horses
    tent_kosten = COST_TENT_GOLD_PER_WEEK * tents * 2
    totaal = paard_kosten + tent_kosten
    return totaal

##################### M04.D02.O7 #####################

def getItemsAsText(items:list) -> str:
    converted= ""
    for key in range (len(items)):
        amount = str(items[key]['amount'])
        converted += amount + items[key]['unit'] + " " + items[key]['name']
        if key < len(items) -1:
            converted += ','
    return(converted)

def getItemsValueInGold(items:list) -> float:
    value= 0
    for key in range (len(items)):
        if items[key]['price']['type'] =='gold':
            amount = items[key]['price']['amount'] * items[key]['amount']
            value += amount
        elif items[key]['price']['type'] =='copper':
            amount = copper2gold( items[key]['price']['amount']) * items[key]['amount']
            value += amount
        elif items[key]['price']['type'] =='silver':
            amount = silver2gold (items[key]['price']['amount']) * items[key]['amount']
            value += amount
        elif items[key]['price']['type'] =='platinum':
            amount =  platinum2gold(items[key]['price']['amount']) * items[key]['amount']
            value += amount
    return round(value,2)

##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people:list) -> float:
    value= 0
    for key in range (len(people)):
        amount = people[key]['cash']['gold']
        value += amount
        amount = copper2gold( people[key]['cash']['copper']) 
        value += amount
        amount = silver2gold (people[key]['cash']['silver']) 
        value += amount
        amount =  platinum2gold(people[key]['cash']['platinum'])
        value += amount
    totaal = round(value,2)
    return totaal

##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    InterestingInvestors = []
    for index in range(0,len(investors)):    
        if investors[index]['profitReturn'] <= 10:
            InterestingInvestors.append(investors[index])
    return InterestingInvestors

def getAdventuringInvestors(investors:list) -> list:
    adventuringInvestors= []
    for index in range (len(getInterestingInvestors(investors))):
        if getInterestingInvestors(investors)[index]['adventuring'] :
            adventuringInvestors.append(getInterestingInvestors(investors)[index])
    return adventuringInvestors

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    people= getAdventuringInvestors(investors)
    rentalCost = getTotalRentalCost(1,1)
    foodCost = getJourneyFoodCostsInGold(1,1)
    totaal = (getItemsValueInGold(gear)  + rentalCost + foodCost) * len(people)
    return totaal

##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    people_cost = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT) * people
    horses_cost  = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT) * horses
    herberg_cost = people_cost  + horses_cost
    try:
        maxNachten = leftoverGold // herberg_cost
    except ZeroDivisionError: 
        maxNachten = 0
    return maxNachten

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    # rekent uit hoeveel alle nachten samen die in een herberg gespendeerd worden kosten
    people_cost = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT) * people
    horses_cost  = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT) * horses
    herberg_cost = round(nightsInInn * (people_cost + horses_cost) , 2)
    return herberg_cost

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    goldList = []
    AdventuringInvestors = getInterestingInvestors(investors)
    for teller in range (len(AdventuringInvestors)):
        investorsCuts = round(profitGold / 100 * AdventuringInvestors[teller][ 'profitReturn'] , 2)
        goldList.append(investorsCuts)
    return goldList

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:list) -> float:
    for gold in investorsCuts:
        profitGold -= gold
    adventurCut = round(profitGold / fellowship ,2)
    return adventurCut

##################### M04.D02.O13 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    # haal de juiste inhoud op
    adventuringFriends = getAdventuringFriends(friends)
    interestingInvestors = getInterestingInvestors(investors)
    adventuringInvestors = getAdventuringInvestors(investors)
    
    aftrek_goud = 0
    goudToAvonturier = 0.0
    
    #lijst maken 
    fellowship = [mainCharacter] + friends + investors 
    fellowship_adventurCut = [mainCharacter] + adventuringFriends + adventuringInvestors
    earnings = []

    # verdeel de uitkomsten
    for teller in range (len(interestingInvestors)): #profitReturn aftrekken van de profitGold om te kunnen verdelen.
         aftrek_goud += round(profitGold / 100 * interestingInvestors[teller][ 'profitReturn'],2)
    
    adventurCut = (profitGold -  aftrek_goud) / len(fellowship_adventurCut)
    
    for adventuring in  adventuringFriends:
        goudToAvonturier += 10 #goud van adventuring Friends to mainCharacter

    for index in range (len(fellowship)):
        startCash = round(getPersonCashInGold(fellowship[index]['cash']),2)
        if fellowship[index] in [mainCharacter]:
            endCash = startCash + goudToAvonturier + adventurCut
        elif fellowship[index] in investors:
            if fellowship[index] in interestingInvestors and fellowship[index] in adventuringInvestors :
                investorsGoud = round(profitGold / 100 * fellowship[index][ 'profitReturn'],2)
                endCash = startCash + investorsGoud + adventurCut
            elif fellowship[index] in interestingInvestors:
                investorsGoud = round(profitGold / 100 * fellowship[index][ 'profitReturn'],2)
                endCash = startCash + investorsGoud
                # if fellowship[index] in adventuringInvestors:
            else:
                endCash = startCash
        elif fellowship[index] in friends:
            if fellowship[index] in adventuringFriends:
                endCash = startCash + (adventurCut - 10)
            else:
                endCash = startCash 
        earnings.append({
                'name'   : fellowship[index]['name'],
                'start'  : startCash,
                'end'    : endCash
            })
    return earnings
    
##################### view functions #####################
def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()