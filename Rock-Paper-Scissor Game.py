import random

def rps(comp,mine):
    if (comp == 'r' and mine == 'p'):
        return True
    elif (comp == 'p' and mine == 's'):
        return True
    elif (comp == 's' and mine == 'r'):
        return True
    elif (comp == mine):
        return None
    else:
        return False

choice=('r','p','s')
comp=random.randint(0,2)
comp = choice[comp]
mine = input('''
r = rock
p = paper
s= scissor
Choose either r, p, s: ''')

print('Your choice:',mine)
print('My choice:',comp)

win = rps(comp,mine)
if win == True:
    print("You Won!")
elif win == None:
    print("Tied!")
else:
    print("Haha! Better luck next time!")

