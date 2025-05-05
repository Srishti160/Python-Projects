import random
choices=('r' , 'p' , 's')
emojis= {'r':'🪨', 'p':'📃', 's':'✂️'}
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
        elif (user_choice=='r' and comp_choice=='s') or (user_choice=='p' and comp_choice=='r') or (user_choice=='s' and comp_choice=='p'):
            print("You win!")
        else:
            print("You loose!")
    
    cont=input("Continue?(y/n)").lower()
    if cont=='n':
        break

print("Thanks for playing!")
#if user chooses r and comp chooses r- tie
#if user chooses p and comp chooses p- tie
#if user chooses s and comp chooses s- tie
#if user chooses r and comp chooses p- lose
#if user chooses r and comp chooses s- win
#if user chooses p and comp chooses r- win
#if user chooses p and comp chooses s- loose
#if user chooses s and comp chooses r- loose
#if user chooses s and comp chooses p- win
#continue?
# if yes
# loop
#else end