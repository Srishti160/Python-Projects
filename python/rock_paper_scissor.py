import random
choices=('r' , 'p' , 's')
emojis= {'r':'🪨', 'p':'📃', 's':'✂️'}
user_win=0
comp_win=0
tie=0
loose=0

while True:
    user_choice=input("Rock,Paper,Scissor? (r/p/s):").lower()
    if user_choice not in choices:
        print("Invalid choice!")
        continue

    else:
        comp_choice=random.choice(choices)
        print(f'You choose {emojis[user_choice]}')
        print(f"Computer choose {emojis[comp_choice]}")
    
        if user_choice==comp_choice:
            print('Tie!')
            tie=+1
        elif (user_choice=='r' and comp_choice=='s') or (user_choice=='p' and comp_choice=='r') or (user_choice=='s' and comp_choice=='p'):
            print("You win!")
            user_win=+1
        else:
            print("You loose!")
            comp_win=+1
            loose=+1
    
    cont=input("Continue?(y/n)").lower()
    if cont=='n':
        break

print("Overall Winner:")
if user_win>comp_win:
    print("!!! YOU WON !!!")
elif user_win == comp_win:
    print("OOPS! A TIE....")
else:
    print("...SORRY! YOU LOOSE...")

print(f"WIN SCORE {user_win} ; LOOSE SCORE {loose} ; TIE SCORE {tie}")