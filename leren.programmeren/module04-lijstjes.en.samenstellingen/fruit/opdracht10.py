from fruitmand import fruitmand

bewerkte_fruitmand= sorted(fruitmand , key= lambda weight:weight['weight'], reverse=True)
for teller in range (0,len(fruitmand)):
    print((bewerkte_fruitmand[teller]['name']) , (bewerkte_fruitmand[teller]['weight']))

# UITLEG:
# lambda = is een funcion (def) ,, varible is de name van lambda (key van fruitmand).
# (:) means Return == (return naar key).


#oefenen
#namen van variabelen !!!!