from fruitmand import fruitmand

for teller in range (0,len(fruitmand)):
    if fruitmand[teller]['round']: #if not -- if f false
        print(fruitmand[teller]['name'])