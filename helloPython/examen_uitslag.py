# examen uitslag berekenen

#errormessage
errormessage = ('Geen geldig geheel getal! Probeer het opnieuw...')
#scores invoeren (done)
while True:
    try:
        score1 = int ( input ('voer aub de 1e score, voor excellente acties (is minimaal 0 en maximaal 6)') )
        break
    except ValueError:
        print(errormessage)
while True:
    try:
        score2 = int ( input ('voer aub de 2e score, voor professionele acties (is minimaal 0 en maximaal 8)'))
        break
    except ValueError:
        print(errormessage)
while True:
    try:
        score3 = int ( input ('voer aub de 3e score, voor onprofessionele acties (minimaal 0 en maximaal 5)') )
        break
    except ValueError:
        print(errormessage)
while True:
    try:
        score4 = int ( input ('voer aub de 4e score, voor slechte acties (minimaal 0 en maximaal 2)') )
        break
    except ValueError:
        print(errormessage)

#examen uitsalg bereken
total_score = score1 + score2 - score3 - score4
print (f"total score is: {total_score} ") 

# examenuitslag  beoordeling
voldoende_score = score4 == 0 and total_score > 7 and total_score < 13
voldoende_score2 = score4 == 1 and total_score > 9
goed_score = score2 == 8 and score1 > 4 and score3 == 0 and score4 == 0 

if voldoende_score or voldoende_score2 : 
    print ('voldoende') 
elif goed_score :
    print ("Goed")
else:
    print ("Onvoldoende ")



