# To make a dice roller, user ca also roll multiple dice according to their choice, also count the no. of times dice are rolled
import random
count=0

def multi_roll(n):
    global count
    for i in range(0,n):
        die1=random.randint(1,6)
        die2=random.randint(1,6)
        print(f'({die1},{die2})')
    count += 1
    return count
    
#To roll the dice
while True:
    choice = input("Roll a Dice? (y/n) :").lower()
    if choice=='y':
        n=int(input("How many Dice to roll together?"))
        if n==0:
            print("Invalid Entry!")
        else:
            multi_roll(n)
        
    elif choice=='n':
        print("Thanks for playing!")
        print("Total no. of times dice are rolled:", count)
        break
    else:
        print("invalid choice!")
