def multipier (num):
    for i in range (1,11):
        print(f'{i} x {num} =  ' , i * num)

vraag = int(input("Van welk getal wilt u de tafel zien? "))
multipier(vraag)