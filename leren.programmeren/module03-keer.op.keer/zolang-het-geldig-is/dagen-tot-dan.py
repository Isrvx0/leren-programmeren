
weekdagen = ["ma","di","wo","do","vr",'za','zo']
while True:
    print ('wat is de dag van de vandaag? kies de juiste dag')
    today= input (' ma , di , wo , do , vr , za , zo .   ')
    if today in weekdagen:
        break

newLst = weekdagen[weekdagen.index(today)+1:]
while len(newLst) > 0:
        print(newLst[0])
        newLst = newLst[1:]

