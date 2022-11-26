def getallenreeks_berekenen(nummer):
   if nummer <= 1:
       return nummer
   else:
       return(getallenreeks_berekenen(nummer-1) + getallenreeks_berekenen(nummer-2))

nterms = int(input('Hoeveel getalen wil je? '))

if nterms <= 0:
   print("Mag alleen positieve cijfers")
else:
   print("Fibonacci getalen: ")
   for i in range(nterms):
       print(getallenreeks_berekenen(i))

#_________________ 2e manieer :

term= int(input('Hoeveel getalen wil je?  '))

def getallenreeks_berekenen(num):
    nummer_1 , nummer_2 = 0 , 1
    if num == 1 :
        print(f"de getallenreeks: {term} ")
    else:
        print (nummer_1)
        print (nummer_2)
        for i in range (term):
            answer = nummer_2 + nummer_1
            nummer_1 = nummer_2
            nummer_2 = answer
            print(answer)
getallenreeks_berekenen (term) 