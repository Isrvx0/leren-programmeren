from functions import *
from data import *
import math



def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    # rekent uit hoeveel alle nachten samen die in een herberg gespendeerd worden kosten
    people_cost = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT) * people
    horses_cost  = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT) * horses
    herberg_cost = nightsInInn * (people_cost + horses_cost)
    return herberg_cost

# rekent uit hoevel nachten er maximaal in een herberg overnacht kan worden. 
print(getJourneyInnCostsInGold(3,12,4))