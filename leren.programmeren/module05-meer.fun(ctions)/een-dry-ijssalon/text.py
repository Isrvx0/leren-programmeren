smaken_list = [{ 
    'name' : 'aardbei',
    'amount' : 0,
    'price' : 1.70
},{ 
    'name' : 'chocolade',
    'amount' : 1,
    'price' : 1.70
},{ 
    'name' : 'munt',
    'amount' : 0,
    'price' : 1.70
},{ 
    'name' : 'vanille',
    'amount' : 0,
    'price' : 1.70
}]


lijst = [{ 
        'name' : 'bakjes',
        'amount' : 2,
        'price' : 1.70
    },{ 
        'name' : 'hoorntjes',
        'amount' : 3,
        'price' : 1.70
}]
bon = smaken_list

for item in bon:
    if item['amount'] == 0:
        bon.remove(item) 

for item in bon:
    print(item)











# # name             aantal * prijs     = totaal 

# name = []
# aantal = []
# price = []

# for index in range (0,len(smaken_list)):
#     name.append(smaken_list[index]['name'])

# for index in range (0,len(smaken_list)):
#     aantal.append(smaken_list[index]['amount'])

# for index in range (0,len(smaken_list)):
#     price.append(smaken_list[index]['price'])

# for name,aantal,price in zip(name,aantal,price):
#     print('{:10} {:10} {:5}'.format(name,aantal,price))




# # for index in range (0,len(smaken_list)):
# #     totaal = smaken_list[index]["amount"] * smaken_list[index]["price"]
# #     bon.append(f'{smaken_list[index]["name"]}{smaken_list[index]["amount"]} * {smaken_list[index]["price"]} = {totaal}')

# # # for i in bon:
# #     print(i)


# # print("{:<10} {:<10} ".format('ITEMS', 'HOEVEELHEID')) #namen van de kolommen.
# # for key in smaken_list:
# #     name = key['name']
# #     ("{:<10} {:<10} ".format(key, name))

