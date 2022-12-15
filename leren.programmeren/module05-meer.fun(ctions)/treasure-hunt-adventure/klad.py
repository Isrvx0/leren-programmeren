from data import *
from functions import copper2gold 

people = 10
horses = 10

cost_people = people * copper2gold(COST_FOOD_HUMAN_COPPER_PER_DAY)
coste_horses = horses * copper2gold(COST_FOOD_HORSE_COPPER_PER_DAY)
totaal = round((cost_people + coste_horses) * JOURNEY_IN_DAYS , 2)
print (totaal)