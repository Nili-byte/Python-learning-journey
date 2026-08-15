print("="*15,"rock paper scissors","="*15)

import random


computer = random.choice([1,0,-1])


options = {"R":1,"S":0,"P":-1}

dic = {1:"ROCK",0:"SCISSOR",-1:"PAPER"}
user = input("Enter the first letter of your choice.... : ").upper()
userf = options[user]

print(f"You chose : {dic[userf]} \nComputer chose : {dic[computer]}")



if (computer == userf):
        print("Draw")

elif(computer == 1 and userf == -1):
        print("You won")
elif(computer == -1 and userf == 1):
        print("Computer won")
elif(computer == 0 and userf == -1):
        print("You won")
elif(computer == -1 and userf == 0):
        print("Computer won")
elif(computer == 1 and userf == 0):
        print("Computer  won")
elif(computer == 0 and userf == 1):
        print("You won")








