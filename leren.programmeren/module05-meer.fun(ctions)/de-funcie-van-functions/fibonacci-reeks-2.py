def getallenreeks_berekenen(nummer):
   if nummer <= 1:
       return nummer
   else:
       return(getallenreeks_berekenen(nummer-1) + getallenreeks_berekenen(nummer-2))

def tri_recursion(term):
    teller = 0
    while teller <= term :
        print(getallenreeks_berekenen(teller))
        teller +=1

nterms = int(input('Hoeveel getalen wil je? '))
print("Fibonacci getalen: ")
tri_recursion(nterms)

