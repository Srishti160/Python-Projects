import random
start=int(input("Enter the starting range of number :"))
stop= int(input("Enter ending range of the number :"))
limit=int(input("Enter the limit of guesses a player can make :"))
try:
    num= random.randint(start,stop)
except ValueError:
    print("Please enter valid range")

flag=0
n=1
count=0

while n<=limit:
    try:
        count=count+1
        guess=int(input("Guess the number :"))
        if guess>num:
            print("Too High!")
        elif guess<num:
            print("Too low!")
        elif guess==num:
            print("Congrats! You have guess correct number..")
            flag=1
            break
        else:
            print("Invalid Input!") 

    except ValueError:
        print("Please enter valid number ")
    
    n=n+1

if flag==0:
    print("You ran out of moves!")
    print("The number was", num)
else:
    print("Best Score:",count)