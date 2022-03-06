# program to make a random number guessing number:
import random
while True:
    user = int(input('enter any number between 1 to 10 : '))
    i=random.randint(1,10)
    print('computer has choose ',i)
    if user<0 or user>10:
        print("choose between 1 to 10 only")
    elif user >i:
        print('you are the winner')
    elif user <i:
        print('computer is the winner this time')
    elif user==i:
        print('you both are equal')
    else:
        print('Oops! NO match try again')
    nextattempt= input('''want to play again type 'y' if not type 'n''')
    if nextattempt =='y':
        continue
    else:
        print('Thank you for playing random guessing number!')
        break
