lijst = [{ 'name' : 'aardbei', 'amount' : 0, 'price' : 1.10},
             { 'name' : 'chocolade', 'amount' : 0, 'price' : 1.10},
             { 'name' : 'vanille', 'amount' : 0, 'price' : 1.10 },
             { 'name' : 'munt', 'amount' : 0, 'price' : 1.10 }]

smaken_lijst = ["aardbei" , 'munt']


for item in lijst:
    for smaak in smaken_lijst:
        if smaak == item['name']:
            item['amount'] += 1

for item in lijst:
    print(item)