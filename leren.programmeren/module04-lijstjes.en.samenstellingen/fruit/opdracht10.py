from fruitmand import fruitmand

bewerkte_fruitmand= sorted(fruitmand , key= lambda weight:weight['weight'], reverse=True)
for fruit in range (0,7):
    print((bewerkte_fruitmand[fruit]['name']) , (bewerkte_fruitmand[fruit]['weight']))

# UITLEG:
# lambda = is een funcion (def) ,, varible is de name van lambda (key van fruitmand).
# (:) means Return == (return naar key).
