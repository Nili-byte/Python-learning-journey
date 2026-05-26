# print("hello world")


# a = 12
# while(a>6):
#     print(a)
#     a = a - 1

# i = 3
# while(i<15):
#     print(i)
#     i = i + 1

A = ("WELCOME TO GUESS THE NUMBER GAME")

print(A.center(50))



import random
number = random.randint(0,10)
print(number)

guess = 0

while(guess!=number):
    guess = int(input("Enter you number: "))
    if(guess>number):
        print("lower you scumbag")
    elif(guess<number):
        print("Think higher you shit")
    else:
        print("You Won")    








         






