from functions import getInterestingInvestors , getAdventuringInvestors
from data import friends , investors , mainCharacter


interestingInvestors = getInterestingInvestors(investors)
adventuringInvestors = getAdventuringInvestors(investors)
fellowship = [mainCharacter] + friends + investors
earnings= []
investors_names = []
profitGold = 500
investorsGoud = 0


for index in range (len(fellowship)):
    if fellowship[index] in [mainCharacter]:
        print('hello')





# def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
#     # haal de juiste inhoud op
#     adventuringFriends = getAdventuringFriends(friends)
#     interestingInvestors = getInterestingInvestors(investors)
#     adventuringInvestors = getAdventuringInvestors(investors)
#     aftrek_goud = 0
#     goudToAvonturier = 0.0

#     #lijst maken 
#     fellowship = [mainCharacter] + adventuringFriends + adventuringInvestors #voor het delen van goud
#     earnings = []
#     earnings_names = []

#     # verdeel de uitkomsten
#     for index in range (len(interestingInvestors)): #Delen van goud voor Investors
#         startCash = round(getPersonCashInGold(interestingInvestors[index]['cash']),2)
#         investorsGoud = round(profitGold / 100 * interestingInvestors[index][ 'profitReturn'],2)
#         endCash = startCash + investorsGoud
#         earnings.append({
#                     'name'   : interestingInvestors[index]['name'],
#                     'start'  : startCash,
#                     'end'    : endCash
#                 }) 
#         aftrek_goud += investorsGoud
    
#     profitGold -= aftrek_goud
#     adventurCut = profitGold / len(fellowship)

#     for name_index in range (len(adventuringInvestors)):
#         earnings_names.append(adventuringInvestors[name_index]['name'])

#     for index in range(len(earnings)):
#         if earnings[index]['name'] in earnings_names:
#             updateCash = earnings[index]['end'] + adventurCut
#             earnings[index]['end'] = updateCash

#     for teller in range (len(adventuringFriends)): 
#         startCash = round(getPersonCashInGold(adventuringFriends[teller]['cash']) , 2)
#         if adventuringFriends[teller]['adventuring']:
#             goudToAvonturier += 10        
#             endCash = startCash + (adventurCut-10)
#             earnings.append({
#                     'name'   : adventuringFriends[teller]['name'],
#                     'start'  : startCash,
#                     'end'    : endCash
#                 })   
#         else:
#             endCash = startCash + adventurCut
#             earnings.append({
#                         'name'   : adventuringFriends[teller]['name'],
#                         'start'  : startCash,
#                         'end'    : endCash
#                     })

#     mainCharacter_startCash = round(getPersonCashInGold(mainCharacter['cash']) , 2)
#     mainCharacter_endCash = mainCharacter_startCash + goudToAvonturier + adventurCut
#     earnings.append({
#                 'name'   : mainCharacter['name'],
#                 'start'  : mainCharacter_startCash,
#                 'end'    : mainCharacter_endCash
#             })
        
#     return earnings