import random
choices=('r' , 'p' , 's')
emojis= {'r':'🪨', 'p':'📃', 's':'✂️'}
user_win=0 
comp_win=0 
tie=0
loose=0

def get_user_choice():
    while True:
        user_choice=input("Rock,Paper,Scissor? (r/p/s):").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid Choice!")

def display_choice(user_choice, comp_choice):
    print(f'You choose {emojis[user_choice]}')
    print(f"Computer choose {emojis[comp_choice]}")

def get_res(user_choice, comp_choice):
    global user_win, comp_win, tie, loose 
    if user_choice==comp_choice:
        print('Tie!')
        tie+=1
    elif (user_choice=='r' and comp_choice=='s') or (user_choice=='p' and comp_choice=='r') or (user_choice=='s' and comp_choice=='p'):
        print("You win!")
        user_win+=1
    else:
        print("You lose!")
        comp_win+=1
        loose+=1

def Overall_score():
    print("Overall Winner:")
    if user_win>comp_win:
        print("!!! YOU WON !!!")
    elif user_win == comp_win:
        print("OOPS! A TIE....")
    else:
        print("...SORRY! YOU LOSE...")

def play():
    while True:
        user_choice= get_user_choice()
        comp_choice=random.choice(choices)
        display_choice(user_choice, comp_choice)
        get_res(user_choice, comp_choice)

        cont=input("Continue?(y/n)").lower()
        if cont=='n':
            break

    Overall_score()
    print(f"WIN SCORE {user_win} ; LOOSE SCORE {loose} ; TIE SCORE {tie}")


play()
