import random
print('\n\t\t\tЦе гра "Відгадай число:)" !!! ')
number = random.randint(1,100)
guest  = int(input('\nЯ загадав число від 1 до 100, давай спробуй вгадай:'))
popitka = 1
while guest != number:
    if guest>number:
        print("Моє число  менше :(")
    else:
        print("Моє число більше :)")
    guest = int(input('Спробуй ще раз :'))
    popitka+=1
print('Ура! Ти вгадав, так, це число :', number, '\n Ти вгадав його за ', popitka, ' спроби\n')
input('\t\t\tНатисни ентер для виходу :) ')

