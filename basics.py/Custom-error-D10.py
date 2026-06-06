n = int(input("Enter your rating out of 10 : "))

if (n<0 or n>10):
    raise ValueError("Invaild i said out 10 and not negative")

else:
    print("Thankyou for your opinion")