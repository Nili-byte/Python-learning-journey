print("hello world")

def sothing (x,y):
    try:
        a = int(input("Enter a number to its square: "))

        x = print(f"{a**2}")
        return x
        
    except:
        print("Invalid")
        



    try:
        t = int(input("Enter your number for multiplicaton table"))

        for i in range(1,11):
            print(f"{t} X {i} = {t*i}")

    except:
        print("invalid")

    finally:
        print("i'm always here for you")



sothing(3,4)
print("hello world")
