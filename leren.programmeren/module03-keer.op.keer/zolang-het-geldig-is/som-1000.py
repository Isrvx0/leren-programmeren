num = 50
som = 0
sommen_lijst= ""
while som < 1000:
    som += num
    sommen_lijst += f"coins returned: {num} van {som} cents\n"
    print(f"Het getal is =  {num}. De som wordt {som}")
    print (sommen_lijst)
    num += 1

print('The end')
