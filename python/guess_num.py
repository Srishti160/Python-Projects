import random
num= random.randint(1,100)
while True:
    try:
        guess=int(input("Guess the number between 1-100 :"))
        if guess>num:
            print("Too High")
            continue
        elif guess<num:
            print("Too low")
            continue
        elif guess==num:
            print("Congrats! You have guess correct number..")
            break
        else:
            print("Invalid Input!") 
    except ValueError:
        print("Please enter valid number (between 1 to 100)")