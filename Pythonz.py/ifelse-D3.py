# print("Today we gonna do if else elif")
# a = int(input("Enter your number :\n"))
# if (a>0):
#     print("Your number is positive")
# elif( a == 0 ):
#     print("Your number is 0")
# else:
#     print("Your number is negative")




import random
number = random.randint(1, 100)
# this gives computer a random number
# rest you already know with if/elif!

guess = int(input("go on guess it :\n"))

if (guess == number ):
    print("You Won")
elif(guess>number):
    print("Nope its lower")
else:
    print("keep going its higher")



    import time
    time =time.strftime('%H:%M:%S')
    print(time)