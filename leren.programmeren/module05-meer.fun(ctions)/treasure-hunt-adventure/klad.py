from data import friends
from functions import getFromListByKeyIs

list = [{
    'name' : 'Jorick',
    'shareWith' : True,
    'adventuring' : True,
    'cash' : {
        'platinum' : 0,
        'gold' : 9,
        'silver' : 9,
        'copper' : 43
    }
},{
    'name' : 'Grommel',
    'shareWith' : True,
    'adventuring' : True,
    'cash' : {
        'platinum' : 1,
        'gold' : 2,
        'silver' : 2,
        'copper' : 8
    }
},{
    'name' : 'Tristan',
    'shareWith' : False,
    'adventuring' : True,
    'cash' : {
        'platinum' : 0,
        'gold' : 2,
        'silver' : 17,
        'copper' : 11
    }
},{
    'name' : 'Massimo',
    'shareWith' : True,
    'adventuring' : True,
    'cash' : {
        'platinum' : 0,
        'gold' : 5,
        'silver' : 9,
        'copper' : 3
    }
},{
    'name' : 'Durbane',
    'shareWith' : True,
    'adventuring' : False,
    'cash' : {
        'platinum' : 1,
        'gold' : 5,
        'silver' : 12,
        'copper' : 11
    }
},{
    'name' : 'Otho',
    'shareWith' : True,
    'adventuring' : True,
    'cash' : {
        'platinum' : 0,
        'gold' : 1,
        'silver' : 2,
        'copper' : 7
    }
}]

# key = input('choose 1 :   ')
# value = input('choose 2 :   ') 

# def boolean(choice):
#     if choice == "True":
#         return True
#     if choice == "False":
#         return False

# newlist = []

# if value == True or value == False:
#         for teller in range (0,len(list)):
#             if value == True:
#                 if list[teller][key]: 
#                      newlist.append(list[teller])
                     
#             elif value == False:
#                 if not list[teller][key]: 
#                      newlist.append(list[teller])
# else:
#         for teller in range (0,len(list)):
#             if list[teller][key] and list[teller][value]:
#                 newlist.append(list[teller])       




# for i in range (0,len(newlist)):
#     print(newlist[i])
# print("----------")
# for items in range (0,len(newlist)):
#     if newlist[items]['shareWith']:
#         print(newlist[items]['name'])      
# print("----------")





friends= []
shareWith = getFromListByKeyIs(list ,'shareWith', True)
adventuring = getFromListByKeyIs(list ,'adventuring', True) 


newlist= []

for it in shareWith:
    newlist.append(it)
for itt in adventuring:
    if itt not in newlist:
        newlist.append(itt)

for teller in range (0,len(newlist)):
    if newlist[teller]['shareWith'] and newlist[teller]['adventuring']:
        friends.append(newlist[teller]) 

for items in friends:
    print(items['name'])