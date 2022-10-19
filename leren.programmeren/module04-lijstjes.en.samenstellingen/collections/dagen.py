WEEKDAGEN= ('maandag','dinsdag','woensdag','donderdag','vrijdag','zaterdag','zondag')
print('Alle dagen van de week zijn:' , WEEKDAGEN[:7])
print('De werkdagen zijn: ' , WEEKDAGEN [:5]) #tot 5 printen
print ('De weekenddagen zijn: ' , WEEKDAGEN[-2:])

# # #  # :: == Geheel getal omkeren en het dan terug converteren naar een string
# print('\nAlle dagen van de week in omgekeerde volgorde zijn: ', WEEKDAGEN [:: -1])
# print('De werkdagen in omgekeerde volgorde zijn: ' , WEEKDAGEN [-3::-1])
# print('De weekenddagen in omgekeerde volgorde zijn: ' ,WEEKDAGEN [:4:-1]) #begint van 4


week_string = "Alle dagen van de week in omgekeerde volgorde zijn:"
for x in range (6,-1,-1):
    week_string += WEEKDAGEN[x] + ", "
print(week_string)

week_string = "De werkdagen in omgekeerde volgorde zijn:"
for x in range (4,-1,-1):
    week_string += WEEKDAGEN[x] + ", "
print(week_string)

week_string = "De weekenddagen in omgekeerde volgorde zijn:"
for x in range (6,4,-1):
    week_string += WEEKDAGEN[x] + ", "
print(week_string)



