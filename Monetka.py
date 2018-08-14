
import random
print('\n\t\t\tCe gra y monetky!')
orel = 0
reshka = 0
score = 1
count = int(input('Vvedu skilku paz pidkunytu monety:' ))
while score <= count:
    input('Pidkun monetky! Press Enter:')
    monetka = random.randint(1,2)
    if monetka == 1:
        reshka+=1
        print('Vupala reshka...')
    else:
        orel+=1
        print('Vupav orel...')
    score +=1
print('Reshka vupala  ', reshka, ' raziv')
print('Orel vupav  ', orel, ' raziv')
if reshka > orel:
    print('\t\t\tWin Reshka!\n')
elif reshka < orel:
    print('\t\t\tWin Orel!\n')
else:
    print('DEAD HEAT!!!')

input('\tPress Enter to exit....')
