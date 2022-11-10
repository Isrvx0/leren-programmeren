from fruitmand import fruitmand

fruit = filter (lambda fruit: fruit['name'] == 'appel' , fruitmand)
for f in fruit:
    print (f['weight'])


