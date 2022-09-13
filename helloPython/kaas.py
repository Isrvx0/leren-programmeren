print (' welke kaas de gebruiker in zijn gedachte heeft')
print (" je antwoord moet 'ja' of 'nee ' zijn ")

geel = input (' is de kaas geel?') 
if geel == 'ja':
    gaten = input (" ziiten er gaten in?")
    if gaten == 'ja':
        duur = input (" is de kaas belangrijk duur?")
    if gaten == 'nee':
        hard= input ("is fr kaar hard als steen?")
        if hard == 'ja':
            print ("antwoord is Parmigiano Reggiano")
            if hard == 'nee':
                 print (" antwoord is Goude kaas")
                 if duur == 'ja':
                    print (" antwoord is Emmenthaler")
                    if duur == 'nee':
                        print ("antwoord is Leerdammer ")

if geel == 'nee':
    schimmel = input ('heeft de kaas blauwe schimmel?')
    if schimmel == 'ja':
        korst = input ('heeft de kaas een korst?')
        if korst == 'ja':
            print ("antwoord is Blue de Rochbaron")
            if korst == 'nee':
                print ("antwoord is Foume d'Ambert")
if schimmel == 'nee':
        korst1 = input ('heeft de kaas korst?')
        if korst1 == 'ja':
            print ("antwoord is Camembert")
        if korst1 == 'nee':
            print (" antwoord is mozzarella")
     






