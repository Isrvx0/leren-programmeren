from data import friends
from functions import COST_TENT_GOLD_PER_WEEK , silver2gold , COST_HORSE_SILVER_PER_DAY , JOURNEY_IN_DAYS



# if getTotalRentalCost(1,2) != 23.0:
# def getTotalRentalCost(horses:int, tents:int) -> float:             5.2

paard_gold = silver2gold(COST_HORSE_SILVER_PER_DAY)

paard_kosten = paard_gold * JOURNEY_IN_DAYS 
tent_kosten = COST_TENT_GOLD_PER_WEEK * 4
totaal = paard_kosten + tent_kosten

print(totaal)
